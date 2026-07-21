---
paik: "0.3"
kind: environment
id: staging
name: Staging
lifecycle: active
owner:
  name: Platform team
  ref: https://aurora-logistics.example/directory/teams/platform
purpose: pre-production verification, mirrors prod topology, manual promotion from dev
app_url: https://staging.aurora-logistics.example
health_endpoint: https://staging.aurora-logistics.example/health
databases:
  - type: postgres
    host_ref: "Vault path secret/aurora/staging/orders-service/db-url (orders database)"
  - type: postgres
    host_ref: "Vault path secret/aurora/staging/fleet-service/db-url (fleet database)"
access: VPN required
links:
  - kind: status-page
    url: https://status.aurora-logistics.example
  - kind: deploy-pipeline
    purpose: one per service, orders-service shown as representative
    url: https://github.com/aurora-logistics/orders-service/actions/workflows/deploy-staging.yml
  - kind: secrets
    provider: vault
    purpose: shared cross-service config, aurora/staging/shared/<key>
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

# Staging

- Purpose: pre-production verification, mirrors prod topology, promoted manually from `dev`
- App URL: https://staging.aurora-logistics.example
- Health endpoint: https://staging.aurora-logistics.example/health
- Databases (only the stateful services have one): Orders and Fleet, each Postgres — see
  `databases` above (Vault paths, never connection strings)
- Status page / deploy pipeline / shared secrets / feature flags: see `links` above
- Access: VPN required
- Owner: Platform team
