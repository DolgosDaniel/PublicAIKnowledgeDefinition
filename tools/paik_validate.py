#!/usr/bin/env python3
"""Validate one or more paik/ folders against the PAIK v0.3 schemas and conventions.

Usage:
    python tools/paik_validate.py <paik-dir> [<paik-dir> ...]

Checks performed, per paik/ folder:
  - Every document's YAML frontmatter parses and validates against its kind's JSON Schema,
    including `format: uri` fields (a real FormatChecker is wired in, not jsonschema's silent
    default of skipping format assertions).
  - A document under components/ or environments/ has the matching kind (kind vs. placement).
  - Every id is unique across the *whole* project, not just within one kind - a component and
    an environment cannot share an id either.
  - Every relative reference resolves to a file that exists, AND that file's own `kind` matches
    what the referencing field expects: a `components` entry must point at a `kind: component`
    document, an `environments` entry at a `kind: environment` document.
  - The project document lists every component and every environment document that actually
    exists under the folder - nothing is silently unreachable from project.md.
  - Every `links[].component` / `links[].environment` qualifier, and every
    `databases[].component` qualifier, names a component/environment id that actually exists.
  - Every `depends_on` entry is a known component id, and the dependency graph has no cycles.
  - Every links[] entry has a non-empty `kind` (error) and, as a soft convention, a kebab-case
    `kind` (warning); and carries at least one of url/id/purpose/provider beyond `kind` (warning -
    a kind-only link isn't useful to a reader).
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

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMA_DIR = os.path.join(SCRIPT_DIR, "..", "paik-spec", "schema")

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ABSOLUTE_URL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")
KEBAB_CASE_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

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


def _compose_schema(common, kind_schema):
    """Flatten common.schema.json's allOf/$ref into kind_schema's own properties.

    jsonschema (as of 4.26, via the `referencing` library) has a real bug where a `format`
    assertion failing inside a property that's only declared through a *cross-resource* `$ref`
    (i.e. exactly the allOf: [{"$ref": "./common.schema.json"}] pattern the schema files use for
    readability) makes `unevaluatedProperties` forget that $ref'd schema contributed any
    properties at all - so a single invalid URI anywhere under `links[]` spuriously "unlocks" a
    false "'id'/'name'/'owner'/... were unexpected" error on top of the real one. Composing the
    schemas into one flat object before handing them to the validator sidesteps the bug entirely
    (same-document `$ref`s to `$defs`, which this still uses for `owner`/`link`, don't trigger
    it) without changing what's actually enforced or touching the on-disk schema files.
    """
    merged = dict(kind_schema)
    merged.pop("allOf", None)
    merged["$defs"] = {**common.get("$defs", {}), **kind_schema.get("$defs", {})}
    merged["properties"] = {**common.get("properties", {}), **kind_schema.get("properties", {})}
    merged["required"] = sorted(set(common.get("required", [])) | set(kind_schema.get("required", [])))
    return merged


def load_validators():
    schemas = {}
    for f in glob.glob(os.path.join(SCHEMA_DIR, "*.schema.json")):
        with open(f, encoding="utf-8") as fh:
            s = json.load(fh)
        schemas[s["$id"]] = s
    common = schemas["https://paik.dev/schema/common.schema.json"]
    return {
        kind: Draft202012Validator(
            _compose_schema(common, schemas[f"https://paik.dev/schema/{kind}.schema.json"]),
            format_checker=Draft202012Validator.FORMAT_CHECKER,
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

    docs = {}  # rel path -> frontmatter dict
    project_docs = []
    ids_all = {}  # id -> [(kind, rel), ...] across every kind
    component_docs = {}  # component id -> rel path
    environment_docs = {}  # environment id -> rel path

    # Pass 1: parse, schema-validate, collect ids, scan for secrets/link hygiene.
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

        cid = fm.get("id")
        if kind == "project":
            project_docs.append(rel)
        if cid:
            ids_all.setdefault(cid, []).append((kind, rel))
            if kind == "component":
                component_docs[cid] = rel
            elif kind == "environment":
                environment_docs[cid] = rel

        for pattern, label in SECRET_PATTERNS:
            if pattern.search(content):
                report.error(rel, f"looks like it contains {label} - never embed secret values, only where they live")

        for i, link in enumerate(fm.get("links") or []):
            if not isinstance(link, dict):
                continue
            k = link.get("kind")
            if not isinstance(k, str) or not k.strip():
                report.error(rel, f"links[{i}] has an empty or missing 'kind'")
            elif not KEBAB_CASE_RE.match(k):
                report.warn(rel, f"links[{i}] kind {k!r} isn't kebab-case - consider normalizing it")
            if not (link.keys() - {"kind"}):
                report.warn(rel, f"links[{i}] (kind: {k!r}) has only 'kind' - add url/id/purpose/provider or drop it")

    if len(project_docs) != 1:
        report.error(paik_dir, f"expected exactly one project document, found {len(project_docs)}: {project_docs}")

    # Ids must be unique across the whole project, not just within one kind.
    for cid, entries in ids_all.items():
        if len(entries) > 1:
            where = ", ".join(f"{k}:{r}" for k, r in entries)
            report.error(where, f"duplicate id {cid!r} used by {len(entries)} documents")

    # Pass 2: reference resolution, including that the target's kind matches expectations and
    # that the target is actually inside this paik/ folder (a relative link can walk outside it
    # with enough "../", which is never valid - PAIK documents only cross-reference each other).
    paik_abs = os.path.normpath(paik_dir)

    def resolve(base, r):
        target = os.path.normpath(os.path.join(base, r))
        try:
            common = os.path.commonpath([paik_abs, target])
        except ValueError:
            common = None  # e.g. different drives on Windows
        if common != paik_abs:
            return "outside", None, None
        if not os.path.isfile(target):
            return "missing", None, None
        target_rel = os.path.relpath(target, paik_abs)
        return "ok", target_rel, docs.get(target_rel)

    for rel, fm in docs.items():
        base = os.path.dirname(os.path.join(paik_dir, rel))

        for field, expected_kind in (("components", "component"), ("environments", "environment")):
            for r in fm.get(field) or []:
                status, target_rel, target_fm = resolve(base, r)
                if status == "outside":
                    report.error(rel, f"{field} entry {r!r} resolves outside the paik/ folder - PAIK documents must only reference other PAIK documents")
                elif status == "missing":
                    report.error(rel, f"{field} entry {r!r} does not resolve to a file")
                elif target_fm is not None and target_fm.get("kind") != expected_kind:
                    report.error(
                        rel,
                        f"{field} entry {r!r} points at a {target_fm.get('kind')!r} document, expected {expected_kind!r}",
                    )

        for i, link in enumerate(fm.get("links") or []):
            if not isinstance(link, dict):
                continue
            u = link.get("url")
            if u and not ABSOLUTE_URL_RE.match(u):
                status, _, _ = resolve(base, u)
                if status == "outside":
                    report.error(rel, f"links[{i}] url {u!r} resolves outside the paik/ folder - PAIK documents must only reference other PAIK documents")
                elif status == "missing":
                    report.error(rel, f"links[{i}] url {u!r} does not resolve to a file")
            comp = link.get("component")
            if comp is not None and comp not in component_docs:
                report.error(rel, f"links[{i}] component {comp!r} is not a known component id")
            envq = link.get("environment")
            if envq is not None and envq not in environment_docs:
                report.error(rel, f"links[{i}] environment {envq!r} is not a known environment id")

        if fm.get("kind") == "environment":
            for i, dbentry in enumerate(fm.get("databases") or []):
                if not isinstance(dbentry, dict):
                    continue
                comp = dbentry.get("component")
                if comp is not None and comp not in component_docs:
                    report.error(rel, f"databases[{i}] component {comp!r} is not a known component id")

    # The project document must list every component/environment that actually exists.
    if len(project_docs) == 1:
        project_rel = project_docs[0]
        proj_fm = docs[project_rel]
        proj_base = os.path.dirname(os.path.join(paik_dir, project_rel))
        listed_components = {
            os.path.normpath(os.path.join(proj_base, r)) for r in proj_fm.get("components") or []
        }
        listed_environments = {
            os.path.normpath(os.path.join(proj_base, r)) for r in proj_fm.get("environments") or []
        }
        for cid, rel in component_docs.items():
            if os.path.normpath(os.path.join(paik_dir, rel)) not in listed_components:
                report.error(project_rel, f"component {cid!r} ({rel}) exists but isn't listed in this project's 'components'")
        for eid, rel in environment_docs.items():
            if os.path.normpath(os.path.join(paik_dir, rel)) not in listed_environments:
                report.error(project_rel, f"environment {eid!r} ({rel}) exists but isn't listed in this project's 'environments'")

    # depends_on: unknown targets + cycles.
    component_ids = set(component_docs.keys())
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
