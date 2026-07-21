---
paik: "0.3"
kind: component
id: ledger-worker
name: Ledger Worker
lifecycle: active
owner:
  name: Payments team
  ref: https://helios-payments.example/wiki/spaces/PAY/pages/1/Payments+Team
type: job
links:
  - kind: repository
    provider: github
    url: https://github.com/helios-payments/ledger-worker
  - kind: jira-component
    id: ledger-worker
    url: https://helios-payments.example/jira/software/projects/PAY?component=ledger-worker
  - kind: secrets
    provider: vault
    url: https://vault.helios-payments.example/ui/vault/secrets/ledger-worker
environments:
  - ../environments/prod.md
depends_on:
  - payments-api
---

# Ledger Worker

Consumes settlement events from `payments-api` off a queue and posts them to the double-entry
ledger. Its full per-component operational map also lives on
[`environments/prod.md`](../environments/prod.md), tagged `component: ledger-worker`.

- Type: `job`
- Repository / ticket scope / secrets: see `links` above
- Deployed to: [prod](../environments/prod.md)
- Depends on: Payments API (consumes its settlement events)
- Owner: Payments team
