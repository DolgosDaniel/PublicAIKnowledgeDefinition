---
paik: "0.4"
type: paik-component
id: ingest-api
title: Ingest API
lifecycle: active
owner:
  name: Data platform team
  ref: https://dataforge.example/wiki/spaces/DATA/pages/1/Data+Platform+Team
component_type: service
links:
  - kind: repository
    provider: github
    url: https://github.com/dataforge/ingest-api
  - kind: api
    purpose: provides
    provider: swaggerhub
    format: openapi
    id: dataforge/ingest-api
    url: https://api.swaggerhub.com/apis/dataforge/ingest-api/1.0.0
  - kind: jira-component
    id: ingest-api
    url: https://dataforge.example/jira/software/projects/DATA?component=ingest-api
  - kind: secrets
    provider: aws-secrets-manager
    url: https://console.aws.amazon.com/secretsmanager/dataforge/ingest-api
environments:
  - ../environments/dev.md
  - ../environments/prod.md
depends_on:
  - shared-validation-lib
---

# Ingest API

Accepts raw event data from client applications over HTTP and writes it to the warehouse's
landing zone, validating each payload against the shared schema library before accepting it.

- Type: `service`
- Repository / API / ticket scope / secrets: see `links` above
- Deployed to: [dev](../environments/dev.md), [prod](../environments/prod.md)
- Depends on: Shared Validation Library
- Owner: Data platform team
