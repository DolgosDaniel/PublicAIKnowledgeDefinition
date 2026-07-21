---
paik: "0.3"
kind: component
id: orders-service
name: Orders Service
lifecycle: active
owner:
  name: Orders team
  ref: https://aurora-logistics.example/directory/teams/orders
type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/aurora-logistics/orders-service
    id: aurora-logistics/orders-service
    purpose: trunk-based, short-lived feature branches, PR review required
  - kind: api
    purpose: provides
    provider: openapi-file
    id: aurora-logistics/orders-service
    url: https://api.swaggerhub.com/apis/aurora-logistics/orders-service/1.4.0
    served_by_env:
      dev: 1.5.0-rc1
      staging: 1.4.0
      prod: 1.4.0
  - kind: api
    purpose: consumes
    provider: grpc
    id: aurora-logistics/routing-service
    url: https://api.swaggerhub.com/apis/aurora-logistics/routing-service/2.0.0
  - kind: api
    purpose: consumes
    provider: asyncapi
    id: aurora-logistics/notifications-service
    url: https://api.swaggerhub.com/apis/aurora-logistics/notifications-service/1.0.0
  - kind: jira-component
    id: orders-service
    url: https://aurora-logistics.atlassian.net/jira/software/projects/AUR/boards/1?component=orders-service
  - kind: secrets
    provider: vault
    url: https://vault.aurora-logistics.example/ui/vault/secrets/aurora
    purpose: "aurora/<environment>/orders-service/<key>"
  - kind: external-service
    provider: stripe
    vendor: Stripe, Inc.
    url: https://stripe.com
    docs_url: https://docs.stripe.com/api
    status_page: https://status.stripe.com
    contract_ref: https://aurora-logistics.atlassian.net/wiki/spaces/AUR/overview
    data_shared: payment card tokens and delivery-fee charge amounts; card numbers never touch our systems (Stripe-hosted checkout)
    secret_ref: "Vault path aurora/<environment>/orders-service/stripe-key, never the key itself"
  - kind: chat
    id: "#aurora-orders"
  - kind: pagerduty
    url: https://aurora-logistics.pagerduty.com/schedules/orders
environments:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod.md
depends_on:
  - routing-service
  - notifications-service
---

# Orders Service

Owns delivery order intake, pricing, and payment. Calls `routing-service` for ETAs at order
creation and `notifications-service` to notify customers/drivers of order events; calls Stripe
directly for payment processing.

- Type: `service`
- Repository / provided + consumed APIs / ticket scope / secrets / Stripe: see `links` above
  (currently published `1.4.0`; `dev` runs ahead on `1.5.0-rc1`)
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod](../environments/prod.md)
- Depends on: Routing Service, Notifications Service
- External dependencies: Stripe (payment processing) — see `links` above
- Owner: Orders team
