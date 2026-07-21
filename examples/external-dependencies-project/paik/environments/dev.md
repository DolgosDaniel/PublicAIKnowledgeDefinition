---
paik: "0.3"
kind: environment
id: dev
name: Development
lifecycle: active
owner:
  name: Platform team
  ref: https://aurora-logistics.example/directory/teams/platform
purpose: shared developer integration environment for all five services, auto-deployed from main
app_url: https://dev.aurora-logistics.example
health_endpoint: https://dev.aurora-logistics.example/health
databases:
  - type: postgres
    host_ref: "Vault path secret/aurora/dev/orders-service/db-url (orders database)"
  - type: postgres
    host_ref: "Vault path secret/aurora/dev/fleet-service/db-url (fleet database)"
access: VPN required
links:
  - kind: status-page
    url: https://status.aurora-logistics.example
  - kind: deploy-pipeline
    purpose: one per service, orders-service shown as representative
    url: https://github.com/aurora-logistics/orders-service/actions/workflows/deploy-dev.yml
  - kind: secrets
    provider: vault
    purpose: shared cross-service config, aurora/dev/shared/<key>
    url: https://vault.aurora-logistics.example/ui/vault/secrets/aurora
  - kind: dashboard
    provider: launchdarkly
    purpose: feature-flags
    url: https://app.launchdarkly.com/aurora-logistics
  - kind: chat
    id: "#aurora-platform"
  - kind: pagerduty
    url: https://aurora-logistics.pagerduty.com/schedules/platform
---

# Development

- Purpose: shared developer integration environment for all five services, auto-deployed from
  `main` on every merge
- App URL: https://dev.aurora-logistics.example
- Health endpoint: https://dev.aurora-logistics.example/health
- Databases (only the stateful services have one): Orders and Fleet, each Postgres — see
  `databases` above (Vault paths, never connection strings); `routing-service` and
  `notifications-service` are stateless
- Status page / deploy pipeline / shared secrets / feature flags: see `links` above
- Access: VPN required
- Owner: Platform team
