---
paik: "0.4"
type: paik-project
id: taskflow-lite
title: TaskFlow Lite
lifecycle: active
owner:
  name: TaskFlow Lite team
  ref: https://taskflow-inc.example/directory/teams/taskflow-lite
description: >
  A small, single-service web app for tracking personal to-do lists. One team, one repo,
  one API, two environments. Used here as the minimal instance of the PAIK standard.
links:
  - kind: jira-project
    id: TFL
    url: https://taskflow-inc.atlassian.net/jira/software/projects/TFL/boards/1
  - kind: confluence
    purpose: project-home
    url: https://taskflow-inc.atlassian.net/wiki/spaces/TFL/overview
  - kind: chat
    id: "#taskflow-lite"
  - kind: pagerduty
    url: https://taskflow-inc.pagerduty.com/schedules/taskflow-lite
components:
  - component.md
environments:
  - environments/dev.md
  - environments/prod.md
---

# TaskFlow Lite

A small, single-service web app for tracking personal to-do lists. One team, one repo, one API,
two environments — the minimal instance of the PAIK standard.

## Where things live
- Ticketing: Jira, project `TFL` — see `links` above
- Knowledge base: Confluence, `TFL` space — see `links` above
- Chat / on-call: `#taskflow-lite` / PagerDuty — see `links` above

## Implementation
- Component: [TaskFlow Lite](component.md)

## Operations
- Environments: [dev](environments/dev.md), [prod](environments/prod.md)
