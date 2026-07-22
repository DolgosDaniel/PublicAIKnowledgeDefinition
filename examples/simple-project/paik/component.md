---
paik: "0.4"
type: paik-component
id: taskflow-lite-service
title: TaskFlow Lite
lifecycle: active
owner:
  name: TaskFlow Lite team
  ref: https://taskflow-inc.example/directory/teams/taskflow-lite
component_type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/taskflow-inc/taskflow-lite
    id: taskflow-inc/taskflow-lite
  - kind: api
    purpose: provides
    provider: swaggerhub
    id: taskflow-inc/taskflow-lite-api
    url: https://api.swaggerhub.com/apis/taskflow-inc/taskflow-lite-api/1.2.0
  - kind: jira-project
    id: TFL
    url: https://taskflow-inc.atlassian.net/jira/software/projects/TFL
  - kind: secrets
    provider: dotenv
    url: https://dashboard.render.com/web/taskflow-lite/env
environments:
  - environments/dev.md
  - environments/prod.md
depends_on: []
---

# TaskFlow Lite

The single service that makes up this project: a to-do list web app plus its API.

- Type: `service`
- Repository / API / ticket scope / secrets location: see `links` above (currently published API
  version `1.2.0`; dev is running a release candidate `1.3.0-rc1` ahead of prod)
- Deployed to: [dev](environments/dev.md), [prod](environments/prod.md)
- Depends on: none — single-service project
- Owner: TaskFlow Lite team
