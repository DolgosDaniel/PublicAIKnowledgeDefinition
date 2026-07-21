---
paik_version: "1.0"
doc_type: environment
id: <env-slug>
name: <Environment Name>
status: active
last_updated: <YYYY-MM-DD>
owner_ref: ../participants.md#<owner-anchor>
purpose: <e.g. "developer integration testing" / "customer-facing production, EU region">
app_url: https://<env>.example.com
health_endpoint: https://<env>.example.com/health
status_page: https://status.example.com
databases:
  - type: postgres
    host_ref: ../configuration.md#<env>-database
deploy_pipeline_ref: https://github.com/<org>/<repo>/actions/workflows/deploy-<env>.yml
config_ref: ../configuration.md#<env>
access: <e.g. "VPN + SSO required" / "public">
---

# <Environment Name>

- Purpose: <purpose>
- App URL: <app_url>
- Health endpoint: <health_endpoint>
- Status page: <status_page>
- Database(s): see `databases` above — connection details live in
  [configuration.md](../configuration.md#<env>-database), never here
- Deploy pipeline: <deploy_pipeline_ref>
- Access: <access>
- Owner: [<Owner Name>](../participants.md#<owner-anchor>)
