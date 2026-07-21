---
paik_version: "2.1"
doc_type: environment
id: staging
name: Staging
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/platform.md
visibility: internal
purpose: pre-production verification, mirrors prod topology, manual promotion from dev
app_url: https://staging.aurora-logistics.example
health_endpoint: https://staging.aurora-logistics.example/health
status_page: https://status.aurora-logistics.example
databases:
  - type: postgres
    host_ref: ../configuration/orders-service.md#staging-orders-database
  - type: postgres
    host_ref: ../configuration/fleet-service.md#staging-fleet-database
deploy_pipeline_ref: https://github.com/aurora-logistics/orders-service/actions/workflows/deploy-staging.yml
config_ref: ../configuration/shared.md
access: VPN required
---

# Staging

- Purpose: pre-production verification, mirrors prod topology, promoted manually from `dev`
- App URL: https://staging.aurora-logistics.example
- Health endpoint: https://staging.aurora-logistics.example/health
- Status page: https://status.aurora-logistics.example
- Databases (only the stateful services have one):
  - Orders — [configuration](../configuration/orders-service.md#staging-orders-database)
  - Fleet — [configuration](../configuration/fleet-service.md#staging-fleet-database)
- Deploy pipelines: one per service, e.g.
  https://github.com/aurora-logistics/orders-service/actions/workflows/deploy-staging.yml
- Configuration: [shared](../configuration/shared.md), plus each service's own configuration doc
- Access: VPN required
- Owner: [Platform](../teams/platform.md)
