---
paik: "0.4"
type: paik-project
id: dataforge-analytics
title: DataForge Analytics
lifecycle: active
owner:
  name: Data platform team
  ref: https://dataforge.example/wiki/spaces/DATA/pages/1/Data+Platform+Team
description: >
  An internal analytics platform: an ingest API, a shared validation library, a nightly ETL job,
  and a no-code reporting dashboard. Used here to show all four component.type values in one
  project - most PAIK projects aren't just a fleet of HTTP services.
links:
  - kind: jira-project
    id: DATA
    url: https://dataforge.example/jira/software/projects/DATA
  - kind: confluence
    purpose: project-home
    url: https://dataforge.example/wiki/spaces/DATA/overview
components:
  - components/ingest-api.md
  - components/shared-validation-lib.md
  - components/nightly-etl.md
  - components/reporting-dashboard.md
environments:
  - environments/dev.md
  - environments/prod.md
---

# DataForge Analytics

An internal analytics platform. Four components, four different `type` values:

- [Ingest API](components/ingest-api.md) — `service`, the only one with a normal HTTP
  request/response lifecycle.
- [Shared Validation Library](components/shared-validation-lib.md) — `library`, never deployed
  anywhere itself (`environments: []`), consumed by the other two.
- [Nightly ETL](components/nightly-etl.md) — `job`, runs on a schedule rather than serving
  requests.
- [Reporting Dashboard](components/reporting-dashboard.md) — `other`, a hosted no-code BI tool
  with no repository of its own.

## Operations
- Environments: [dev](environments/dev.md), [prod](environments/prod.md)
