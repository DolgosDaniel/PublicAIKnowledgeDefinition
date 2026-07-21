---
paik: "0.3"
kind: environment
id: prod
name: Production
lifecycle: active
owner:
  name: Platform team
  ref: https://aurora-logistics.example/directory/teams/platform
purpose: customer-facing production
app_url: https://app.aurora-logistics.example
health_endpoint: https://app.aurora-logistics.example/health
databases:
  - type: postgres
    component: orders-service
    host_ref: "Vault path secret/aurora/prod/orders-service/db-url"
  - type: postgres
    component: fleet-service
    host_ref: "Vault path secret/aurora/prod/fleet-service/db-url"
access: SRE + release manager approval required
links:
  - kind: status-page
    url: https://status.aurora-logistics.example
  - kind: deploy-pipeline
    component: ops-console
    purpose: requires a signed-off release ticket (see the project's jira-project link)
    url: https://github.com/aurora-logistics/ops-console/actions/workflows/deploy-prod.yml
  - kind: deploy-pipeline
    component: orders-service
    purpose: requires a signed-off release ticket (see the project's jira-project link)
    url: https://github.com/aurora-logistics/orders-service/actions/workflows/deploy-prod.yml
  - kind: deploy-pipeline
    component: routing-service
    purpose: requires a signed-off release ticket (see the project's jira-project link)
    url: https://github.com/aurora-logistics/routing-service/actions/workflows/deploy-prod.yml
  - kind: deploy-pipeline
    component: fleet-service
    purpose: requires a signed-off release ticket (see the project's jira-project link)
    url: https://github.com/aurora-logistics/fleet-service/actions/workflows/deploy-prod.yml
  - kind: deploy-pipeline
    component: notifications-service
    purpose: requires a signed-off release ticket (see the project's jira-project link)
    url: https://github.com/aurora-logistics/notifications-service/actions/workflows/deploy-prod.yml
  - kind: secrets
    provider: vault
    purpose: shared cross-service config, aurora/prod/shared/<key>
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

# Production

- Purpose: customer-facing production
- App URL: https://app.aurora-logistics.example
- Health endpoint: https://app.aurora-logistics.example/health
- Databases (only the stateful services have one): Orders and Fleet, each Postgres — see
  `databases` above (Vault paths, never connection strings)
- Deploy pipelines: one per component, each requiring a signed-off release ticket — see `links`
  above (tagged with the `component` each deploys)
- Access: SRE + release manager approval required
- Owner: Platform team
