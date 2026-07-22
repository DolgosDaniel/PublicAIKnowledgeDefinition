---
paik: "0.4"
type: paik-project
id: helios-payments
title: Helios Payments
lifecycle: active
owner:
  name: Payments team
  ref: https://helios-payments.example/wiki/spaces/PAY/pages/1/Payments+Team
description: >
  A payments platform: a request-serving API and a settlement worker. Used here to show the
  full operational map two components can carry on one shared production environment - health
  checks, deploy pipelines, dashboards, runbooks, on-call, a status page, logs, and SLO/backup
  docs - entirely as links[] entries, with no dedicated "operations" document kind. Dev/staging
  environments exist internally but are omitted here to keep the example focused on production.
links:
  - kind: jira-project
    id: PAY
    url: https://helios-payments.example/jira/software/projects/PAY
  - kind: confluence
    purpose: project-home
    url: https://helios-payments.example/wiki/spaces/PAY/overview
components:
  - components/payments-api.md
  - components/ledger-worker.md
environments:
  - environments/prod.md
---

# Helios Payments

A payments platform: [Payments API](components/payments-api.md) serves card-present and
card-not-present charge requests; [Ledger Worker](components/ledger-worker.md) settles them
into the double-entry ledger asynchronously. Both run in the one production environment modeled
here — see [`environments/prod.md`](environments/prod.md) for the full per-component
operational map.

## Operations
- Environment: [prod](environments/prod.md)
