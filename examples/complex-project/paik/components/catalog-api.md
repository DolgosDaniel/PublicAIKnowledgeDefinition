---
paik: "0.3"
kind: component
id: catalog-api
name: Catalog API
lifecycle: active
owner:
  name: Catalog team
  ref: https://nimbus-commerce.example/directory/teams/catalog
type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/nimbus-commerce/catalog-api
    id: nimbus-commerce/catalog-api
    purpose: trunk-based, short-lived feature branches, PR review required
  - kind: api
    purpose: provides
    provider: swaggerhub
    id: nimbus-commerce/catalog-api
    url: https://api.swaggerhub.com/apis/nimbus-commerce/catalog-api/2.1.0
    served_by_env:
      dev: 2.2.0-rc1
      staging: 2.1.0
      prod-eu: 2.1.0
      prod-us: 2.1.0
  - kind: jira-component
    id: catalog-api
    url: https://nimbus-commerce.atlassian.net/jira/software/projects/NIM/boards/4?component=catalog-api
  - kind: secrets
    provider: vault
    url: https://vault.nimbus.example/ui/vault/secrets/nimbus
    purpose: "nimbus/<environment>/catalog-api/<key>"
  - kind: chat
    id: "#nimbus-catalog"
  - kind: pagerduty
    url: https://nimbus-commerce.pagerduty.com/schedules/catalog
environments:
  - ../environments/dev.md
  - ../environments/staging.md
  - ../environments/prod-eu.md
  - ../environments/prod-us.md
depends_on: []
---

# Catalog API

The catalog microservice: owns the Catalog API contract end to end.

- Type: `service`
- Repository / API / ticket scope / secrets: see `links` above
- Deployed to: [dev](../environments/dev.md), [staging](../environments/staging.md),
  [prod-eu](../environments/prod-eu.md), [prod-us](../environments/prod-us.md)
- Depends on: none
- Owner: Catalog team
