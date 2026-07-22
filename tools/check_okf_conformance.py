#!/usr/bin/env python3
"""Check that one or more paik/ folders are, on their own, conformant OKF v0.1 bundles.

This is deliberately narrower than tools/paik_validate.py: it checks *only* the Open Knowledge
Format's own base conformance rule, nothing PAIK-specific. Per the OKF v0.1 spec
(github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), a bundle conforms if:

  1. Every non-reserved `.md` file has a parseable YAML frontmatter block.
  2. Every frontmatter block has a non-empty `type` field.
  3. Reserved filenames (`index.md`, `log.md`) follow their specified structure when present.

That's it - OKF does not know or care about PAIK's `id`, `depends_on`, `links[]`, or any of the
rest of the profile; a bundle can satisfy this script and still fail tools/paik_validate.py (an
OKF-valid but PAIK-invalid document), though not the other way around - passing the PAIK
validator implies passing this one, since PAIK's `type` values are always non-empty strings.

Usage: python tools/check_okf_conformance.py <paik-dir> [<paik-dir> ...]
"""
import glob
import os
import re
import sys

import yaml

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
RESERVED_FILENAMES = {"index.md", "log.md"}


def check_dir(bundle_dir):
    errors = []
    md_files = sorted(glob.glob(os.path.join(bundle_dir, "**", "*.md"), recursive=True))
    if not md_files:
        errors.append(f"{bundle_dir}: no .md files found")
        return errors

    for path in md_files:
        rel = os.path.relpath(path, bundle_dir)
        if os.path.basename(path) in RESERVED_FILENAMES:
            continue  # reserved filenames aren't concept documents; no type required

        with open(path, encoding="utf-8") as fh:
            content = fh.read()

        m = FRONTMATTER_RE.match(content)
        if not m:
            errors.append(f"{rel}: no parseable YAML frontmatter block")
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            errors.append(f"{rel}: frontmatter is not valid YAML: {e}")
            continue
        if not isinstance(fm, dict):
            errors.append(f"{rel}: frontmatter did not parse to a mapping")
            continue

        type_value = fm.get("type")
        if not isinstance(type_value, str) or not type_value.strip():
            errors.append(f"{rel}: missing or empty 'type' field (OKF's only required field)")

    return errors


def main():
    dirs = sys.argv[1:]
    if not dirs:
        print("Usage: python tools/check_okf_conformance.py <paik-dir> [<paik-dir> ...]")
        sys.exit(2)

    errors = []
    for d in dirs:
        errors.extend(check_dir(d))

    for e in errors:
        print(f"ERROR: {e}")
    if errors:
        print(f"\n{len(errors)} error(s) - not a conformant OKF v0.1 bundle.")
        sys.exit(1)
    print(f"OK - all {len(dirs)} folder(s) are conformant OKF v0.1 bundles.")


if __name__ == "__main__":
    main()
