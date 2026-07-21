---
paik: "0.3"
kind: project
id: vertex-platform
name: Vertex Platform
lifecycle: active
owner:
  name: Platform team
  ref: https://vertex-robotics.example/wiki/spaces/PLATFORM/pages/1/Platform+Team
description: >
  Three components living in one GitHub monorepo. Used here to show that a PAIK component is
  not the same thing as a repository - each component's `repository` link points at the same
  URL with a different `purpose` naming its subpath, a common real-world setup the other
  examples (one repo per component) don't cover.
links:
  - kind: jira-project
    id: VTX
    url: https://vertex-robotics.example/jira/software/projects/VTX
  - kind: confluence
    purpose: project-home
    url: https://vertex-robotics.example/wiki/spaces/PLATFORM/overview
components:
  - components/api-gateway.md
  - components/billing-service.md
  - components/web-client.md
environments:
  - environments/dev.md
  - environments/prod.md
---

# Vertex Platform

Three components — [API Gateway](components/api-gateway.md),
[Billing Service](components/billing-service.md), and
[Web Client](components/web-client.md) — all living in a single repository,
`github.com/vertex-robotics/platform`, each in its own subpath. Each component's `repository`
link carries the same `url` with a `purpose` field naming that subpath; there is no PAIK rule
that one component gets one repository.

## Operations
- Environments: [dev](environments/dev.md), [prod](environments/prod.md)
