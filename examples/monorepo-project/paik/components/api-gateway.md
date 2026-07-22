---
paik: "0.4"
type: paik-component
id: api-gateway
title: API Gateway
lifecycle: active
owner:
  name: Platform team
  ref: https://vertex-robotics.example/wiki/spaces/PLATFORM/pages/1/Platform+Team
component_type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/vertex-robotics/platform
    purpose: apps/api-gateway
  - kind: api
    purpose: provides
    provider: swaggerhub
    format: openapi
    id: vertex-robotics/api-gateway
    url: https://api.swaggerhub.com/apis/vertex-robotics/api-gateway/1.0.0
  - kind: jira-component
    id: api-gateway
    url: https://vertex-robotics.example/jira/software/projects/VTX?component=api-gateway
environments:
  - ../environments/dev.md
  - ../environments/prod.md
depends_on:
  - billing-service
---

# API Gateway

Routes external traffic to `billing-service` and other internal services. Lives at
`apps/api-gateway` in the `vertex-robotics/platform` monorepo.

- Type: `service`
- Repository (subpath `apps/api-gateway` of the shared monorepo) / API / ticket scope: see
  `links` above
- Deployed to: [dev](../environments/dev.md), [prod](../environments/prod.md)
- Depends on: Billing Service
- Owner: Platform team
