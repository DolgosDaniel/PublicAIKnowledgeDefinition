---
paik_version: "1.0"
doc_type: project
id: <project-slug>
name: <Project Name>
status: planning # planning | active | maintenance | sunset
last_updated: <YYYY-MM-DD>
owner_ref: participants.md#<owner-anchor>
description: >
  One paragraph: what this project is, who it's for, and what problem it solves.
systems:
  ticketing: [systems/ticketing.md]
  knowledge_base: [systems/knowledge-base.md]
  api_specs: [systems/api-spec.md]
  source_repos: [systems/source-repo.md]
participants_ref: participants.md
environments_ref: environments/
configuration_ref: configuration.md
---

# <Project Name>

<One paragraph: what this project is, who it's for, and what problem it solves.>

## Planning
- Ticketing: [<Ticketing system name>](systems/ticketing.md)
- Knowledge base: [<Knowledge base name>](systems/knowledge-base.md)

## Implementation
- API spec: [<API name>](systems/api-spec.md)
- Source repo: [<Repo name>](systems/source-repo.md)

## People
- See [participants.md](participants.md)

## Operations
- Environments: see [environments/](environments/)
- Configuration management: see [configuration.md](configuration.md)
