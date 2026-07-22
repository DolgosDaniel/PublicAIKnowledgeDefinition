---
paik: "0.4"
type: paik-component
id: fleet-service
title: Fleet Service
lifecycle: active
owner:
  name: Fleet team
  ref: https://aurora-logistics.example/directory/teams/fleet
component_type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/aurora-logistics/fleet-service
    id: aurora-logistics/fleet-service
    purpose: trunk-based, short-lived feature branches, PR review required
  - kind: api
    purpose: provides
    provider: swaggerhub
    format: openapi
    id: aurora-logistics/fleet-service
    url: https://api.swaggerhub.com/apis/aurora-logistics/fleet-service/1.1.0
    served_by_env:
      dev: 1.1.0
      staging: 1.1.0
      prod: 1.1.0
  - kind: api
    purpose: consumes
    provider: swaggerhub
    protocol: grpc
    id: aurora-logistics/routing-service
    url: https://api.swaggerhub.com/apis/aurora-logistics/routing-service/2.0.0
  - kind: jira-component
    id: fleet-service
    url: https://aurora-logistics.atlassian.net/jira/software/projects/AUR/boards/1?component=fleet-service
  - kind: secrets
    provider: vault
    url: https://vault.aurora-logistics.example/ui/vault/secrets/aurora
    purpose: "aurora/<environment>/fleet-service/<key>"
  - kind: chat
    id: "#aurora-fleet"
  - kind: pagerduty
    url: https://aurora-logistics.pagerduty.com/schedules/fleet
environments:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod.md
depends_on:
  - routing-service
---

# Fleet Service

Tracks vehicles and drivers, and assigns routes computed by `routing-service` to available
drivers.

- Type: `service`
- Repository / provided + consumed APIs / ticket scope / secrets: see `links` above
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod](../environments/prod.md)
- Depends on: Routing Service
- External dependencies: none
- Owner: Fleet team
