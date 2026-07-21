---
paik_version: "1.0"
doc_type: environment
id: prod-eu
name: Production — EU
status: active
last_updated: 2026-07-21
owner_ref: ../participants.md#adam-fekete
purpose: customer-facing production, EU region, GDPR-scoped customer data
app_url: https://eu.nimbus.example
health_endpoint: https://eu.nimbus.example/health
status_page: https://status.nimbus.example
databases:
  - type: postgres
    host_ref: ../configuration/orders-api.md#prod-eu-orders-database
  - type: postgres
    host_ref: ../configuration/catalog-api.md#prod-eu-catalog-database
deploy_pipeline_ref: https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-prod-eu.yml
config_ref: ../configuration/shared.md
access: SRE + release manager approval required
---

# Production — EU

- Purpose: customer-facing production, EU region, GDPR-scoped customer data
- App URL: https://eu.nimbus.example
- Health endpoint: https://eu.nimbus.example/health
- Status page: https://status.nimbus.example
- Databases:
  - Orders — [configuration](../configuration/orders-api.md#prod-eu-orders-database)
  - Catalog — [configuration](../configuration/catalog-api.md#prod-eu-catalog-database)
- Deploy pipelines: one per service, e.g.
  https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-prod-eu.yml
  (requires a signed-off release ticket, see [ticketing.md](../systems/ticketing.md))
- Configuration: [shared](../configuration/shared.md),
  [orders-api](../configuration/orders-api.md), [catalog-api](../configuration/catalog-api.md)
- Access: SRE + release manager approval required
- Owner: [Adam Fekete](../participants.md#adam-fekete)
