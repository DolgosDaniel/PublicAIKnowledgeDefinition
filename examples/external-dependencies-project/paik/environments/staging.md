---
paik: "0.4"
type: paik-environment
id: staging
title: Staging
lifecycle: active
owner:
  name: Platform team
  ref: https://aurora-logistics.example/directory/teams/platform
purpose: pre-production verification, mirrors prod topology, manual promotion from dev
app_url: https://staging.aurora-logistics.example
health_endpoint: https://staging.aurora-logistics.example/health
databases:
  - type: postgres
    component: orders-service
    host_ref: "Vault path secret/aurora/staging/orders-service/db-url"
  - type: postgres
    component: fleet-service
    host_ref: "Vault path secret/aurora/staging/fleet-service/db-url"
access: VPN required
links:
  - kind: status-page
    url: https://status.aurora-logistics.example
  - kind: deploy-pipeline
    component: ops-console
    url: https://github.com/aurora-logistics/ops-console/actions/workflows/deploy-staging.yml
  - kind: deploy-pipeline
    component: orders-service
    url: https://github.com/aurora-logistics/orders-service/actions/workflows/deploy-staging.yml
  - kind: deploy-pipeline
    component: routing-service
    url: https://github.com/aurora-logistics/routing-service/actions/workflows/deploy-staging.yml
  - kind: deploy-pipeline
    component: fleet-service
    url: https://github.com/aurora-logistics/fleet-service/actions/workflows/deploy-staging.yml
  - kind: deploy-pipeline
    component: notifications-service
    url: https://github.com/aurora-logistics/notifications-service/actions/workflows/deploy-staging.yml
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
- Status page / per-component deploy pipelines / shared secrets / feature flags: see `links`
  above (each `deploy-pipeline` link is tagged with the `component` it deploys)
- Access: VPN required
- Owner: Platform team
