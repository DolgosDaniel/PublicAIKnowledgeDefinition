---
paik: "0.3"
kind: environment
id: <env-slug>
name: <Environment Name>
lifecycle: active
purpose: <e.g. "developer integration testing" / "customer-facing production, EU region">
app_url: https://<env>.example.com
health_endpoint: https://<env>.example.com/health
databases:
  - type: postgres
    host_ref: <e.g. "Vault: secret/data/<project>/<env>#database" or an env var name>
access: <e.g. "VPN + SSO required" / "public">
links:
  - kind: status-page
    url: https://status.example.com
  - kind: deploy-pipeline
    url: https://github.com/<org>/<repo>/actions/workflows/deploy-<env>.yml
---

# <Environment Name>

- Purpose: <purpose>
- App URL: <app_url>
- Health endpoint: <health_endpoint>
- Database(s): see `databases` above — connection details live wherever `host_ref` points,
  never here
- Status page / deploy pipeline: see `links` above
- Access: <access>
