---
paik: "0.3"
kind: component
id: notifications-service
name: Notifications Service
lifecycle: active
owner:
  name: Notifications team
  ref: https://aurora-logistics.example/directory/teams/notifications
type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/aurora-logistics/notifications-service
    id: aurora-logistics/notifications-service
    purpose: trunk-based, short-lived feature branches, PR review required
  - kind: api
    purpose: provides
    provider: asyncapi
    id: aurora-logistics/notifications-service
    url: https://api.swaggerhub.com/apis/aurora-logistics/notifications-service/1.0.0
    served_by_env:
      dev: 1.0.0
      staging: 1.0.0
      prod: 1.0.0
  - kind: jira-component
    id: notifications-service
    url: https://aurora-logistics.atlassian.net/jira/software/projects/AUR/boards/1?component=notifications-service
  - kind: secrets
    provider: vault
    url: https://vault.aurora-logistics.example/ui/vault/secrets/aurora
    purpose: "aurora/<environment>/notifications-service/<key>"
  - kind: chat
    id: "#aurora-notifications"
  - kind: pagerduty
    url: https://aurora-logistics.pagerduty.com/schedules/notifications
environments:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod.md
depends_on: []
---

# Notifications Service

Relays order/delivery events to drivers and customers (SMS/push/email) on behalf of the other
services. Stateless relay — no external dependency modeled in this example.

- Type: `service`
- Repository / API / ticket scope / secrets: see `links` above
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod](../environments/prod.md)
- Depends on: none (internal)
- External dependencies: none
- Owner: Notifications team
