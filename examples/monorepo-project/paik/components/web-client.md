---
paik: "0.3"
kind: component
id: web-client
name: Web Client
lifecycle: active
owner:
  name: Platform team
  ref: https://vertex-robotics.example/wiki/spaces/PLATFORM/pages/1/Platform+Team
type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/vertex-robotics/platform
    purpose: apps/web-client
  - kind: api
    purpose: consumes
    provider: swaggerhub
    format: openapi
    id: vertex-robotics/api-gateway
    url: https://api.swaggerhub.com/apis/vertex-robotics/api-gateway/1.0.0
  - kind: jira-component
    id: web-client
    url: https://vertex-robotics.example/jira/software/projects/VTX?component=web-client
environments:
  - ../environments/dev.md
  - ../environments/prod.md
depends_on:
  - api-gateway
---

# Web Client

The customer-facing web app. Lives at `apps/web-client` in the `vertex-robotics/platform`
monorepo, the third component sharing that one repository URL.

- Type: `service`
- Repository (subpath `apps/web-client` of the shared monorepo) / consumed API / ticket scope:
  see `links` above
- Deployed to: [dev](../environments/dev.md), [prod](../environments/prod.md)
- Depends on: API Gateway
- Owner: Platform team
