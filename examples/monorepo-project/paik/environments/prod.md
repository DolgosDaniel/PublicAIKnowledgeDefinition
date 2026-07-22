---
paik: "0.4"
type: paik-environment
id: prod
title: Production
lifecycle: active
purpose: customer-facing production
app_url: https://vertex-robotics.example
health_endpoint: https://vertex-robotics.example/health
databases:
  - type: postgres
    component: billing-service
    host_ref: "Vault path secret/vertex/prod/billing-service/db-url"
access: SRE approval required
links:
  - kind: status-page
    url: https://status.vertex-robotics.example
  - kind: deploy-pipeline
    component: api-gateway
    url: https://github.com/vertex-robotics/platform/actions/workflows/deploy-api-gateway-prod.yml
  - kind: deploy-pipeline
    component: billing-service
    url: https://github.com/vertex-robotics/platform/actions/workflows/deploy-billing-service-prod.yml
  - kind: deploy-pipeline
    component: web-client
    url: https://github.com/vertex-robotics/platform/actions/workflows/deploy-web-client-prod.yml
---

# Production

- Purpose: customer-facing production
- App URL: https://vertex-robotics.example
- Health endpoint: https://vertex-robotics.example/health
- Database: Postgres, owned by `billing-service` — see `databases` above
- Status page / per-component deploy pipelines: see `links` above
- Access: SRE approval required
