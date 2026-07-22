---
paik: "0.4"
type: paik-environment
id: prod
title: Production
lifecycle: active
owner:
  name: Payments team
  ref: https://helios-payments.example/wiki/spaces/PAY/pages/1/Payments+Team
purpose: customer-facing production - the only environment this project models (dev/staging exist internally but are out of scope here)
app_url: https://api.helios-payments.example
health_endpoint: https://api.helios-payments.example/health
databases:
  - type: postgres
    component: payments-api
    host_ref: "Vault path secret/helios/prod/payments-api/db-url"
  - type: redis
    component: ledger-worker
    host_ref: "Vault path secret/helios/prod/ledger-worker/queue-url"
access: SRE + release manager approval required, PCI-scoped
links:
  - kind: status-page
    url: https://status.helios-payments.example
  - kind: health-check
    component: ledger-worker
    purpose: ledger-worker has no public app_url of its own - this is its internal health probe
    url: https://internal.helios-payments.example/ledger-worker/health
  - kind: deploy-pipeline
    component: payments-api
    purpose: requires a signed-off release ticket
    url: https://github.com/helios-payments/payments-api/actions/workflows/deploy-prod.yml
  - kind: deploy-pipeline
    component: ledger-worker
    purpose: requires a signed-off release ticket
    url: https://github.com/helios-payments/ledger-worker/actions/workflows/deploy-prod.yml
  - kind: dashboard
    component: payments-api
    provider: grafana
    url: https://grafana.helios-payments.example/d/payments-api
  - kind: dashboard
    component: ledger-worker
    provider: grafana
    url: https://grafana.helios-payments.example/d/ledger-worker
  - kind: runbook
    component: payments-api
    purpose: incident response
    url: https://helios-payments.example/wiki/spaces/PAY/pages/20/Payments+API+Incident+Runbook
  - kind: runbook
    component: ledger-worker
    purpose: incident response
    url: https://helios-payments.example/wiki/spaces/PAY/pages/21/Ledger+Worker+Incident+Runbook
  - kind: backup-restore
    component: payments-api
    url: https://helios-payments.example/wiki/spaces/PAY/pages/22/Payments+DB+Backup+Restore
  - kind: pagerduty
    component: payments-api
    url: https://helios-payments.pagerduty.com/schedules/payments-api
  - kind: pagerduty
    component: ledger-worker
    url: https://helios-payments.pagerduty.com/schedules/ledger-worker
  - kind: logs
    component: payments-api
    provider: datadog
    url: https://app.datadoghq.com/logs?query=service:payments-api
  - kind: logs
    component: ledger-worker
    provider: datadog
    url: https://app.datadoghq.com/logs?query=service:ledger-worker
  - kind: slo
    component: payments-api
    url: https://helios-payments.example/wiki/spaces/PAY/pages/23/Payments+API+SLO
  - kind: slo
    component: ledger-worker
    url: https://helios-payments.example/wiki/spaces/PAY/pages/24/Ledger+Worker+SLO
---

# Production

The only environment this project models — dev/staging exist internally but are omitted here to
keep the example focused on a complete production operational map.

- Purpose: customer-facing production, PCI-scoped
- App URL / health endpoint: `payments-api`'s public API — see frontmatter; `ledger-worker` has
  no public endpoint, so its health check is a `links` entry instead (`kind: health-check`)
- Databases: Postgres for `payments-api`, Redis for `ledger-worker`'s settlement queue — see
  `databases` above (Vault paths, never connection strings)
- Access: SRE + release manager approval required, PCI-scoped

## Per-component operational map

Every link below is tagged `component: payments-api` or `component: ledger-worker` (per SPEC.md
section 3) rather than one link standing in for both:

| Concern | `payments-api` | `ledger-worker` |
|---|---|---|
| Deploy pipeline | ✅ | ✅ |
| Dashboard | ✅ (Grafana) | ✅ (Grafana) |
| Incident runbook | ✅ | ✅ |
| Backup/restore runbook | ✅ | — (stateless consumer of `payments-api`'s data) |
| On-call | ✅ (PagerDuty) | ✅ (PagerDuty) |
| Logs | ✅ (Datadog) | ✅ (Datadog) |
| SLO | ✅ | ✅ |
| Status page | shared — one incident surface for the whole environment, not per-component |
