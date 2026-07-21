# PAIK (Public AI Knowledge Definition)

A tool-agnostic, Markdown-based standard for describing a software project end-to-end —
planning, implementation, and operations — by **linking** the systems a team already uses
instead of duplicating their content. PAIK v0.3 has exactly three document kinds — `project`,
`component`, `environment` — plus one generic, typed `links[]` list that covers ticketing (Jira,
...), knowledge base (Confluence, ...), API specs (SwaggerHub, ...), source repos (GitHub/GitLab,
...), third-party/external services, and where secrets are managed. There is no separate document
type per external system, and no separate `team` document — ownership is an inline `owner: {
name, ref }` on `project.md`/`component.md`.

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
   Windows). This becomes the `paik/` folder tooling looks for by default.

3. **Pick a shape and fill in the placeholders.** A one-service project keeps `component.md` as
   is; a multi-service project converts it to `components/*.md` — compare
   [`examples/simple-project/`](examples/simple-project/) against
   [`examples/complex-project/`](examples/complex-project/) to see both shapes side by side.
   Replace every `<placeholder>` with a real value: every field is documented in
   [`paik-spec/SPEC.md`](paik-spec/SPEC.md) and enforced by the matching schema in
   [`paik-spec/schema/`](paik-spec/schema/) — except a `links[]` item, which only requires a
   `kind`. Never invent a URL or identifier — leave a clearly marked `TODO` if a value is
   genuinely unknown.

4. **Validate.** There's no packaged `paik validate` CLI yet (tracked as future work in
   `SPEC.md` section 9) — until then, check each file's YAML frontmatter against its schema in
   `paik-spec/schema/` with any JSON Schema (2020-12) validator for your language of choice
   (e.g. Python's `jsonschema` + `pyyaml`, or Node's `ajv`). That's exactly how every document
   in `examples/` is checked during development.

5. **(Optional) Wire up live access for an AI agent.** Copy the relevant server block(s) from
   [`mcp/`](mcp/README.md) into your project's `.mcp.json` so an agent can reach the live
   systems your `paik/` folder's `links[]` point at (Jira/Confluence, GitHub/GitLab, databases,
   API specs), and drop any of the [`skills/`](skills/README.md) into `.claude/skills/` for
   ready-made workflows (bootstrap, onboarding brief, health-check, sync).

6. **Commit `paik/` to your repo.** Every document only points at *where* things live — never a
   secret — see `SPEC.md` section 6. Whether a given `paik/` folder is safe to make public is a
   repo-level call you make the same way you would for any other doc in the repo; PAIK doesn't
   impose a per-document classification for this.

## Start here

- [`paik-spec/SPEC.md`](paik-spec/SPEC.md) — the normative standard: directory layout, common
  frontmatter, the `links` convention, cross-referencing, and the three document kinds.
- [`paik-spec/templates/`](paik-spec/templates/) — blank files to copy into a new project as its
  `paik/` folder.
- [`paik-spec/schema/`](paik-spec/schema/) — JSON Schema for every document kind's frontmatter.

## Examples

- [`examples/simple-project/`](examples/simple-project/) — TaskFlow Lite: the minimal instance,
  one team, one repo/API, two environments — `project.md` + `component.md` + `environments/*.md`.
- [`examples/complex-project/`](examples/complex-project/) — Nimbus Commerce: the multi-service
  instance, 3 services, 5 owning teams, 4 environments across 2 regions.
- [`examples/external-dependencies-project/`](examples/external-dependencies-project/) — Aurora
  Logistics: 5 services, 6 owning teams, 3 environments, and 2 third-party dependencies
  (payments, mapping) expressed as `links[].kind: external-service` entries on the components
  that call them.

## Tooling

- [`mcp/`](mcp/README.md) — sample MCP server configs that give an AI agent live access to the
  systems a `paik/` folder's `links[]` reference (Jira/Confluence, GitHub/GitLab, databases, API
  specs), wired to the example projects above.
- [`skills/`](skills/README.md) — sample Claude Skills that operate on a `paik/` folder:
  scaffolding, syncing status from the live systems, health-checking environments, and
  generating an onboarding brief.
