---
paik: "0.4"
type: paik-component
id: payments-api
title: Payments API
lifecycle: active
owner:
  name: Payments team
  ref: https://helios-payments.example/wiki/spaces/PAY/pages/1/Payments+Team
component_type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/helios-payments/payments-api
  - kind: api
    purpose: provides
    provider: swaggerhub
    format: openapi
    id: helios-payments/payments-api
    url: https://api.swaggerhub.com/apis/helios-payments/payments-api/2.0.0
  - kind: jira-component
    id: payments-api
    url: https://helios-payments.example/jira/software/projects/PAY?component=payments-api
  - kind: secrets
    provider: vault
    url: https://vault.helios-payments.example/ui/vault/secrets/payments-api
environments:
  - ../environments/prod.md
depends_on: []
---

# Payments API

Serves charge, refund, and payment-method requests. Depends on nothing internal - the full
per-component operational map (health, deploy pipeline, dashboard, runbook, on-call, logs,
SLO, backup/restore) lives on [`environments/prod.md`](../environments/prod.md), tagged
`component: payments-api`.

- Type: `service`
- Repository / API / ticket scope / secrets: see `links` above
- Deployed to: [prod](../environments/prod.md)
- Depends on: none
- Owner: Payments team
