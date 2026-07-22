---
paik: "0.4"
type: paik-component
id: billing-service
title: Billing Service
lifecycle: active
owner:
  name: Platform team
  ref: https://vertex-robotics.example/wiki/spaces/PLATFORM/pages/1/Platform+Team
component_type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/vertex-robotics/platform
    purpose: services/billing
  - kind: api
    purpose: provides
    provider: swaggerhub
    format: openapi
    id: vertex-robotics/billing-service
    url: https://api.swaggerhub.com/apis/vertex-robotics/billing-service/1.0.0
  - kind: jira-component
    id: billing-service
    url: https://vertex-robotics.example/jira/software/projects/VTX?component=billing-service
  - kind: secrets
    provider: vault
    url: https://vault.vertex-robotics.example/ui/vault/secrets/vertex
environments:
  - ../environments/dev.md
  - ../environments/prod.md
depends_on: []
---

# Billing Service

Owns invoicing and payment state. Lives at `services/billing` in the `vertex-robotics/platform`
monorepo — a different subpath of the same repository as `api-gateway`, not a repository of its
own.

- Type: `service`
- Repository (subpath `services/billing` of the shared monorepo) / API / ticket scope / secrets:
  see `links` above
- Deployed to: [dev](../environments/dev.md), [prod](../environments/prod.md)
- Depends on: none
- Owner: Platform team
