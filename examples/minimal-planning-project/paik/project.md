---
paik: "0.3"
kind: project
id: northwind-loyalty
name: Northwind Loyalty
lifecycle: planning
owner:
  name: Northwind Labs product team
  ref: https://northwind-labs.example/wiki/spaces/PLANNING/pages/1/Loyalty+Program+Brief
description: >
  A proposed customer loyalty program - still in planning. Used here to show the minimal,
  honest instance of PAIK: no components or environments exist yet, and no URL or identifier is
  invented for anything that hasn't been created. Compare against examples/simple-project (an
  active, built-out single-service project) to see the same three-kind model at both ends of a
  project's life.
links:
  - kind: confluence
    purpose: product-brief
    url: https://northwind-labs.example/wiki/spaces/PLANNING/pages/1/Loyalty+Program+Brief
  - kind: jira-project
    purpose: "not created yet - ticketing will be set up once a build decision is made"
components: []
environments: []
---

# Northwind Loyalty

A proposed customer loyalty program for Northwind Labs' retail app: earn and redeem points
across purchases. Currently in the planning/discovery phase - no repository, service, or
environment exists yet.

## Where things live
- Product brief: Confluence — see `links` above
- Ticketing: not set up yet — see `links` above; this is deliberately left without a `url`
  rather than a placeholder one, since the project doesn't have a Jira project yet

## Implementation
None yet — `components` is intentionally empty. When a first service exists, add
`components/<id>.md` (or `component.md` for a single service) and list it here.

## Operations
None yet — `environments` is intentionally empty for the same reason.

## Why this is still valid PAIK
`components: []` and `environments: []` are valid, schema-passing values — a project doesn't
need anything running to start being described. The `jira-project` link demonstrates the other
half of the same principle: when something genuinely doesn't exist yet, say so in `purpose`
rather than inventing a URL that would fail validation (or worse, silently point at nothing).
