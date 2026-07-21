---
paik_version: "2.0"
doc_type: component
id: nimbus-orders-api
name: Orders API
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/orders.md
visibility: internal
type: service
repository_ref: ../systems/source-repos/orders-api.md
provides_api_refs:
  - ../systems/api-specs/orders.md
consumes_api_refs: []
environment_refs:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod-eu.md
  - ../environments/prod-us.md
configuration_ref: ../configuration/orders-api.md
depends_on: []
ticket_scopes:
  - type: jira-component
    key: orders-api
---

# Orders API

The orders microservice: owns the Orders API contract end to end.

- Type: `service`
- Repository: [nimbus-commerce/orders-api](../systems/source-repos/orders-api.md)
- Provides API: [Orders API](../systems/api-specs/orders.md)
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod-eu](../environments/prod-eu.md), [prod-us](../environments/prod-us.md)
- Configuration: [orders-api](../configuration/orders-api.md)
- Depends on: none
- Owner: [Orders team](../teams/orders.md)
