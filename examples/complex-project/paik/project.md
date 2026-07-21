---
paik_version: "1.0"
doc_type: project
id: nimbus-commerce
name: Nimbus Commerce
status: active
last_updated: "2026-07-21"
owner_ref: participants.md#eszter-varga
description: >
  A multi-service e-commerce platform: a frontend app plus an orders-api and a catalog-api
  microservice, built by three teams, deployed to four environments across two regions.
  Used here as the multi-service instance of the PAIK standard — the same doc types as
  examples/simple-project, but split one-per-service/one-per-region where that matches reality.
systems:
  ticketing: [systems/ticketing.md]
  knowledge_base: [systems/knowledge-base.md]
  api_specs: [systems/api-specs/orders.md, systems/api-specs/catalog.md]
  source_repos:
    [
      systems/source-repos/frontend.md,
      systems/source-repos/orders-api.md,
      systems/source-repos/catalog-api.md,
    ]
participants_ref: participants.md
environments_ref: environments/
configuration_ref: configuration/
---

# Nimbus Commerce

A multi-service e-commerce platform: a frontend app plus an `orders-api` and a `catalog-api`
microservice, built by three teams, deployed to four environments across two regions.

## Planning
- Ticketing (shared across all three services): [Jira — NIM](systems/ticketing.md)
- Knowledge base: [Confluence — NIM space](systems/knowledge-base.md)

## Implementation
- Services and their repos:
  - Frontend — [repo](systems/source-repos/frontend.md) (consumes both APIs below, has no API
    spec of its own)
  - Orders — [repo](systems/source-repos/orders-api.md) / [API spec](systems/api-specs/orders.md)
  - Catalog — [repo](systems/source-repos/catalog-api.md) / [API spec](systems/api-specs/catalog.md)

## People
- See [participants.md](participants.md) — Platform, Frontend, Orders, Catalog and SRE teams

## Operations
- Environments: [dev](environments/dev.md), [staging](environments/staging.md),
  [prod-eu](environments/prod-eu.md), [prod-us](environments/prod-us.md)
- Configuration management: [shared](configuration/shared.md),
  [orders-api](configuration/orders-api.md), [catalog-api](configuration/catalog-api.md)
