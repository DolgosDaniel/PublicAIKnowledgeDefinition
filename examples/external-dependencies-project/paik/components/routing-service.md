---
paik_version: "2.1"
doc_type: component
id: aurora-routing-service
name: Routing Service
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/routing.md
visibility: internal
type: service
repository_ref: ../systems/source-repos/routing-service.md
provides_api_refs:
  - ../systems/api-specs/routing.md
consumes_api_refs: []
environment_refs:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod.md
configuration_ref: ../configuration/routing-service.md
depends_on: []
external_dependency_refs:
  - ../external-services/mapbox.md
ticket_scopes:
  - type: jira-component
    key: routing-service
---

# Routing Service

Route optimization and dispatch: given a set of pickups/dropoffs, returns an optimized route.
Stateless — calls Mapbox for the underlying geocoding/routing computation.

- Type: `service`
- Repository: [aurora-logistics/routing-service](../systems/source-repos/routing-service.md)
- Provides API: [Routing API](../systems/api-specs/routing.md)
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod](../environments/prod.md)
- Configuration: [routing-service](../configuration/routing-service.md)
- Depends on: none (internal)
- External dependencies: [Mapbox](../external-services/mapbox.md) (route optimization/geocoding)
- Owner: [Routing team](../teams/routing.md)
