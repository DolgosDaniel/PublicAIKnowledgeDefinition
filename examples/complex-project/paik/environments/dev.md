---
paik: "0.3"
kind: environment
id: dev
name: Development
lifecycle: active
owner:
  name: SRE & QA
  ref: https://nimbus-commerce.example/directory/teams/sre-qa
purpose: shared developer integration environment for all three services, auto-deployed from main
app_url: https://dev.nimbus.example
health_endpoint: https://dev.nimbus.example/health
databases:
  - type: postgres
    host_ref: "Vault path secret/nimbus/dev/orders-api/db-url (orders database)"
  - type: postgres
    host_ref: "Vault path secret/nimbus/dev/catalog-api/db-url (catalog database)"
access: VPN required
links:
  - kind: status-page
    url: https://status.nimbus.example
  - kind: deploy-pipeline
    purpose: one per service, orders-api shown as representative
    url: https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-dev.yml
  - kind: secrets
    provider: vault
    purpose: shared cross-service config, nimbus/dev/shared/<key>
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

# Development

- Purpose: shared developer integration environment for all three services, auto-deployed from
  `main` on every merge
- App URL: https://dev.nimbus.example
- Health endpoint: https://dev.nimbus.example/health
- Databases: Orders and Catalog, each Postgres — see `databases` above (Vault paths, never
  connection strings)
- Status page / deploy pipeline / shared secrets / feature flags: see `links` above
- Access: VPN required
- Owner: SRE & QA
