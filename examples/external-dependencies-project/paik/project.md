---
paik: "0.4"
type: paik-project
id: aurora-logistics
title: Aurora Logistics
lifecycle: active
owner:
  name: Platform team
  ref: https://aurora-logistics.example/directory/teams/platform
description: >
  A fleet/delivery management platform: a dispatcher dashboard plus four microservices
  (orders, routing, fleet, notifications), built by six teams, deployed to three environments,
  and depending on two third-party services (Stripe for payments, Mapbox for routing/geocoding)
  it does not operate. Used here as the PAIK v0.4 instance that demonstrates third-party
  dependencies (as `links[].kind: external-service`, no dedicated document type) and a multi-hop
  internal dependency graph, alongside examples/simple-project (one service) and
  examples/complex-project (three services, region-scaled environments).
links:
  - kind: jira-project
    id: AUR
    purpose: shared across all five services; components distinguish teams within the same board
    url: https://aurora-logistics.atlassian.net/jira/software/projects/AUR/boards/1
  - kind: confluence
    purpose: project-home
    url: https://aurora-logistics.atlassian.net/wiki/spaces/AUR/overview
components:
  - components/ops-console.md
  - components/orders-service.md
  - components/routing-service.md
  - components/fleet-service.md
  - components/notifications-service.md
environments:
  - environments/dev.md
  - environments/staging.md
  - environments/prod.md
---

# Aurora Logistics

A fleet/delivery management platform: a dispatcher dashboard (`ops-console`) plus four
microservices — `orders-service`, `routing-service`, `fleet-service`, `notifications-service` —
built by six teams, deployed to three environments, and depending on two third-party services it
does not operate.

## Where things live
- Ticketing (shared across all five services): Jira, project `AUR` — see `links` above
- Knowledge base: Confluence, `AUR` space — see `links` above (vendor contract/SLA pages for
  Stripe/Mapbox live under this space as child pages)

## Implementation
- Components (repo/API/secrets/environments/owner/dependencies wired together via `links`/`owner`/`depends_on`):
  - [Ops Console](components/ops-console.md) (consumes Orders/Routing/Fleet, has no API of its own)
  - [Orders Service](components/orders-service.md) (depends on Routing + Notifications; calls Stripe)
  - [Routing Service](components/routing-service.md) (calls Mapbox)
  - [Fleet Service](components/fleet-service.md) (depends on Routing)
  - [Notifications Service](components/notifications-service.md)
- Third-party dependencies the project calls but does not operate: Stripe (payments, on
  `orders-service`) and Mapbox (routing/geocoding, on `routing-service`) — each is a
  `kind: external-service` entry in that component's `links`, not a separate document.

## Operations
- Environments: [dev](environments/dev.md), [staging](environments/staging.md),
  [prod](environments/prod.md)
