---
name: paik-health-check
description: Call every environment's health_endpoint (and status-page link where available) listed under a paik/environments/ folder and report which environments are healthy, degraded, or unreachable. Use when the user asks "are all environments up", "run a health check", or before/after a deployment.
---

# paik-health-check

Check the operational status of every environment a PAIK project describes.

## Preconditions

- The `fetch` MCP server from `mcp/servers/fetch.mcp.json` is configured.

## Steps

1. List every file under `paik/environments/` (or the single `paik/environment.md` if the project
   hasn't split into per-environment files).
2. For each one, read `app_url` and `health_endpoint` from its frontmatter, plus any
   `links[]` entry with `kind: status-page`.
3. Call `health_endpoint` via the fetch MCP server. Classify the result:
   - 2xx and body indicates healthy → **healthy**
   - 2xx but body indicates a dependency is down, or a 5xx → **degraded**
   - timeout / connection refused / DNS failure → **unreachable**
4. If a `status-page` link is set and the environment isn't healthy, check it too — an
   already-declared incident changes how you report the finding (known issue vs. new problem).
5. Do not attempt to fix anything or restart anything — this skill only reports. If something is
   unreachable, escalate to the environment's `owner` field directly (it's inline — `name` plus
   an optional `ref` — no separate team file to resolve it against). If the environment has no
   `owner`, fall back to the owner of the component(s) deployed there.
6. Report a table: environment, status, response time if available, owner to notify if not
   healthy.
