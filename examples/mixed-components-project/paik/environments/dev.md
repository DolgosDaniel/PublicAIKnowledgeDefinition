---
paik: "0.3"
kind: environment
id: dev
name: Development
lifecycle: active
purpose: developer integration testing for ingest-api; the batch job and dashboard have no dev environment
app_url: https://ingest-dev.dataforge.example
health_endpoint: https://ingest-dev.dataforge.example/health
access: internal only
links:
  - kind: deploy-pipeline
    component: ingest-api
    url: https://github.com/dataforge/ingest-api/actions/workflows/deploy-dev.yml
---

# Development

- Purpose: developer integration testing for `ingest-api`; `nightly-etl` and
  `reporting-dashboard` have no dev environment
- App URL: https://ingest-dev.dataforge.example
- Health endpoint: https://ingest-dev.dataforge.example/health
- Deploy pipeline: see `links` above
- Access: internal only
