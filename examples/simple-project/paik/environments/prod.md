---
paik: "0.4"
type: paik-environment
id: prod
title: Production
lifecycle: active
purpose: customer-facing production
app_url: https://taskflow.example
health_endpoint: https://taskflow.example/health
databases:
  - type: postgres
    host_ref: env var TFL_DB_URL on the Render service "taskflow-lite-prod"
access: public
links:
  - kind: status-page
    url: https://status.taskflow.example
  - kind: deploy-pipeline
    url: https://github.com/taskflow-inc/taskflow-lite/actions/workflows/deploy-prod.yml
    purpose: manual approval required, see the Jira release checklist
---

# Production

- Purpose: customer-facing production
- App URL: https://taskflow.example
- Health endpoint: https://taskflow.example/health
- Database: Postgres — connection string lives in env var `TFL_DB_URL` on the Render service
  `taskflow-lite-prod`, never in this file
- Deploy pipeline: manual approval required (see the Jira release checklist) — see `links` above
- Access: public
