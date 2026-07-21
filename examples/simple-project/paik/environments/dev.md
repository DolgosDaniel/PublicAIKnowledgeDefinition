---
paik: "0.3"
kind: environment
id: dev
name: Development
lifecycle: active
purpose: developer integration testing, auto-deployed from main on every merge
app_url: https://taskflow-lite-dev.onrender.com
health_endpoint: https://taskflow-lite-dev.onrender.com/health
databases:
  - type: postgres
    host_ref: env var TFL_DB_URL on the Render service "taskflow-lite-dev"
access: public (read-only demo data, reset nightly)
links:
  - kind: status-page
    url: https://status.render.com
  - kind: deploy-pipeline
    url: https://github.com/taskflow-inc/taskflow-lite/actions/workflows/deploy-dev.yml
---

# Development

- Purpose: developer integration testing, auto-deployed from `main` on every merge
- App URL: https://taskflow-lite-dev.onrender.com
- Health endpoint: https://taskflow-lite-dev.onrender.com/health
- Database: Postgres — connection string lives in env var `TFL_DB_URL` on the Render service
  `taskflow-lite-dev`, never in this file
- Status page / deploy pipeline: see `links` above
- Access: public, read-only demo data, reset nightly
