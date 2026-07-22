---
paik: "0.4"
type: paik-project
id: beacon-tasks
title: Beacon Tasks
lifecycle: active
owner:
  name: Beacon team
  ref: https://beacon-tasks.example/wiki/spaces/BEACON/pages/1/Beacon+Team
description: >
  A small task-tracking app. Used here specifically to demonstrate that a PAIK v0.4 project is,
  by construction, also a conformant OKF v0.1 bundle - see the README next to this file for the
  concept-by-concept walkthrough.
links:
  - kind: jira-project
    id: BCN
    url: https://beacon-tasks.example/jira/software/projects/BCN
  - kind: confluence
    purpose: project-home
    url: https://beacon-tasks.example/wiki/spaces/BEACON/overview
components:
  - component.md
environments:
  - environments/dev.md
  - environments/prod.md
---

# Beacon Tasks

A small task-tracking app: create, assign, and complete tasks.

## Implementation
- Component: [Beacon Tasks](component.md)

## Operations
- Environments: [dev](environments/dev.md), [prod](environments/prod.md)
