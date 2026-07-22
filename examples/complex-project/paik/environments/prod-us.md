---
paik: "0.4"
type: paik-environment
id: prod-us
title: Production — US
lifecycle: active
owner:
  name: SRE & QA
  ref: https://nimbus-commerce.example/directory/teams/sre-qa
purpose: customer-facing production, US region
app_url: https://us.nimbus.example
health_endpoint: https://us.nimbus.example/health
databases:
  - type: postgres
    component: orders-api
    host_ref: "Vault path secret/nimbus/prod-us/orders-api/db-url"
  - type: postgres
    component: catalog-api
    host_ref: "Vault path secret/nimbus/prod-us/catalog-api/db-url"
access: SRE + release manager approval required
links:
  - kind: status-page
    url: https://status.nimbus.example
  - kind: deploy-pipeline
    component: frontend
    purpose: requires a signed-off release ticket (see the project's jira-project link)
    url: https://github.com/nimbus-commerce/frontend/actions/workflows/deploy-prod-us.yml
  - kind: deploy-pipeline
    component: orders-api
    purpose: requires a signed-off release ticket (see the project's jira-project link)
    url: https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-prod-us.yml
  - kind: deploy-pipeline
    component: catalog-api
    purpose: requires a signed-off release ticket (see the project's jira-project link)
    url: https://github.com/nimbus-commerce/catalog-api/actions/workflows/deploy-prod-us.yml
  - kind: secrets
    provider: vault
    purpose: shared cross-service config, nimbus/prod-us/shared/<key>
    url: https://vault.nimbus.example/ui/vault/secrets/nimbus
  - kind: dashboard
    provider: launchdarkly
    purpose: feature-flags
    url: https://app.launchdarkly.com/nimbus-commerce
  - kind: chat
    id: "#nimbus-sre-qa"
  - kind: pagerduty
    url: https://nimbus-commerce.pagerduty.com/schedules/sre
---

# Production — US

- Purpose: customer-facing production, US region
- App URL: https://us.nimbus.example
- Health endpoint: https://us.nimbus.example/health
- Databases: Orders and Catalog, each Postgres — see `databases` above (Vault paths, never
  connection strings)
- Deploy pipelines: one per component, each requiring a signed-off release ticket — see `links`
  above (tagged with the `component` each deploys)
- Access: SRE + release manager approval required
- Owner: SRE & QA
