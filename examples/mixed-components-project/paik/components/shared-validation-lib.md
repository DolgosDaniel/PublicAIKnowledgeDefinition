---
paik: "0.4"
type: paik-component
id: shared-validation-lib
title: Shared Validation Library
lifecycle: active
owner:
  name: Data platform team
  ref: https://dataforge.example/wiki/spaces/DATA/pages/1/Data+Platform+Team
component_type: library
links:
  - kind: repository
    provider: github
    url: https://github.com/dataforge/validation-lib
  - kind: package-registry
    provider: npm
    id: "@dataforge/validation"
    url: https://www.npmjs.com/package/@dataforge/validation
  - kind: jira-component
    id: shared-validation-lib
    url: https://dataforge.example/jira/software/projects/DATA?component=shared-validation-lib
environments: []
depends_on: []
---

# Shared Validation Library

The event-schema validation logic shared by `ingest-api` and `nightly-etl`, published as an npm
package rather than deployed anywhere itself.

- Type: `library`
- Repository / package registry / ticket scope: see `links` above
- Deployed to: nowhere — `environments` is intentionally empty; this is consumed as a package
  dependency, not run as a service
- Depends on: none
- Owner: Data platform team
