---
paik_version: "1.0"
doc_type: environment
id: prod
name: Production
status: active
last_updated: 2026-07-21
owner_ref: ../participants.md#bence-nagy
purpose: customer-facing production
app_url: https://taskflow.example
health_endpoint: https://taskflow.example/health
status_page: https://status.taskflow.example
databases:
  - type: postgres
    host_ref: ../configuration.md#prod-database
deploy_pipeline_ref: https://github.com/taskflow-inc/taskflow-lite/actions/workflows/deploy-prod.yml
config_ref: ../configuration.md#prod-database
access: public
---

# Production

- Purpose: customer-facing production
- App URL: https://taskflow.example
- Health endpoint: https://taskflow.example/health
- Status page: https://status.taskflow.example
- Database: Postgres — connection details in
  [configuration.md](../configuration.md#prod-database)
- Deploy pipeline: https://github.com/taskflow-inc/taskflow-lite/actions/workflows/deploy-prod.yml
  (manual approval required, see Jira release checklist in
  [ticketing.md](../systems/ticketing.md))
- Access: public
- Owner: [Bence Nagy](../participants.md#bence-nagy)
