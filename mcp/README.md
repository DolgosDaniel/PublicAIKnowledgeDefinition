# PAIK sample MCP configs

These are working `mcpServers` configuration snippets (the format used by Claude Code /
`.mcp.json`) for the systems a PAIK `paik/` folder's `links[]` entries point at. They let an AI
agent actually reach the live system a given link only references — e.g. resolve the current
ticket status behind a `jira-project` link, or check the schema behind an `api` link.

> **The MCP ecosystem moves fast.** Package names, versions, and auth flows below were accurate
> at time of writing but are not guaranteed to be current — verify the server's own repo/docs
> before wiring it into a real project. Treat these as a starting point, not a pinned dependency.
> In particular, `servers/gitlab.mcp.json` and `servers/postgres.mcp.json` currently point at
> servers published under
> [`modelcontextprotocol/servers-archived`](https://github.com/modelcontextprotocol/servers-archived) —
> archived means no further security updates, not "broken," but it does mean you should evaluate
> a maintained alternative before relying on either in a real project (see each file's `_paik`
> block).

## What's here

- `servers/` — one config per system, each mapped to the `links[]` `kind` it serves:
  - `atlassian.mcp.json` → `kind: jira-*` (Jira) and `kind: confluence`, via Atlassian's official
    remote MCP server.
  - `github.mcp.json` / `gitlab.mcp.json` → `kind: repository`.
  - `postgres.mcp.json` → the `databases` field in `environments/*.md`.
  - `fetch.mcp.json` → `kind: api` when the spec is SwaggerHub (or anything else reachable over
    plain HTTP) — there is no single ubiquitous official SwaggerHub MCP server at time of
    writing, so a generic HTTP fetch server is the honest fallback. Swap in a SwaggerHub-specific
    server if/when one becomes standard.
  - `filesystem.mcp.json` → local access to the `paik/` folder itself, for skills that need to
    read/write the documents directly.
- `examples/` — combined configs wiring exactly the servers each example project needs, with env
  var names matching the identifiers used in that project's `paik/` `links[]` entries.

## Using one of these

1. Copy the relevant server block(s) into your project's `.mcp.json` (or your Claude Code /
   Claude Desktop MCP settings).
2. Set the referenced environment variables to real credentials — never commit them. Nothing in
   this directory contains a real token; every `env` value is a placeholder name.
3. Cross-check the identifiers you pass (project key, space key, repo URL, DB name) against the
   corresponding `links[]` entry or `paik/environments/*.md` document so the two stay in sync.

## Access model

PAIK doesn't enforce anything at the MCP layer — that's the tooling's job — but each `_paik`
metadata block is a place to record the access decisions a real deployment actually needs to
make, so they're documented rather than implicit:

```jsonc
"_paik": {
  "access_mode": "read-only",
  "allowed_capabilities": ["jira.search", "confluence.read"],
  "human_approval_required": ["jira.update", "database.query"],
  "environment_scope": ["dev"]
}
```

This is advisory documentation, not something the servers below currently read or enforce.

**The direct production Postgres wiring in `examples/complex-project.mcp.json`
(`postgres-orders-prod-eu`, `postgres-orders-prod-us`, `postgres-catalog-prod-eu`,
`postgres-catalog-prod-us`) is an example of the shape, not a production-ready pattern.** A real
deployment pointing an MCP server at a production database needs, at minimum: a read-only
database role, masked/audited views instead of raw tables, a credential scoped and rotated
separately from non-prod, and query logging — not just a `DATABASE_URL` env var pointed at prod.
