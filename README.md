# PAIK (Public AI Knowledge Definition)

A tool-agnostic, Markdown-based standard for describing a software project end-to-end —
planning, implementation, and operations — by **linking** the systems a team already uses
instead of duplicating their content. PAIK v0.4 has exactly three document kinds — `project`,
`component`, `environment` — plus one generic, typed `links[]` list that covers ticketing (Jira,
...), knowledge base (Confluence, ...), API specs (SwaggerHub, ...), source repos (GitHub/GitLab,
...), third-party/external services, and where secrets are managed. There is no separate document
type per external system, and no separate `team` document — ownership is an inline `owner: {
name, ref }` on `project.md`/`component.md`. PAIK is also a strict domain profile of the
[Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
— every PAIK document is a valid OKF v0.1 concept, see `paik-spec/SPEC.md` section 2.

A PAIK document is never a copy of a ticket, a wiki page, or a database password — it's a small,
structured pointer: what system, which identifier, whose responsibility, how to reach it. The
systems stay the source of truth; PAIK stays the map.

## How to use

1. **Get the repo.** Either clone it:
   ```
   git clone https://github.com/DolgosDaniel/PublicAIKnowledgeDefinition.git
   ```
   or, if you don't need git history, download the ZIP from GitHub's "Code → Download ZIP"
   button and unzip it. Either way, the only part you actually need to copy from is
   `paik-spec/templates/` (and optionally `mcp/` and `skills/`, see step 5) — the rest of the
   repo (`examples/`, `paik-spec/SPEC.md`, `paik-spec/schema/`) is reference material you'll
   look back at, not something you copy into your own project.

2. **Copy the templates into your project as a `paik/` folder:**
   ```
   cp -r PublicAIKnowledgeDefinition/paik-spec/templates <your-project>/paik
   ```
   (`xcopy /E /I PublicAIKnowledgeDefinition\paik-spec\templates <your-project>\paik` on
   Windows). This becomes the `paik/` folder tooling looks for by default. The copy lands as
   `paik/components/component.md` and `paik/environments/environment.md` (the multi-service
   shape) — see step 3 for the one-service flatten.

3. **Pick a shape and fill in the placeholders.** The templates default to the multi-service
   shape (`components/*.md`); for a true one-service project, move `components/component.md` up
   to `paik/component.md` and change `project.md`'s `components:` entry from
   `components/component.md` to `component.md` to match — compare
   [`examples/simple-project/`](examples/simple-project/) (flattened) against
   [`examples/complex-project/`](examples/complex-project/) (`components/*.md`) to see both
   shapes side by side. Duplicate `environments/environment.md` once per real environment
   (`dev.md`, `staging.md`, `prod.md`, ...) either way — `environments/` is always a directory.
   Replace every `<placeholder>` with a real value: every field is documented in
   [`paik-spec/SPEC.md`](paik-spec/SPEC.md) and enforced by the matching schema in
   [`paik-spec/schema/`](paik-spec/schema/) — except a `links[]` item, which only requires a
   `kind`. Never invent a URL or identifier — leave a clearly marked `TODO` if a value is
   genuinely unknown.

4. **Validate.**
   ```
   pip install -r PublicAIKnowledgeDefinition/tools/requirements.txt
   python PublicAIKnowledgeDefinition/tools/paik_validate.py <your-project>/paik
   ```
   [`tools/paik_validate.py`](tools/paik_validate.py) checks two layers: OKF's own base
   conformance (every document has a non-empty `type`), then everything PAIK adds on top — YAML
   frontmatter against the matching schema, that every relative reference (`components`,
   `environments`, non-absolute `links[].url`) resolves to a real file of the expected `type`,
   that ids are unique and `depends_on` has no unknown targets or cycles, and a best-effort scan
   for accidentally-embedded secrets. [`tools/check_okf_conformance.py`](tools/check_okf_conformance.py)
   checks the OKF layer alone, if that's all you need. It's the same check
   [`.github/workflows/paik-validate.yml`](.github/workflows/paik-validate.yml) runs in CI
   against every example in this repo — copy that workflow into your own project to get the same
   check on every push/PR.

   To validate directly against the schemas with a different tool (Node's `ajv`, etc.) instead,
   remember every schema in `paik-spec/schema/` needs to be registered with the validator up
   front — a `$ref` like `./common.schema.json` won't resolve on its own unless your tool has
   all four schema files loaded (this is what trips up a naive one-schema-at-a-time validation
   attempt).

5. **(Optional) Wire up live access for an AI agent.** Copy the relevant server block(s) from
   [`mcp/`](mcp/README.md) into your project's `.mcp.json` so an agent can reach the live
   systems your `paik/` folder's `links[]` point at (Jira/Confluence, GitHub/GitLab, databases,
   API specs), and drop any of the [`skills/`](skills/README.md) — a portable Agent Skills
   format, not Claude-specific — wherever your agent looks for skills (`.claude/skills/` for
   Claude Code) for ready-made workflows (bootstrap, onboarding brief, health-check, sync).

6. **Commit `paik/` to your repo.** Every document only points at *where* things live — never a
   secret — see `SPEC.md` section 7. Whether a given `paik/` folder is safe to make public is a
   repo-level call you make the same way you would for any other doc in the repo; PAIK doesn't
   impose a per-document classification for this.

## Start here

- [`paik-spec/SPEC.md`](paik-spec/SPEC.md) — the normative standard: directory layout, its
  relationship to the Open Knowledge Format, common frontmatter, the `links` convention,
  cross-referencing, and the three document kinds.
- [`paik-spec/templates/`](paik-spec/templates/) — blank files to copy into a new project as its
  `paik/` folder.
- [`paik-spec/schema/`](paik-spec/schema/) — JSON Schema for every document kind's frontmatter.
- [`tools/paik_validate.py`](tools/paik_validate.py) — the validator described in step 4 above.
- [`tools/check_okf_conformance.py`](tools/check_okf_conformance.py) — checks only the OKF base
  rule, if you want proof a `paik/` folder is a conformant OKF v0.1 bundle on its own.
- [`paik-spec/LINKS.md`](paik-spec/LINKS.md) — non-normative recommendations for which fields to
  set on common `links[]` `kind` values, so different projects shape the same `kind` the same way.
- [`paik-spec/ROLES.md`](paik-spec/ROLES.md) — who typically edits which part of a `paik/`
  folder (product owner, designer, engineer, operator), plus an optional
  [`CODEOWNERS.example`](paik-spec/templates/CODEOWNERS.example).
- [`paik-spec/CHECKLIST.md`](paik-spec/CHECKLIST.md) — three honest "is this done?" tiers
  (minimal / development-ready / operations-ready), as documentation, not a new schema profile.
- [`paik-spec/TROUBLESHOOTING.md`](paik-spec/TROUBLESHOOTING.md) — common `paik_validate.py`
  errors with the broken snippet and the exact message each one produces.

## Examples

- [`examples/minimal-planning-project/`](examples/minimal-planning-project/) — Northwind Loyalty:
  the smallest valid PAIK project, still in planning, `components: []` and `environments: []`.
- [`examples/simple-project/`](examples/simple-project/) — TaskFlow Lite: the minimal *built*
  instance, one team, one repo/API, two environments — `project.md` + `component.md` +
  `environments/*.md`.
- [`examples/cross-functional-product/`](examples/cross-functional-product/) — Solstice Rewards:
  the same single-service shape read from a product owner/designer angle — `figma`, `analytics`,
  `roadmap` links alongside the usual engineering ones.
- [`examples/complex-project/`](examples/complex-project/) — Nimbus Commerce: the multi-service
  instance, 3 services, 5 owning teams, 4 environments across 2 regions.
- [`examples/mixed-components-project/`](examples/mixed-components-project/) — DataForge
  Analytics: all four `component_type` values in one project — `service`, `library`
  (`environments: []`), `job` (scheduled), and `other` (a no-code tool with no repository).
- [`examples/monorepo-project/`](examples/monorepo-project/) — Vertex Platform: three components
  sharing one repository URL, disambiguated by `purpose` — a component is not a repository.
- [`examples/external-dependencies-project/`](examples/external-dependencies-project/) — Aurora
  Logistics: 5 services, 6 owning teams, 3 environments, and 2 third-party dependencies
  (payments, mapping) expressed as `links[].kind: external-service` entries on the components
  that call them.
- [`examples/operations-ready-project/`](examples/operations-ready-project/) — Helios Payments:
  a complete per-component operational map (health, deploy pipeline, dashboard, runbooks,
  on-call, logs, SLO) on one shared production environment.
- [`examples/okf-compatible-project/`](examples/okf-compatible-project/) — Beacon Tasks: a
  file-by-file walkthrough of why every PAIK document is also a conformant OKF v0.1 concept,
  and where PAIK's own `id` diverges from OKF's file-path-based concept identity.

## Tooling

- [`mcp/`](mcp/README.md) — sample MCP server configs that give an AI agent live access to the
  systems a `paik/` folder's `links[]` reference (Jira/Confluence, GitHub/GitLab, databases, API
  specs), wired to the example projects above.
- [`skills/`](skills/README.md) — sample Agent Skills that operate on a `paik/` folder:
  scaffolding, ad-hoc natural-language maintenance (`paik-maintain`), syncing status from the
  live systems, health-checking environments, and generating an onboarding brief.
