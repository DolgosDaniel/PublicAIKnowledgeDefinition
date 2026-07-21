---
paik_version: "2.1"
doc_type: environment
id: prod
name: Production
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/platform.md
visibility: internal
purpose: customer-facing production
app_url: https://app.aurora-logistics.example
health_endpoint: https://app.aurora-logistics.example/health
status_page: https://status.aurora-logistics.example
databases:
  - type: postgres
    host_ref: ../configuration/orders-service.md#prod-orders-database
  - type: postgres
    host_ref: ../configuration/fleet-service.md#prod-fleet-database
deploy_pipeline_ref: https://github.com/aurora-logistics/orders-service/actions/workflows/deploy-prod.yml
config_ref: ../configuration/shared.md
access: SRE + release manager approval required
---

# Production

- Purpose: customer-facing production
- App URL: https://app.aurora-logistics.example
- Health endpoint: https://app.aurora-logistics.example/health
- Status page: https://status.aurora-logistics.example
- Databases (only the stateful services have one):
  - Orders — [configuration](../configuration/orders-service.md#prod-orders-database)
  - Fleet — [configuration](../configuration/fleet-service.md#prod-fleet-database)
- Deploy pipelines: one per service, e.g.
  https://github.com/aurora-logistics/orders-service/actions/workflows/deploy-prod.yml
  (requires a signed-off release ticket, see [ticketing.md](../systems/ticketing.md))
- Configuration: [shared](../configuration/shared.md), plus each service's own configuration doc
- Access: SRE + release manager approval required
- Owner: [Platform](../teams/platform.md)
