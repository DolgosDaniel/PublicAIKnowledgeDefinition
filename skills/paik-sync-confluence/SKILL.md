---
name: paik-sync-confluence
description: Verify that a paik/ project's confluence links[] entries still point at a real, reachable Confluence (or other knowledge base) space/page, using the Atlassian MCP server. Use when the user asks to "check the knowledge base links", "sync Confluence", or as part of a periodic PAIK health pass.
---

# paik-sync-confluence

Verify (not mirror) the knowledge-base pointers in a PAIK project.

## Preconditions

- The `atlassian` MCP server from `mcp/servers/atlassian.mcp.json` is configured.
- At least one `links[]` entry with `kind: confluence` exists (typically on `project.md`; other
  wikis use their own `kind`, e.g. `notion`, `sharepoint`).

## Steps

1. Find every `kind: confluence` link across `paik/project.md` and `paik/component*.md` — the
   `kind` itself is the filter, since each wiki product gets its own `kind` value (`confluence`,
   `notion`, `sharepoint`, ...) rather than a shared `kind: knowledge-base` plus a `provider`
   field. Read each link's `url` and `purpose` (disambiguates when more than one exists, e.g.
   `project-home` vs `architecture`).
2. Via the MCP server, confirm each URL resolves and the page isn't archived/deleted. This skill
   only handles `kind: confluence` links; a project's `notion`/`sharepoint`/other wiki links need
   their own MCP integration and are out of scope here.
3. Do not fetch or store the page's actual content — PAIK links point to knowledge, they don't
   duplicate it (see `paik-spec/SPEC.md` section 4).
4. If a space or page has moved, propose the corrected `url` to the user rather than editing
   silently. If it's gone entirely, flag it rather than guessing a replacement.
5. Report: link status (OK / moved / broken) per entry, and anything you'd update.
