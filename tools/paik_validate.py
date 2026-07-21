#!/usr/bin/env python3
"""Validate one or more paik/ folders against the PAIK v0.3 schemas and conventions.

Usage:
    python tools/paik_validate.py <paik-dir> [<paik-dir> ...]

Checks performed, per paik/ folder:
  - Every document's YAML frontmatter parses and validates against its kind's JSON Schema.
  - A document under components/ or environments/ has the matching kind (kind vs. placement).
  - Every id (component, environment) is unique within the project.
  - Every relative reference (project/component `components`/`environments` arrays, and any
    non-absolute `links[].url`) resolves to a file that actually exists.
  - Every `depends_on` entry is a known component id, and the dependency graph has no cycles.
  - Every links[] entry carries at least one of url/id/purpose/provider beyond `kind` (a
    kind-only link isn't useful to a reader) - reported as a warning, not an error.
  - A best-effort regex scan for accidentally-embedded secrets (AWS keys, private key blocks,
    common vendor token prefixes, inline password/api_key-looking assignments) across the whole
    file, not just frontmatter - PAIK documents must only ever point at where a secret lives.

Exit code is non-zero if any error (not warning) was found in any of the given folders.
"""
import argparse
import glob
import json
import os
import re
import sys

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMA_DIR = os.path.join(SCRIPT_DIR, "..", "paik-spec", "schema")

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ABSOLUTE_URL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")

SECRET_PATTERNS = [
    (re.compile(r"AKIA[0-9A-Z]{16}"), "an AWS access key ID"),
    (re.compile(r"-----BEGIN (RSA |EC |OPENSSH |DSA |)PRIVATE KEY-----"), "a private key block"),
    (re.compile(r"sk_live_[0-9a-zA-Z]{16,}"), "a Stripe live secret key"),
    (re.compile(r"ghp_[0-9A-Za-z]{36}"), "a GitHub personal access token"),
    (re.compile(r"xox[baprs]-[0-9A-Za-z-]{10,}"), "a Slack token"),
    (
        re.compile(r"(?i)\b(password|passwd|secret|api[_-]?key)\s*[:=]\s*['\"]?[^\s'\"]{6,}"),
        "an inline credential-looking assignment",
    ),
]


def load_validators():
    schemas = {}
    for f in glob.glob(os.path.join(SCHEMA_DIR, "*.schema.json")):
        with open(f, encoding="utf-8") as fh:
            s = json.load(fh)
        schemas[s["$id"]] = s
    registry = Registry().with_resources(
        (uri, Resource.from_contents(s)) for uri, s in schemas.items()
    )
    return {
        kind: Draft202012Validator(
            schemas[f"https://paik.dev/schema/{kind}.schema.json"], registry=registry
        )
        for kind in ("project", "component", "environment")
    }


def expected_kind_for_path(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    if "environments" in parts:
        return "environment"
    if "components" in parts:
        return "component"
    return None


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{where}: {msg}")


def find_cycle(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}
    stack = []

    def visit(n):
        color[n] = GRAY
        stack.append(n)
        for m in graph.get(n, []):
            if m not in color:
                continue
            if color[m] == GRAY:
                return stack[stack.index(m):] + [m]
            if color[m] == WHITE:
                cyc = visit(m)
                if cyc:
                    return cyc
        stack.pop()
        color[n] = BLACK
        return None

    for n in list(graph):
        if color[n] == WHITE:
            cyc = visit(n)
            if cyc:
                return cyc
    return None


def validate_dir(paik_dir, validators, report):
    md_files = sorted(glob.glob(os.path.join(paik_dir, "**", "*.md"), recursive=True))
    if not md_files:
        report.error(paik_dir, "no .md files found")
        return

    docs = {}
    project_docs = []
    ids_by_kind = {"component": {}, "environment": {}}

    for path in md_files:
        rel = os.path.relpath(path, paik_dir)
        with open(path, encoding="utf-8") as fh:
            content = fh.read()

        m = FRONTMATTER_RE.match(content)
        if not m:
            report.error(rel, "no YAML frontmatter found (must open and close with '---')")
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            report.error(rel, f"frontmatter is not valid YAML: {e}")
            continue
        if not isinstance(fm, dict):
            report.error(rel, "frontmatter did not parse to a mapping")
            continue

        kind = fm.get("kind")
        if kind not in validators:
            report.error(rel, f"unknown or missing 'kind': {kind!r}")
            continue

        expected = expected_kind_for_path(rel)
        if expected and kind != expected:
            report.error(rel, f"file lives under {expected}s/ but kind is {kind!r}")

        for e in sorted(validators[kind].iter_errors(fm), key=lambda e: list(e.path)):
            report.error(rel, f"schema violation at {list(e.path)}: {e.message}")

        docs[rel] = fm
        if kind == "project":
            project_docs.append(rel)
        elif fm.get("id"):
            ids_by_kind[kind].setdefault(fm["id"], []).append(rel)

        for pattern, label in SECRET_PATTERNS:
            if pattern.search(content):
                report.error(rel, f"looks like it contains {label} - never embed secret values, only where they live")

        for i, link in enumerate(fm.get("links") or []):
            if isinstance(link, dict) and not (link.keys() - {"kind"}):
                report.warn(rel, f"links[{i}] (kind: {link.get('kind')!r}) has only 'kind' - add url/id/purpose/provider or drop it")

    if len(project_docs) != 1:
        report.error(paik_dir, f"expected exactly one project document, found {len(project_docs)}: {project_docs}")

    for kind, ids in ids_by_kind.items():
        for cid, paths in ids.items():
            if len(paths) > 1:
                report.error(", ".join(paths), f"duplicate {kind} id {cid!r}")

    for rel, fm in docs.items():
        base = os.path.dirname(os.path.join(paik_dir, rel))
        refs = list(fm.get("components") or []) + list(fm.get("environments") or [])
        for link in fm.get("links") or []:
            if isinstance(link, dict):
                u = link.get("url")
                if u and not ABSOLUTE_URL_RE.match(u):
                    refs.append(u)
        for r in refs:
            target = os.path.normpath(os.path.join(base, r))
            if not os.path.isfile(target):
                report.error(rel, f"reference {r!r} does not resolve to a file")

    component_ids = set(ids_by_kind["component"].keys())
    graph = {}
    for rel, fm in docs.items():
        if fm.get("kind") != "component":
            continue
        cid = fm.get("id")
        deps = fm.get("depends_on") or []
        graph[cid] = deps
        for d in deps:
            if d not in component_ids:
                report.error(rel, f"depends_on references unknown component id {d!r}")

    cycle = find_cycle(graph)
    if cycle:
        report.error(paik_dir, f"dependency cycle: {' -> '.join(cycle)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paik_dirs", nargs="+", help="one or more paik/ folders to validate")
    args = ap.parse_args()

    validators = load_validators()
    report = Report()
    for d in args.paik_dirs:
        validate_dir(d, validators, report)

    for w in report.warnings:
        print(f"WARNING: {w}")
    for e in report.errors:
        print(f"ERROR: {e}")

    if report.errors:
        print(f"\n{len(report.errors)} error(s), {len(report.warnings)} warning(s).")
        sys.exit(1)
    print(f"OK - 0 errors, {len(report.warnings)} warning(s).")


if __name__ == "__main__":
    main()
