---
paik_version: "2.0"
doc_type: component
id: taskflow-lite
name: TaskFlow Lite
status: active
last_updated: "2026-07-21"
owner_ref: team.md
visibility: internal
type: service
repository_ref: systems/source-repo.md
provides_api_refs:
  - systems/api-spec.md
consumes_api_refs: []
environment_refs:
  - environments/dev.md
  - environments/prod.md
configuration_ref: configuration.md
depends_on: []
ticket_scopes:
  - type: jira-project
    key: TFL
---

# TaskFlow Lite

The single service that makes up this project: a to-do list web app plus its API.

- Type: `service`
- Repository: [taskflow-inc/taskflow-lite](systems/source-repo.md)
- Provides API: [TaskFlow Lite API](systems/api-spec.md)
- Deployed to: [dev](environments/dev.md), [prod](environments/prod.md)
- Configuration: [configuration.md](configuration.md)
- Depends on: none — single-service project
- Owner: [TaskFlow Lite team](team.md)
