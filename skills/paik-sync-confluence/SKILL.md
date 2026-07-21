---
name: paik-sync-confluence
description: Verify that a paik/ project's systems/knowledge-base.md still points at a real, reachable Confluence (or other knowledge base) space and root page, using the Atlassian MCP server. Use when the user asks to "check the knowledge base links", "sync Confluence", or as part of a periodic PAIK health pass.
---

# paik-sync-confluence

Verify (not mirror) the knowledge-base pointer in a PAIK project.

## Preconditions

- The `atlassian` MCP server from `mcp/servers/atlassian.mcp.json` is configured.
- `paik/systems/knowledge-base.md` exists.

## Steps

1. Read `base_url`, `space_key`, and `root_page_url` from the frontmatter.
2. Via the MCP server, confirm the space key resolves and the root page is reachable and not
   archived/deleted. If the tool `type` isn't `confluence`, skip the MCP call and just note that
   a manual check is needed (this skill is Confluence-specific; other knowledge bases need their
   own MCP integration).
3. Do not fetch or store the page's actual content — PAIK documents link to knowledge, they don't
   duplicate it (see `paik-spec/SPEC.md` section 1).
4. If the space or page has moved, update `base_url`/`root_page_url` and bump `last_updated`.
   If it's gone entirely, flag it to the user rather than guessing a replacement.
5. Report: link status (OK / moved / broken), and anything you updated.
