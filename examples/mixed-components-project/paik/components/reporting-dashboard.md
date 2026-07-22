---
paik: "0.4"
type: paik-component
id: reporting-dashboard
title: Reporting Dashboard
lifecycle: active
owner:
  name: Data platform team
  ref: https://dataforge.example/wiki/spaces/DATA/pages/1/Data+Platform+Team
component_type: other
links:
  - kind: dashboard
    provider: retool
    url: https://dataforge.retool.com/apps/reporting
  - kind: jira-component
    id: reporting-dashboard
    url: https://dataforge.example/jira/software/projects/DATA?component=reporting-dashboard
environments:
  - ../environments/prod.md
depends_on: []
extensions:
  dataforge.example/no-code: true
---

# Reporting Dashboard

An internally-facing analytics dashboard built in Retool, a hosted no-code tool — there is no
repository, CI pipeline, or codebase for this component; the app is authored and deployed
entirely inside the vendor's own editor.

- Type: `other` (no closer fit than `service`/`library`/`job` - it isn't code)
- No `repository` link on purpose; see `links` for the hosted dashboard itself
- Deployed to: [prod](../environments/prod.md) — the vendor's single hosted instance is the only
  "environment" that exists
- Depends on: none
- Owner: Data platform team
