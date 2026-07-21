---
paik: "0.3"
kind: environment
id: prod-us
name: Production — US
lifecycle: active
owner:
  name: SRE & QA
  ref: https://nimbus-commerce.example/directory/teams/sre-qa
purpose: customer-facing production, US region
app_url: https://us.nimbus.example
health_endpoint: https://us.nimbus.example/health
databases:
  - type: postgres
    host_ref: "Vault path secret/nimbus/prod-us/orders-api/db-url (orders database)"
  - type: postgres
    host_ref: "Vault path secret/nimbus/prod-us/catalog-api/db-url (catalog database)"
access: SRE + release manager approval required
links:
  - kind: status-page
    url: https://status.nimbus.example
  - kind: deploy-pipeline
    purpose: one per service, orders-api shown as representative; requires a signed-off release ticket (see the project's jira-project link)
    url: https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-prod-us.yml
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
- Deploy pipeline: requires a signed-off release ticket — see `links` above
- Access: SRE + release manager approval required
- Owner: SRE & QA
