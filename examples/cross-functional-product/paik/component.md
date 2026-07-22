---
paik: "0.4"
type: paik-component
id: rewards-app
title: Rewards App
lifecycle: active
owner:
  name: Rewards engineering team
  ref: https://solstice-app.example/wiki/spaces/REWARDS/pages/2/Engineering+Team
component_type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/solstice-app/rewards-app
    id: solstice-app/rewards-app
  - kind: api
    purpose: provides
    provider: swaggerhub
    format: openapi
    id: solstice-app/rewards-api
    url: https://api.swaggerhub.com/apis/solstice-app/rewards-api/1.0.0
  - kind: jira-component
    id: rewards-app
    url: https://solstice-app.example/jira/software/projects/REW?component=rewards-app
  - kind: secrets
    provider: dotenv
    url: https://dashboard.render.com/web/rewards-app/env
environments:
  - environments/dev.md
  - environments/prod.md
depends_on: []
---

# Rewards App

The backend and mobile client for the loyalty program: point accrual, redemption, and offer
notifications.

- Type: `service`
- Repository / API / ticket scope / secrets: see `links` above
- Deployed to: [dev](environments/dev.md), [prod](environments/prod.md)
- Depends on: none
- Owner: Rewards engineering team

The *product* side of this project (brief, design, metrics, roadmap) lives on `project.md`'s
`links` — this file only carries what an engineer needs to build and ship the component.
