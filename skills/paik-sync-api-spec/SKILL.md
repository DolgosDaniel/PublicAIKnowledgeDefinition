---
name: paik-sync-api-spec
description: Pull the current published version and per-environment served version of an API into a paik/ component's api links[] entry (SwaggerHub or generic OpenAPI URL), using the fetch MCP server. Use when the user asks to "sync the API spec version", "check what's deployed where", or after a service release.
---

# paik-sync-api-spec

Refresh the version metadata on a PAIK `kind: api` link — never the spec body itself.

## Preconditions

- The `fetch` MCP server from `mcp/servers/fetch.mcp.json` is configured (or a dedicated
  SwaggerHub MCP server if the project has one — check `mcp/README.md` for the current
  recommendation).
- The target component has a `links[]` entry with `kind: api` and `purpose: provides` (the
  service's own contract, as opposed to `purpose: consumes` entries for APIs it merely calls).

## Steps

1. Find the `kind: api, purpose: provides` link on the target `component*.md`. Read its `url`
   and (if present) `served_by_env`.
2. Fetch `url` and confirm it resolves and its declared version matches what the link's `url`/`id`
   implies. If the published version has moved, update `url` to the new version — this is the one
   thing worth syncing, since "what's the current contract version" is exactly what a caller
   needs to know quickly.
3. For each environment listed under `served_by_env`, if you have a way to check what's actually
   deployed there (e.g. hitting `<app_url>/openapi.json` from the matching `environments/*.md`),
   update that entry. If you don't have that access, leave it and say so rather than guessing.
4. Never inline the OpenAPI/AsyncAPI document itself into the `.md` file — link to it via `url`,
   per the metadata-reference model.
5. Report: version drift found (if any), which `served_by_env` entries were confirmed vs. left
   unchecked.
