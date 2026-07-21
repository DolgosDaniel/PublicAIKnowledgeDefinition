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
  wired to both examples above.
- [`skills/`](skills/README.md) — sample Claude Skills that operate on a `paik/` folder:
  scaffolding, syncing status from the live systems, health-checking environments, and
  generating an onboarding brief.
