---
paik_version: "2.1"
doc_type: project
id: aurora-logistics
name: Aurora Logistics
status: active
last_updated: "2026-07-21"
owner_ref: teams/platform.md
visibility: internal
description: >
  A fleet/delivery management platform: a dispatcher dashboard plus four microservices
  (orders, routing, fleet, notifications), built by six teams, deployed to three environments,
  and depending on two third-party services (Stripe for payments, Mapbox for routing/geocoding)
  it does not operate. Used here as the PAIK instance that demonstrates the external-service
  doc type and a multi-hop internal dependency graph, alongside examples/simple-project (one
  service) and examples/complex-project (three services, region-scaled environments).
systems:
  ticketing: [systems/ticketing.md]
  knowledge_base: [systems/knowledge-base.md]
  api_specs:
    [
      systems/api-specs/orders.md,
      systems/api-specs/routing.md,
      systems/api-specs/fleet.md,
      systems/api-specs/notifications.md,
    ]
  source_repos:
    [
      systems/source-repos/ops-console.md,
      systems/source-repos/orders-service.md,
      systems/source-repos/routing-service.md,
      systems/source-repos/fleet-service.md,
      systems/source-repos/notifications-service.md,
    ]
team_ref: teams/
components_ref: components/
external_services_ref: external-services/
environments_ref: environments/
configuration_ref: configuration/
---

# Aurora Logistics

A fleet/delivery management platform: a dispatcher dashboard (`ops-console`) plus four
microservices — `orders-service`, `routing-service`, `fleet-service`, `notifications-service` —
built by six teams, deployed to three environments, and depending on two third-party services it
does not operate.

## Planning
- Ticketing (shared across all five services): [Jira — AUR](systems/ticketing.md)
- Knowledge base: [Confluence — AUR space](systems/knowledge-base.md)

## Implementation
- Components (repo + API + config + environments + owner + dependencies, wired together):
  - [Ops Console](components/ops-console.md) (consumes Orders/Routing/Fleet, has no API of its own)
  - [Orders Service](components/orders-service.md) (depends on Routing + Notifications; calls Stripe)
  - [Routing Service](components/routing-service.md) (calls Mapbox)
  - [Fleet Service](components/fleet-service.md) (depends on Routing)
  - [Notifications Service](components/notifications-service.md)
- External services this project depends on but does not operate: see
  [external-services/](external-services/) — [Stripe](external-services/stripe.md) (payments),
  [Mapbox](external-services/mapbox.md) (routing/geocoding)

## Teams
- See [teams/](teams/) — Platform, Frontend, Orders, Routing, Fleet, and Notifications

## Operations
- Environments: [dev](environments/dev.md), [staging](environments/staging.md),
  [prod](environments/prod.md)
- Configuration management: [shared](configuration/shared.md),
  [orders-service](configuration/orders-service.md),
  [routing-service](configuration/routing-service.md),
  [fleet-service](configuration/fleet-service.md),
  [notifications-service](configuration/notifications-service.md)
