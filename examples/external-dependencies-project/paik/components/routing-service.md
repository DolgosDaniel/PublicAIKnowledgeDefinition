---
paik: "0.3"
kind: component
id: routing-service
name: Routing Service
lifecycle: active
owner:
  name: Routing team
  ref: https://aurora-logistics.example/directory/teams/routing
type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/aurora-logistics/routing-service
    id: aurora-logistics/routing-service
    purpose: trunk-based, short-lived feature branches, PR review required
  - kind: api
    purpose: provides
    provider: swaggerhub
    protocol: grpc
    id: aurora-logistics/routing-service
    url: https://api.swaggerhub.com/apis/aurora-logistics/routing-service/2.0.0
    served_by_env:
      dev: 2.1.0-rc1
      staging: 2.0.0
      prod: 2.0.0
  - kind: jira-component
    id: routing-service
    url: https://aurora-logistics.atlassian.net/jira/software/projects/AUR/boards/1?component=routing-service
  - kind: secrets
    provider: vault
    url: https://vault.aurora-logistics.example/ui/vault/secrets/aurora
    purpose: "aurora/<environment>/routing-service/<key>"
  - kind: external-service
    provider: mapbox
    vendor: Mapbox, Inc.
    url: https://www.mapbox.com
    docs_url: https://docs.mapbox.com/api/
    status_page: https://status.mapbox.com
    contract_ref: https://aurora-logistics.atlassian.net/wiki/spaces/AUR/overview
    data_shared: pickup/dropoff coordinates and driver GPS pings for route optimization and geocoding
    secret_ref: "Vault path aurora/<environment>/routing-service/mapbox-token, never the token itself"
  - kind: chat
    id: "#aurora-routing"
  - kind: pagerduty
    url: https://aurora-logistics.pagerduty.com/schedules/routing
environments:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod.md
depends_on: []
---

# Routing Service

Route optimization and dispatch: given a set of pickups/dropoffs, returns an optimized route.
Stateless — calls Mapbox for the underlying geocoding/routing computation.

- Type: `service`
- Repository / API / ticket scope / secrets / Mapbox: see `links` above
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod](../environments/prod.md)
- Depends on: none (internal)
- External dependencies: Mapbox (route optimization/geocoding) — see `links` above
- Owner: Routing team
