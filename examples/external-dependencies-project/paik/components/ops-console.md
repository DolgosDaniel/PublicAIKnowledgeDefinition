---
paik: "0.4"
type: paik-component
id: ops-console
title: Ops Console
lifecycle: active
owner:
  name: Frontend team
  ref: https://aurora-logistics.example/directory/teams/frontend
component_type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/aurora-logistics/ops-console
    id: aurora-logistics/ops-console
    purpose: trunk-based, short-lived feature branches, PR review required, feature-flagged releases
  - kind: api
    purpose: consumes
    id: aurora-logistics/orders-service
    url: https://api.swaggerhub.com/apis/aurora-logistics/orders-service/1.4.0
  - kind: api
    purpose: consumes
    provider: swaggerhub
    protocol: grpc
    id: aurora-logistics/routing-service
    url: https://api.swaggerhub.com/apis/aurora-logistics/routing-service/2.0.0
  - kind: api
    purpose: consumes
    id: aurora-logistics/fleet-service
    url: https://api.swaggerhub.com/apis/aurora-logistics/fleet-service/1.1.0
  - kind: jira-component
    id: ops-console
    url: https://aurora-logistics.atlassian.net/jira/software/projects/AUR/boards/1?component=ops-console
  - kind: chat
    id: "#aurora-frontend"
  - kind: pagerduty
    url: https://aurora-logistics.pagerduty.com/schedules/frontend
environments:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod.md
depends_on:
  - orders-service
  - routing-service
  - fleet-service
---

# Ops Console

The dispatcher-facing web dashboard. Has no API of its own — it consumes Orders, Routing, and
Fleet.

- Type: `service`
- Repository / consumed APIs / ticket scope: see `links` above
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod](../environments/prod.md)
- Depends on: Orders Service, Routing Service, Fleet Service
- External dependencies: none (calls Stripe/Mapbox indirectly through orders-service/routing-service)
- Owner: Frontend team
