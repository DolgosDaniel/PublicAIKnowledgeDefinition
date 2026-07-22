---
paik: "0.4"
type: paik-environment
id: dev
title: Development
description: Developer integration environment for Beacon Tasks.
lifecycle: active
purpose: developer integration testing, auto-deployed from main on every merge
app_url: https://beacon-tasks-dev.onrender.com
health_endpoint: https://beacon-tasks-dev.onrender.com/health
databases:
  - type: postgres
    host_ref: env var BEACON_DB_URL on the Render service "beacon-tasks-dev"
access: internal only
links:
  - kind: deploy-pipeline
    url: https://github.com/beacon-tasks/service/actions/workflows/deploy-dev.yml
---

# Development

- Purpose: developer integration testing, auto-deployed from `main` on every merge
- App URL: https://beacon-tasks-dev.onrender.com
- Health endpoint: https://beacon-tasks-dev.onrender.com/health
- Database: Postgres — connection string lives in env var `BEACON_DB_URL`, never in this file
- Deploy pipeline: see `links` above
- Access: internal only
