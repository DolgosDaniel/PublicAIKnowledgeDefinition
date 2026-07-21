---
paik_version: "2.0"
doc_type: component
id: nimbus-frontend
name: Frontend
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/frontend.md
visibility: internal
type: service
repository_ref: ../systems/source-repos/frontend.md
provides_api_refs: []
consumes_api_refs:
  - ../systems/api-specs/orders.md
  - ../systems/api-specs/catalog.md
environment_refs:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod-eu.md
  - ../environments/prod-us.md
configuration_ref: ../configuration/shared.md
depends_on:
  - orders-api.md
  - catalog-api.md
ticket_scopes:
  - type: jira-component
    key: frontend
---

# Frontend

The customer-facing web app. Has no API spec of its own — it consumes both `orders-api` and
`catalog-api`.

- Type: `service`
- Repository: [nimbus-commerce/frontend](../systems/source-repos/frontend.md)
- Consumes API: [Orders API](../systems/api-specs/orders.md),
  [Catalog API](../systems/api-specs/catalog.md)
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod-eu](../environments/prod-eu.md), [prod-us](../environments/prod-us.md)
- Configuration: [shared](../configuration/shared.md)
- Depends on: [Orders API component](orders-api.md), [Catalog API component](catalog-api.md)
- Owner: [Frontend team](../teams/frontend.md)
