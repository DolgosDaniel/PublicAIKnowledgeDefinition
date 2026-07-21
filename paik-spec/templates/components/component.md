---
paik_version: "2.0"
doc_type: component
id: <component-slug>
name: <Component Name>
status: active
last_updated: "<YYYY-MM-DD>"
owner_ref: ../team.md
visibility: internal # public | internal | confidential
type: service # service | library | job | other
repository_ref: ../systems/source-repo.md
provides_api_refs:
  - ../systems/api-spec.md
consumes_api_refs: []
environment_refs:
  - ../environments/dev.md
  - ../environments/prod.md
configuration_ref: ../configuration.md
depends_on: []
ticket_scopes:
  - type: jira-epic
    key: <PROJ-123>
---

# <Component Name>

<One paragraph: what this component does.>

- Type: `service`
- Repository: [<Repo Name>](../systems/source-repo.md)
- Provides API: [<API Name>](../systems/api-spec.md)
- Deployed to: [dev](../environments/dev.md), [prod](../environments/prod.md)
- Configuration: [configuration.md](../configuration.md)
- Depends on: <other components, or "none">
- Owner: [<Team Name>](../team.md)
