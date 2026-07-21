#!/usr/bin/env python3
"""Smoke-check that every template's YAML frontmatter actually parses.

Templates are full of <placeholder> values, so they can never pass full schema validation (see
paik_validate.py for that) - but their frontmatter must still be syntactically valid YAML, since
that's the whole point of shipping them as a starting point to copy. This is the check that
would have caught the unquoted host_ref placeholder in environments/environment.md.

Usage: python tools/check_templates.py [<templates-dir> ...]
Defaults to paik-spec/templates if no directory is given.
"""
import glob
import os
import re
import sys

import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DIR = os.path.join(SCRIPT_DIR, "..", "paik-spec", "templates")

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def check_dir(templates_dir):
    errors = []
    md_files = sorted(glob.glob(os.path.join(templates_dir, "**", "*.md"), recursive=True))
    if not md_files:
        errors.append(f"{templates_dir}: no .md files found")
        return errors
    for path in md_files:
        rel = os.path.relpath(path, templates_dir)
        with open(path, encoding="utf-8") as fh:
            content = fh.read()
        m = FRONTMATTER_RE.match(content)
        if not m:
            errors.append(f"{rel}: no YAML frontmatter found (must open and close with '---')")
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            errors.append(f"{rel}: frontmatter is not valid YAML: {e}")
            continue
        if not isinstance(fm, dict):
            errors.append(f"{rel}: frontmatter did not parse to a mapping")
    return errors


def main():
    dirs = sys.argv[1:] or [DEFAULT_DIR]
    errors = []
    for d in dirs:
        errors.extend(check_dir(d))
    for e in errors:
        print(f"ERROR: {e}")
    if errors:
        print(f"\n{len(errors)} error(s).")
        sys.exit(1)
    print("OK - every template's frontmatter is valid YAML.")


if __name__ == "__main__":
    main()
