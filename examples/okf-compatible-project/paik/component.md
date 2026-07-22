---
paik: "0.4"
type: paik-component
id: beacon-tasks-service
title: Beacon Tasks
description: The backend service for Beacon Tasks - task CRUD and assignment over a REST API.
lifecycle: active
owner:
  name: Beacon team
  ref: https://beacon-tasks.example/wiki/spaces/BEACON/pages/1/Beacon+Team
component_type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/beacon-tasks/service
  - kind: api
    purpose: provides
    provider: swaggerhub
    format: openapi
    id: beacon-tasks/service
    url: https://api.swaggerhub.com/apis/beacon-tasks/service/1.0.0
  - kind: jira-component
    id: service
    url: https://beacon-tasks.example/jira/software/projects/BCN?component=service
  - kind: secrets
    provider: dotenv
    url: https://dashboard.render.com/web/beacon-tasks/env
environments:
  - environments/dev.md
  - environments/prod.md
depends_on: []
---

# Beacon Tasks (service)

The backend service: task CRUD and assignment over a REST API.

- Type: `service`
- Repository / API / ticket scope / secrets: see `links` above
- Deployed to: [dev](environments/dev.md), [prod](environments/prod.md)
- Depends on: none
- Owner: Beacon team
