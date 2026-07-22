---
paik: "0.4"
type: paik-component
id: frontend
title: Frontend
lifecycle: active
owner:
  name: Frontend team
  ref: https://nimbus-commerce.example/directory/teams/frontend
component_type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/nimbus-commerce/frontend
    id: nimbus-commerce/frontend
    purpose: trunk-based, short-lived feature branches, PR review required, feature-flagged releases
  - kind: api
    purpose: consumes
    provider: swaggerhub
    id: nimbus-commerce/orders-api
    url: https://api.swaggerhub.com/apis/nimbus-commerce/orders-api/3.4.0
  - kind: api
    purpose: consumes
    provider: swaggerhub
    id: nimbus-commerce/catalog-api
    url: https://api.swaggerhub.com/apis/nimbus-commerce/catalog-api/2.1.0
  - kind: jira-component
    id: frontend
    url: https://nimbus-commerce.atlassian.net/jira/software/projects/NIM/boards/4?component=frontend
  - kind: chat
    id: "#nimbus-frontend"
  - kind: pagerduty
    url: https://nimbus-commerce.pagerduty.com/schedules/frontend
environments:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod-eu.md
  - ../environments/prod-us.md
depends_on:
  - orders-api
  - catalog-api
---

# Frontend

The customer-facing web app. Has no API of its own — it consumes both `orders-api` and
`catalog-api`.

- Type: `service`
- Repository / consumed APIs / ticket scope: see `links` above
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod-eu](../environments/prod-eu.md), [prod-us](../environments/prod-us.md)
- Depends on: Orders API, Catalog API
- Owner: Frontend team
