# PAIK (Public AI Knowledge Definition)

A tool-agnostic, Markdown-based standard for describing a software project end-to-end —
planning, implementation, and operations — by **linking** the systems a team already uses
instead of duplicating their content: ticketing (Jira, ...), knowledge base (Confluence, ...),
API specs (SwaggerHub, ...), source repos (GitHub/GitLab, ...), components/services, owning
teams, environments (running app / health endpoints / databases), and configuration management.

A PAIK document is never a copy of a ticket, a wiki page, or a database password — it's a small,
structured pointer: what system, which identifier, whose responsibility, how to reach it. The
systems stay the source of truth; PAIK stays the map. Every document also declares its own
`visibility` (`public`/`internal`/`confidential`), because the absence of a password doesn't by
itself make a `paik/` folder safe to publish — see `paik-spec/SPEC.md` section 4.

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

3. **Pick a shape and fill in the placeholders.** A one-service project keeps the singular files
   as they are (`component.md`, `team.md`, `systems/api-spec.md`, ...); a multi-service project
   converts them to directories (`components/*.md`, `teams/*.md`, `systems/api-specs/*.md`,
   ...) — compare [`examples/simple-project/`](examples/simple-project/) against
   [`examples/complex-project/`](examples/complex-project/) to see both shapes side by side.
   Replace every `<placeholder>` with a real value: every field is documented in
   [`paik-spec/SPEC.md`](paik-spec/SPEC.md) and enforced by the matching schema in
   [`paik-spec/schema/`](paik-spec/schema/). Never invent a URL or identifier — leave a clearly
   marked `TODO` if a value is genuinely unknown. Delete whatever doesn't apply (e.g. skip
   `external-service.md` entirely if your project has no third-party dependencies).

4. **Validate.** There's no packaged `paik validate` CLI yet (tracked as future work in
   `SPEC.md` section 7) — until then, check each file's YAML frontmatter against its schema in
   `paik-spec/schema/` with any JSON Schema (2020-12) validator for your language of choice
   (e.g. Python's `jsonschema` + `pyyaml`, or Node's `ajv`). That's exactly how every document
   in `examples/` is checked during development.

5. **(Optional) Wire up live access for an AI agent.** Copy the relevant server block(s) from
   [`mcp/`](mcp/README.md) into your project's `.mcp.json` so an agent can reach the live
   systems your `paik/` folder references (Jira/Confluence, GitHub/GitLab, databases, API
   specs), and drop any of the [`skills/`](skills/README.md) into `.claude/skills/` for
   ready-made workflows (bootstrap, onboarding brief, health-check, sync).

6. **Commit `paik/` to your repo.** Every document only points at *where* things live — never a
   secret — and every document now declares its own `visibility`
   (`public`/`internal`/`confidential`), so you decide per document what's safe to share; see
   `SPEC.md` section 4 before treating the whole folder as public by default.

## Start here

- [`paik-spec/SPEC.md`](paik-spec/SPEC.md) — the normative standard: directory layout, common
  frontmatter, document types, cross-referencing and secrets conventions.
- [`paik-spec/templates/`](paik-spec/templates/) — blank files to copy into a new project as its
  `paik/` folder.
- [`paik-spec/schema/`](paik-spec/schema/) — JSON Schema for every document type's frontmatter.

## Examples

- [`examples/simple-project/`](examples/simple-project/) — TaskFlow Lite: the minimal instance,
  one team/repo/API/two environments.
- [`examples/complex-project/`](examples/complex-project/) — Nimbus Commerce: the multi-service
  instance, 3 services, 5 teams, 4 environments across 2 regions.
- [`examples/external-dependencies-project/`](examples/external-dependencies-project/) — Aurora
  Logistics: 5 services, 6 teams, 3 environments, and 2 `external-service` documents for
  third-party dependencies (payments, mapping) the project calls but doesn't operate.

## Tooling

- [`mcp/`](mcp/README.md) — sample MCP server configs that give an AI agent live access to the
  systems a `paik/` folder references (Jira/Confluence, GitHub/GitLab, databases, API specs),
  wired to the simple- and complex-project examples above.
- [`skills/`](skills/README.md) — sample Claude Skills that operate on a `paik/` folder:
  scaffolding, syncing status from the live systems, health-checking environments, and
  generating an onboarding brief.
