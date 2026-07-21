---
paik_version: "1.0"
doc_type: environment
id: dev
name: Development
status: active
last_updated: "2026-07-21"
owner_ref: ../participants.md#adam-fekete
purpose: shared developer integration environment for all three services, auto-deployed from main
app_url: https://dev.nimbus.example
health_endpoint: https://dev.nimbus.example/health
status_page: https://status.nimbus.example
databases:
  - type: postgres
    host_ref: ../configuration/orders-api.md#dev-orders-database
  - type: postgres
    host_ref: ../configuration/catalog-api.md#dev-catalog-database
deploy_pipeline_ref: https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-dev.yml
config_ref: ../configuration/shared.md
access: VPN required
---

# Development

- Purpose: shared developer integration environment for all three services, auto-deployed from
  `main` on every merge
- App URL: https://dev.nimbus.example
- Health endpoint: https://dev.nimbus.example/health
- Status page: https://status.nimbus.example
- Databases:
  - Orders — [configuration](../configuration/orders-api.md#dev-orders-database)
  - Catalog — [configuration](../configuration/catalog-api.md#dev-catalog-database)
- Deploy pipelines: one per service, e.g.
  https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-dev.yml
- Configuration: [shared](../configuration/shared.md),
  [orders-api](../configuration/orders-api.md), [catalog-api](../configuration/catalog-api.md)
- Access: VPN required
- Owner: [Adam Fekete](../participants.md#adam-fekete)
