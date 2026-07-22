---
paik: "0.4"
type: paik-component
id: nightly-etl
title: Nightly ETL
lifecycle: active
owner:
  name: Data platform team
  ref: https://dataforge.example/wiki/spaces/DATA/pages/1/Data+Platform+Team
component_type: job
links:
  - kind: repository
    provider: github
    url: https://github.com/dataforge/nightly-etl
  - kind: deploy-pipeline
    url: https://github.com/dataforge/nightly-etl/actions/workflows/deploy.yml
    schedule: "0 3 * * *"
    purpose: runs nightly at 03:00 UTC against the prod warehouse; no dev/staging schedule
  - kind: jira-component
    id: nightly-etl
    url: https://dataforge.example/jira/software/projects/DATA?component=nightly-etl
  - kind: secrets
    provider: aws-secrets-manager
    url: https://console.aws.amazon.com/secretsmanager/dataforge/nightly-etl
environments:
  - ../environments/prod.md
depends_on:
  - shared-validation-lib
---

# Nightly ETL

A scheduled batch job (not an HTTP service) that re-validates and aggregates the previous day's
ingested events into the reporting warehouse.

- Type: `job`
- Repository / schedule / ticket scope / secrets: see `links` above (`schedule` is a free-form
  field on the `deploy-pipeline` link - `links[]` items aren't closed, so a `kind` can carry
  whatever extra fields it actually needs)
- Deployed to: [prod](../environments/prod.md) only — there's no separate dev/staging run
- Depends on: Shared Validation Library
- Owner: Data platform team
