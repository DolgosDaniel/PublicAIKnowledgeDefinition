---
paik_version: "1.0"
doc_type: environment
id: staging
name: Staging
status: active
last_updated: 2026-07-21
owner_ref: ../participants.md#adam-fekete
purpose: pre-production verification, mirrors prod topology, manual promotion from dev
app_url: https://staging.nimbus.example
health_endpoint: https://staging.nimbus.example/health
status_page: https://status.nimbus.example
databases:
  - type: postgres
    host_ref: ../configuration/orders-api.md#staging-orders-database
  - type: postgres
    host_ref: ../configuration/catalog-api.md#staging-catalog-database
deploy_pipeline_ref: https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-staging.yml
config_ref: ../configuration/shared.md
access: VPN required
---

# Staging

- Purpose: pre-production verification, mirrors prod topology, promoted manually from `dev`
- App URL: https://staging.nimbus.example
- Health endpoint: https://staging.nimbus.example/health
- Status page: https://status.nimbus.example
- Databases:
  - Orders — [configuration](../configuration/orders-api.md#staging-orders-database)
  - Catalog — [configuration](../configuration/catalog-api.md#staging-catalog-database)
- Deploy pipelines: one per service, e.g.
  https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-staging.yml
- Configuration: [shared](../configuration/shared.md),
  [orders-api](../configuration/orders-api.md), [catalog-api](../configuration/catalog-api.md)
- Access: VPN required
- Owner: [Adam Fekete](../participants.md#adam-fekete)
