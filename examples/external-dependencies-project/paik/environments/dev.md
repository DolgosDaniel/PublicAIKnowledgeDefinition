---
paik_version: "2.1"
doc_type: environment
id: dev
name: Development
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/platform.md
visibility: internal
purpose: shared developer integration environment for all five services, auto-deployed from main
app_url: https://dev.aurora-logistics.example
health_endpoint: https://dev.aurora-logistics.example/health
status_page: https://status.aurora-logistics.example
databases:
  - type: postgres
    host_ref: ../configuration/orders-service.md#dev-orders-database
  - type: postgres
    host_ref: ../configuration/fleet-service.md#dev-fleet-database
deploy_pipeline_ref: https://github.com/aurora-logistics/orders-service/actions/workflows/deploy-dev.yml
config_ref: ../configuration/shared.md
access: VPN required
---

# Development

- Purpose: shared developer integration environment for all five services, auto-deployed from
  `main` on every merge
- App URL: https://dev.aurora-logistics.example
- Health endpoint: https://dev.aurora-logistics.example/health
- Status page: https://status.aurora-logistics.example
- Databases (only the stateful services have one):
  - Orders — [configuration](../configuration/orders-service.md#dev-orders-database)
  - Fleet — [configuration](../configuration/fleet-service.md#dev-fleet-database)
- Deploy pipelines: one per service, e.g.
  https://github.com/aurora-logistics/orders-service/actions/workflows/deploy-dev.yml
- Configuration: [shared](../configuration/shared.md), plus each service's own configuration doc
- Access: VPN required
- Owner: [Platform](../teams/platform.md)
