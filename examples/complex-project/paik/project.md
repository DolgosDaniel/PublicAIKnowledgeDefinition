---
paik: "0.4"
type: paik-project
id: nimbus-commerce
title: Nimbus Commerce
lifecycle: active
owner:
  name: Platform team
  ref: https://nimbus-commerce.example/directory/teams/platform
description: >
  A multi-service e-commerce platform: a frontend app plus an orders-api and a catalog-api
  microservice, built by three service teams and operated by a shared SRE & QA team, deployed
  to four environments across two regions. Used here as the multi-service instance of the PAIK
  v0.3 standard — same shape as examples/simple-project, just split one-per-service/one-per-region
  where that matches reality.
links:
  - kind: jira-project
    id: NIM
    purpose: shared across all three services; components distinguish teams within the same board
    url: https://nimbus-commerce.atlassian.net/jira/software/projects/NIM/boards/4
  - kind: confluence
    purpose: project-home
    url: https://nimbus-commerce.atlassian.net/wiki/spaces/NIM/overview
components:
  - components/frontend.md
  - components/orders-api.md
  - components/catalog-api.md
environments:
  - environments/dev.md
  - environments/staging.md
  - environments/prod-eu.md
  - environments/prod-us.md
---

# Nimbus Commerce

A multi-service e-commerce platform: a frontend app plus an `orders-api` and a `catalog-api`
microservice, built by three service teams and operated by a shared SRE & QA team, deployed to
four environments across two regions.

## Where things live
- Ticketing (shared across all three services): Jira, project `NIM` — see `links` above
- Knowledge base: Confluence, `NIM` space — see `links` above (per-service runbooks live as child
  pages, `NIM / Orders`, `NIM / Catalog`, `NIM / Frontend`, rather than separate PAIK documents)

## Implementation
- Components (repo/API/secrets/environments/owner wired together via `links`/`owner`):
  - [Frontend](components/frontend.md) (consumes both APIs below, has no API of its own)
  - [Orders API](components/orders-api.md)
  - [Catalog API](components/catalog-api.md)

## Operations
- Environments: [dev](environments/dev.md), [staging](environments/staging.md),
  [prod-eu](environments/prod-eu.md), [prod-us](environments/prod-us.md)
