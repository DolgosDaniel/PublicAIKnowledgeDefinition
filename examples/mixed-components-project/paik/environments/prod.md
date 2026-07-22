---
paik: "0.4"
type: paik-environment
id: prod
title: Production
lifecycle: active
purpose: production - serves ingest-api, runs the nightly-etl job, and hosts reporting-dashboard
app_url: https://ingest.dataforge.example
health_endpoint: https://ingest.dataforge.example/health
databases:
  - type: postgres
    component: ingest-api
    host_ref: "AWS Secrets Manager: dataforge/ingest-api/db-url"
access: internal only
links:
  - kind: status-page
    url: https://status.dataforge.example
  - kind: deploy-pipeline
    component: ingest-api
    url: https://github.com/dataforge/ingest-api/actions/workflows/deploy-prod.yml
  - kind: deploy-pipeline
    component: nightly-etl
    url: https://github.com/dataforge/nightly-etl/actions/workflows/deploy.yml
  - kind: dashboard
    component: reporting-dashboard
    provider: retool
    url: https://dataforge.retool.com/apps/reporting
---

# Production

- Purpose: serves `ingest-api`, runs the `nightly-etl` job, and hosts `reporting-dashboard`
- App URL (ingest-api): https://ingest.dataforge.example
- Health endpoint (ingest-api): https://ingest.dataforge.example/health
- Database: Postgres, owned by `ingest-api` — see `databases` above (Secrets Manager pointer,
  never a connection string)
- Status page / per-component deploy pipelines / dashboard: see `links` above (tagged with the
  `component` each applies to)
- Access: internal only
