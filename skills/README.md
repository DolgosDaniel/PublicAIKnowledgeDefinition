# PAIK sample skills

Real `SKILL.md` files (the format Claude Code/Claude Agent SDK skills use: YAML frontmatter with
`name` + `description`, Markdown body with instructions) that operate on a `paik/` folder. Drop
any of these directories into `.claude/skills/` in a project that has adopted PAIK.

| Skill | What it does |
|---|---|
| [`paik-bootstrap`](paik-bootstrap/SKILL.md) | Scaffold a new `paik/` folder from `paik-spec/templates`. |
| [`paik-sync-jira`](paik-sync-jira/SKILL.md) | Refresh `jira-*` `links[]` entries using the Atlassian MCP server. |
| [`paik-sync-confluence`](paik-sync-confluence/SKILL.md) | Verify/refresh `confluence` `links[]` entries. |
| [`paik-sync-api-spec`](paik-sync-api-spec/SKILL.md) | Pull current version/metadata for an `api` `links[]` entry. |
| [`paik-health-check`](paik-health-check/SKILL.md) | Call each environment's `health_endpoint` and report status. |
| [`paik-onboarding`](paik-onboarding/SKILL.md) | Read a whole `paik/` folder and produce an onboarding brief. |

Each skill assumes the relevant MCP server from [`../mcp/`](../mcp/README.md) is configured, and
reads/writes only the `paik/` folder it's pointed at — never the external system's content, per
the PAIK metadata-reference model in [`../paik-spec/SPEC.md`](../paik-spec/SPEC.md).
