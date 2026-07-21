---
paik: "0.3"
kind: environment
id: prod-eu
name: Production — EU
lifecycle: active
owner:
  name: SRE & QA
  ref: https://nimbus-commerce.example/directory/teams/sre-qa
purpose: customer-facing production, EU region, GDPR-scoped customer data
app_url: https://eu.nimbus.example
health_endpoint: https://eu.nimbus.example/health
databases:
  - type: postgres
    host_ref: "Vault path secret/nimbus/prod-eu/orders-api/db-url (orders database)"
  - type: postgres
    host_ref: "Vault path secret/nimbus/prod-eu/catalog-api/db-url (catalog database)"
access: SRE + release manager approval required
links:
  - kind: status-page
    url: https://status.nimbus.example
  - kind: deploy-pipeline
    purpose: one per service, orders-api shown as representative; requires a signed-off release ticket (see the project's jira-project link)
    url: https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-prod-eu.yml
  - kind: secrets
    provider: vault
    purpose: shared cross-service config, nimbus/prod-eu/shared/<key>
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

# Production — EU

- Purpose: customer-facing production, EU region, GDPR-scoped customer data
- App URL: https://eu.nimbus.example
- Health endpoint: https://eu.nimbus.example/health
- Databases: Orders and Catalog, each Postgres — see `databases` above (Vault paths, never
  connection strings)
- Deploy pipeline: requires a signed-off release ticket — see `links` above
- Access: SRE + release manager approval required
- Owner: SRE & QA
