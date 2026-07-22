---
paik: "0.4"
type: paik-environment
id: prod
title: Production
description: Customer-facing production environment for Beacon Tasks.
lifecycle: active
purpose: customer-facing production
app_url: https://app.beacon-tasks.example
health_endpoint: https://app.beacon-tasks.example/health
databases:
  - type: postgres
    host_ref: env var BEACON_DB_URL on the Render service "beacon-tasks-prod"
access: public
links:
  - kind: status-page
    url: https://status.beacon-tasks.example
  - kind: deploy-pipeline
    url: https://github.com/beacon-tasks/service/actions/workflows/deploy-prod.yml
---

# Production

- Purpose: customer-facing production
- App URL: https://app.beacon-tasks.example
- Health endpoint: https://app.beacon-tasks.example/health
- Database: Postgres — connection string lives in env var `BEACON_DB_URL`, never in this file
- Status page / deploy pipeline: see `links` above
- Access: public
