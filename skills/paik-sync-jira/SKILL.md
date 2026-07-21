---
name: paik-sync-jira
description: Refresh the ticket-derived parts of a paik/ project (open ticket counts, current sprint, board link validity) using the Atlassian MCP server against the project's systems/ticketing.md. Use when the user asks to "sync Jira status", "check the ticketing system is still accurate", or before an onboarding brief.
---

# paik-sync-jira

Refresh the ticket-derived status of a PAIK project using live Jira data, without turning
`systems/ticketing.md` into a content mirror.

## Preconditions

- The `atlassian` MCP server from `mcp/servers/atlassian.mcp.json` is configured and
  authenticated.
- `paik/systems/ticketing.md` exists and has `type: jira`.

## Steps

1. Read `paik/systems/ticketing.md` frontmatter: `base_url`, `project_key`, `board_url`.
2. Via the Atlassian MCP server, confirm `project_key` still resolves to a real, active Jira
   project at `base_url`. Flag it clearly if not — don't silently rewrite the identifier.
3. Optionally fetch current sprint name / open ticket count for a status summary — report this to
   the user directly, do **not** write it into `systems/ticketing.md`. That file is a pointer, not
   a cache; ticket counts go stale immediately and would violate the metadata-reference model in
   `paik-spec/SPEC.md`.
4. If `default_workflow` in the frontmatter no longer matches the board's actual workflow states,
   update that field (it's the one piece of Jira config genuinely worth caching, since it changes
   rarely and other tooling may read it).
5. Update `last_updated` only if you changed something.
6. Report: confirmed reachable, any drift found, any field updated.
