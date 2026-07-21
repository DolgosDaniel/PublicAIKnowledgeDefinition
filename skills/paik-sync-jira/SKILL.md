---
name: paik-sync-jira
description: Refresh the ticket-derived parts of a paik/ project (open ticket counts, current sprint, board link validity) using the Atlassian MCP server against every jira-* links[] entry across project.md and components/*.md. Use when the user asks to "sync Jira status", "check the ticketing links are still accurate", or before an onboarding brief.
---

# paik-sync-jira

Refresh the ticket-derived status of a PAIK project using live Jira data, without turning any
`links[]` entry into a content mirror.

## Preconditions

- The `atlassian` MCP server from `mcp/servers/atlassian.mcp.json` is configured and
  authenticated.
- At least one `links[]` entry with a `kind` starting `jira-` (`jira-project`, `jira-epic`,
  `jira-component`, ...) exists somewhere under `paik/` — typically one `jira-project` on
  `project.md` plus one `jira-component`/`jira-epic` per `component*.md`.

## Steps

1. Find every `jira-*` link across `paik/project.md` and `paik/component*.md`. Read each one's
   `id` and `url`.
2. Via the Atlassian MCP server, confirm each `id` still resolves to a real, active Jira
   project/epic/component at that `url`. Flag it clearly if not — don't silently rewrite the
   identifier.
3. Optionally fetch current sprint name / open ticket count per link for a status summary —
   report this to the user directly, do **not** write it into the link. A `links[]` entry is a
   pointer, not a cache; ticket counts go stale immediately and would violate the
   metadata-reference model in `paik-spec/SPEC.md`.
4. Report: which links were confirmed reachable, any drift found (moved/renamed/archived), and
   anything you'd recommend updating (which the user should confirm before you edit the file).
