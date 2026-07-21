---
paik_version: "1.0"
doc_type: environment
id: prod-us
name: Production — US
status: active
last_updated: 2026-07-21
owner_ref: ../participants.md#adam-fekete
purpose: customer-facing production, US region
app_url: https://us.nimbus.example
health_endpoint: https://us.nimbus.example/health
status_page: https://status.nimbus.example
databases:
  - type: postgres
    host_ref: ../configuration/orders-api.md#prod-us-orders-database
  - type: postgres
    host_ref: ../configuration/catalog-api.md#prod-us-catalog-database
deploy_pipeline_ref: https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-prod-us.yml
config_ref: ../configuration/shared.md
access: SRE + release manager approval required
---

# Production — US

- Purpose: customer-facing production, US region
- App URL: https://us.nimbus.example
- Health endpoint: https://us.nimbus.example/health
- Status page: https://status.nimbus.example
- Databases:
  - Orders — [configuration](../configuration/orders-api.md#prod-us-orders-database)
  - Catalog — [configuration](../configuration/catalog-api.md#prod-us-catalog-database)
- Deploy pipelines: one per service, e.g.
  https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-prod-us.yml
  (requires a signed-off release ticket, see [ticketing.md](../systems/ticketing.md))
- Configuration: [shared](../configuration/shared.md),
  [orders-api](../configuration/orders-api.md), [catalog-api](../configuration/catalog-api.md)
- Access: SRE + release manager approval required
- Owner: [Adam Fekete](../participants.md#adam-fekete)
