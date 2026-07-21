# PAIK sample MCP configs

These are working `mcpServers` configuration snippets (the format used by Claude Code /
`.mcp.json`) for the systems a PAIK `paik/` folder points at. They let an AI agent actually reach
the live system a given document only references — e.g. resolve the current ticket status behind
`systems/ticketing.md`, or check the schema behind `systems/api-spec.md`.

> **The MCP ecosystem moves fast.** Package names, versions, and auth flows below were accurate
> at time of writing but are not guaranteed to be current — verify the server's own repo/docs
> before wiring it into a real project. Treat these as a starting point, not a pinned dependency.

## What's here

- `servers/` — one config per system, each mapped to the PAIK doc type it serves:
  - `atlassian.mcp.json` → `systems/ticketing.md` (Jira) and `systems/knowledge-base.md`
    (Confluence), via Atlassian's official remote MCP server.
  - `github.mcp.json` / `gitlab.mcp.json` → `systems/source-repo.md`.
  - `postgres.mcp.json` → the `databases` field in `environments/*.md`.
  - `fetch.mcp.json` → `systems/api-spec.md` when the spec is SwaggerHub (or anything else
    reachable over plain HTTP) — there is no single ubiquitous official SwaggerHub MCP server at
    time of writing, so a generic HTTP fetch server is the honest fallback. Swap in a
    SwaggerHub-specific server if/when one becomes standard.
  - `filesystem.mcp.json` → local access to the `paik/` folder itself, for skills that need to
    read/write the documents directly.
- `examples/` — combined configs wiring exactly the servers each example project needs, with env
  var names matching the identifiers used in that project's `paik/systems/*.md` files.

## Using one of these

1. Copy the relevant server block(s) into your project's `.mcp.json` (or your Claude Code /
   Claude Desktop MCP settings).
2. Set the referenced environment variables to real credentials — never commit them. Nothing in
   this directory contains a real token; every `env` value is a placeholder name.
3. Cross-check the identifiers you pass (project key, space key, repo URL, DB name) against the
   corresponding `paik/systems/*.md` or `paik/environments/*.md` document so the two stay in sync.
