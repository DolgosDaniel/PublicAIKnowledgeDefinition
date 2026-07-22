# Example: okf-compatible-project — Beacon Tasks

Every PAIK v0.4 example in this repo is, by construction, also a conformant
[Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
bundle — PAIK is a strict, software-project-specific domain profile of OKF, not a competing
format (see `paik-spec/SPEC.md`'s "Relationship to Open Knowledge Format" section). This example
exists to make that concrete, one file at a time, rather than leaving it as an abstract claim.

## Why every file here passes OKF base conformance

OKF's entire base-conformance rule is: every non-reserved `.md` file has a parseable YAML
frontmatter block with a non-empty `type` field. Every file in this `paik/` folder satisfies it:

| File | `type` |
|---|---|
| `project.md` | `paik-project` |
| `component.md` | `paik-component` |
| `environments/dev.md` | `paik-environment` |
| `environments/prod.md` | `paik-environment` |

Run it yourself:
```
python tools/check_okf_conformance.py examples/okf-compatible-project/paik
```
That script checks *only* the OKF rule above — nothing PAIK-specific. `tools/paik_validate.py`
checks both layers at once (see its module docstring).

## OKF concept identity vs. PAIK's `id`

OKF's concept identity is always the file's path with `.md` removed — no separate id field
exists at the OKF level. PAIK adds its own `id` field because file paths change (a rename, a
move into a `components/` subdirectory as a project grows) and `depends_on`/`links[].component`/
`links[].environment` all need something more stable to resolve against than a path. The two
routinely disagree, and that's fine — they answer different questions ("where is this concept
in the bundle" vs. "what does the rest of this project's graph call it"):

| File | OKF concept id (path, no `.md`) | PAIK `id` field |
|---|---|---|
| `project.md` | `project` | `beacon-tasks` |
| `component.md` | `component` | `beacon-tasks-service` |
| `environments/dev.md` | `environments/dev` | `dev` |
| `environments/prod.md` | `environments/prod` | `prod` |

## What makes this a *profile*, not just a compatible format

Beyond the one shared `type` field, this bundle also satisfies everything OKF leaves as
producer's choice or "soft guidance" that PAIK makes a hard, schema-enforced rule: closed
frontmatter per kind (no stray fields), a required `owner`, cross-references that must resolve
to a real file of the expected kind, and `depends_on` with no unknown targets or cycles. Try
introducing any of those mistakes and compare `tools/check_okf_conformance.py` (still passes -
OKF doesn't care) against `tools/paik_validate.py` (fails - PAIK does).

Start at [`paik/project.md`](paik/project.md).
