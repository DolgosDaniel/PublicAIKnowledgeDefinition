---
paik_version: "2.1"
doc_type: component
id: aurora-notifications-service
name: Notifications Service
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/notifications.md
visibility: internal
type: service
repository_ref: ../systems/source-repos/notifications-service.md
provides_api_refs:
  - ../systems/api-specs/notifications.md
consumes_api_refs: []
environment_refs:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod.md
configuration_ref: ../configuration/notifications-service.md
depends_on: []
external_dependency_refs: []
ticket_scopes:
  - type: jira-component
    key: notifications-service
---

# Notifications Service

Relays order/delivery events to drivers and customers (SMS/push/email) on behalf of the other
services. Stateless relay — no external dependency modeled at the PAIK level in this example.

- Type: `service`
- Repository: [aurora-logistics/notifications-service](../systems/source-repos/notifications-service.md)
- Provides API: [Notifications API](../systems/api-specs/notifications.md)
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod](../environments/prod.md)
- Configuration: [notifications-service](../configuration/notifications-service.md)
- Depends on: none (internal)
- External dependencies: none
- Owner: [Notifications team](../teams/notifications.md)
