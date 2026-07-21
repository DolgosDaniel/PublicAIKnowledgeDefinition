---
paik_version: "2.1"
doc_type: component
id: aurora-ops-console
name: Ops Console
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/frontend.md
visibility: internal
type: service
repository_ref: ../systems/source-repos/ops-console.md
provides_api_refs: []
consumes_api_refs:
  - ../systems/api-specs/orders.md
  - ../systems/api-specs/routing.md
  - ../systems/api-specs/fleet.md
environment_refs:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod.md
configuration_ref: ../configuration/shared.md
depends_on:
  - orders-service.md
  - routing-service.md
  - fleet-service.md
external_dependency_refs: []
ticket_scopes:
  - type: jira-component
    key: ops-console
---

# Ops Console

The dispatcher-facing web dashboard. Has no API of its own — it consumes Orders, Routing, and
Fleet.

- Type: `service`
- Repository: [aurora-logistics/ops-console](../systems/source-repos/ops-console.md)
- Consumes API: [Orders API](../systems/api-specs/orders.md),
  [Routing API](../systems/api-specs/routing.md), [Fleet API](../systems/api-specs/fleet.md)
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod](../environments/prod.md)
- Configuration: [shared](../configuration/shared.md)
- Depends on: [Orders Service](orders-service.md), [Routing Service](routing-service.md),
  [Fleet Service](fleet-service.md)
- External dependencies: none
- Owner: [Frontend team](../teams/frontend.md)
