---
paik_version: "2.1"
doc_type: component
id: aurora-fleet-service
name: Fleet Service
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/fleet.md
visibility: internal
type: service
repository_ref: ../systems/source-repos/fleet-service.md
provides_api_refs:
  - ../systems/api-specs/fleet.md
consumes_api_refs:
  - ../systems/api-specs/routing.md
environment_refs:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod.md
configuration_ref: ../configuration/fleet-service.md
depends_on:
  - routing-service.md
external_dependency_refs: []
ticket_scopes:
  - type: jira-component
    key: fleet-service
---

# Fleet Service

Tracks vehicles and drivers, and assigns routes computed by `routing-service` to available
drivers.

- Type: `service`
- Repository: [aurora-logistics/fleet-service](../systems/source-repos/fleet-service.md)
- Provides API: [Fleet API](../systems/api-specs/fleet.md)
- Consumes API: [Routing API](../systems/api-specs/routing.md)
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod](../environments/prod.md)
- Configuration: [fleet-service](../configuration/fleet-service.md)
- Depends on: [Routing Service](routing-service.md)
- External dependencies: none
- Owner: [Fleet team](../teams/fleet.md)
