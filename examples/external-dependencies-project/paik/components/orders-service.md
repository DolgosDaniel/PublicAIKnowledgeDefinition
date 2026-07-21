---
paik_version: "2.1"
doc_type: component
id: aurora-orders-service
name: Orders Service
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/orders.md
visibility: internal
type: service
repository_ref: ../systems/source-repos/orders-service.md
provides_api_refs:
  - ../systems/api-specs/orders.md
consumes_api_refs:
  - ../systems/api-specs/routing.md
  - ../systems/api-specs/notifications.md
environment_refs:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod.md
configuration_ref: ../configuration/orders-service.md
depends_on:
  - routing-service.md
  - notifications-service.md
external_dependency_refs:
  - ../external-services/stripe.md
ticket_scopes:
  - type: jira-component
    key: orders-service
---

# Orders Service

Owns delivery order intake, pricing, and payment. Calls `routing-service` for ETAs at order
creation and `notifications-service` to notify customers/drivers of order events.

- Type: `service`
- Repository: [aurora-logistics/orders-service](../systems/source-repos/orders-service.md)
- Provides API: [Orders API](../systems/api-specs/orders.md)
- Consumes API: [Routing API](../systems/api-specs/routing.md),
  [Notifications API](../systems/api-specs/notifications.md)
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod](../environments/prod.md)
- Configuration: [orders-service](../configuration/orders-service.md)
- Depends on: [Routing Service](routing-service.md), [Notifications Service](notifications-service.md)
- External dependencies: [Stripe](../external-services/stripe.md) (payment processing)
- Owner: [Orders team](../teams/orders.md)
