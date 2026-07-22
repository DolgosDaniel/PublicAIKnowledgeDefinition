---
paik: "0.4"
type: paik-environment
id: dev
title: Development
lifecycle: active
owner:
  name: Platform team
  ref: https://aurora-logistics.example/directory/teams/platform
purpose: shared developer integration environment for all five services, auto-deployed from main
app_url: https://dev.aurora-logistics.example
health_endpoint: https://dev.aurora-logistics.example/health
databases:
  - type: postgres
    component: orders-service
    host_ref: "Vault path secret/aurora/dev/orders-service/db-url"
  - type: postgres
    component: fleet-service
    host_ref: "Vault path secret/aurora/dev/fleet-service/db-url"
access: VPN required
links:
  - kind: status-page
    url: https://status.aurora-logistics.example
  - kind: deploy-pipeline
    component: ops-console
    url: https://github.com/aurora-logistics/ops-console/actions/workflows/deploy-dev.yml
  - kind: deploy-pipeline
    component: orders-service
    url: https://github.com/aurora-logistics/orders-service/actions/workflows/deploy-dev.yml
  - kind: deploy-pipeline
    component: routing-service
    url: https://github.com/aurora-logistics/routing-service/actions/workflows/deploy-dev.yml
  - kind: deploy-pipeline
    component: fleet-service
    url: https://github.com/aurora-logistics/fleet-service/actions/workflows/deploy-dev.yml
  - kind: deploy-pipeline
    component: notifications-service
    url: https://github.com/aurora-logistics/notifications-service/actions/workflows/deploy-dev.yml
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
- Status page / per-component deploy pipelines / shared secrets / feature flags: see `links`
  above (each `deploy-pipeline` link is tagged with the `component` it deploys)
- Access: VPN required
- Owner: Platform team
