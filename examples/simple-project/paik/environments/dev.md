---
paik_version: "2.0"
doc_type: environment
id: dev
name: Development
status: active
last_updated: "2026-07-21"
owner_ref: ../team.md
visibility: internal
purpose: developer integration testing, auto-deployed from main on every merge
app_url: https://taskflow-lite-dev.onrender.com
health_endpoint: https://taskflow-lite-dev.onrender.com/health
status_page: https://status.render.com
databases:
  - type: postgres
    host_ref: ../configuration.md#dev-database
deploy_pipeline_ref: https://github.com/taskflow-inc/taskflow-lite/actions/workflows/deploy-dev.yml
config_ref: ../configuration.md#dev-database
access: public (read-only demo data, reset nightly)
---

# Development

- Purpose: developer integration testing, auto-deployed from `main` on every merge
- App URL: https://taskflow-lite-dev.onrender.com
- Health endpoint: https://taskflow-lite-dev.onrender.com/health
- Status page: https://status.render.com
- Database: Postgres — connection details in
  [configuration.md](../configuration.md#dev-database)
- Deploy pipeline: https://github.com/taskflow-inc/taskflow-lite/actions/workflows/deploy-dev.yml
- Access: public, read-only demo data, reset nightly
- Owner: [TaskFlow Lite team](../team.md)
