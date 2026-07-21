---
paik_version: "2.0"
doc_type: component
id: nimbus-catalog-api
name: Catalog API
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/catalog.md
visibility: internal
type: service
repository_ref: ../systems/source-repos/catalog-api.md
provides_api_refs:
  - ../systems/api-specs/catalog.md
consumes_api_refs: []
environment_refs:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod-eu.md
  - ../environments/prod-us.md
configuration_ref: ../configuration/catalog-api.md
depends_on: []
ticket_scopes:
  - type: jira-component
    key: catalog-api
---

# Catalog API

The catalog microservice: owns the Catalog API contract end to end.

- Type: `service`
- Repository: [nimbus-commerce/catalog-api](../systems/source-repos/catalog-api.md)
- Provides API: [Catalog API](../systems/api-specs/catalog.md)
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod-eu](../environments/prod-eu.md), [prod-us](../environments/prod-us.md)
- Configuration: [catalog-api](../configuration/catalog-api.md)
- Depends on: none
- Owner: [Catalog team](../teams/catalog.md)
