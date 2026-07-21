---
paik: "0.3"
kind: project
id: <project-slug>
name: <Project Name>
lifecycle: planning # planning | active | maintenance | sunset
owner:
  name: <Owning team name>
  ref: <optional link to the team in your org's own directory/wiki>
description: >
  One paragraph: what this project is, who it's for, and what problem it solves.
links:
  - kind: jira-project # or linear-project, azure-boards-project, github-issues, ...
    id: <PROJ>
    url: <https://.../projects/PROJ>
  - kind: confluence # or notion, sharepoint, ...
    purpose: project-home
    url: <https://.../spaces/PROJ>
components:
  - component.md # or components/*.md for multiple
environments:
  - environments/dev.md
  - environments/prod.md
---

# <Project Name>

<One paragraph: what this project is, who it's for, and what problem it solves.>

## Where things live
- Ticketing: [<Ticketing project name>](<https://.../projects/PROJ>)
- Knowledge base: [<Space name>](<https://.../spaces/PROJ>)

## Implementation
- Component(s): [<Component Name>](component.md)

## Operations
- Environments: [dev](environments/dev.md), [prod](environments/prod.md)
