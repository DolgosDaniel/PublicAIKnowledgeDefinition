---
paik: "0.4"
type: paik-component
id: orders-api
title: Orders API
lifecycle: active
owner:
  name: Orders team
  ref: https://nimbus-commerce.example/directory/teams/orders
component_type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/nimbus-commerce/orders-api
    id: nimbus-commerce/orders-api
    purpose: trunk-based, short-lived feature branches, PR review required
  - kind: api
    purpose: provides
    provider: swaggerhub
    id: nimbus-commerce/orders-api
    url: https://api.swaggerhub.com/apis/nimbus-commerce/orders-api/3.4.0
    served_by_env:
      dev: 3.5.0-rc2
      staging: 3.5.0-rc2
      prod-eu: 3.4.0
      prod-us: 3.4.0
  - kind: jira-component
    id: orders-api
    url: https://nimbus-commerce.atlassian.net/jira/software/projects/NIM/boards/4?component=orders-api
  - kind: secrets
    provider: vault
    url: https://vault.nimbus.example/ui/vault/secrets/nimbus
    purpose: "nimbus/<environment>/orders-api/<key>"
  - kind: chat
    id: "#nimbus-orders"
  - kind: pagerduty
    url: https://nimbus-commerce.pagerduty.com/schedules/orders
environments:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod-eu.md
  - ../environments/prod-us.md
depends_on: []
---

# Orders API

The orders microservice: owns the Orders API contract end to end.

- Type: `service`
- Repository / API / ticket scope / secrets: see `links` above (currently published `3.4.0`;
  `dev`/`staging` run ahead on `3.5.0-rc2`, both `prod-*` regions pinned to `3.4.0`)
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod-eu](../environments/prod-eu.md), [prod-us](../environments/prod-us.md)
- Depends on: none
- Owner: Orders team
