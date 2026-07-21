---
paik: "0.3"
kind: project
id: solstice-rewards
name: Solstice Rewards
lifecycle: active
owner:
  name: Product team
  ref: https://solstice-app.example/wiki/spaces/REWARDS/pages/1/Product+Team
description: >
  A customer loyalty/rewards mobile app. Used here to show PAIK from a product owner and
  designer's perspective, not just an engineering one - the project-level links carry delivery,
  product-brief, design, analytics, and roadmap pointers alongside the usual engineering ones.
links:
  - kind: jira-project
    purpose: delivery
    id: REW
    url: https://solstice-app.example/jira/software/projects/REW
  - kind: confluence
    purpose: product-brief
    url: https://solstice-app.example/wiki/spaces/REWARDS/pages/10/Product+Brief
  - kind: figma
    purpose: product-design
    url: https://www.figma.com/files/team/solstice-app/project/rewards-app
  - kind: analytics
    provider: amplitude
    purpose: product-metrics
    url: https://analytics.amplitude.com/solstice-app/rewards
  - kind: roadmap
    url: https://solstice-app.example/wiki/spaces/REWARDS/pages/11/Roadmap
components:
  - component.md
environments:
  - environments/dev.md
  - environments/prod.md
---

# Solstice Rewards

A customer loyalty/rewards mobile app: earn and redeem points, tiered perks, and push
notifications for offers.

## Where things live
- Delivery: Jira, project `REW` — see `links` above
- Product brief: Confluence — see `links` above
- Design: Figma — see `links` above
- Product metrics: Amplitude — see `links` above
- Roadmap: see `links` above

## Who's involved
Stakeholders, decision-makers, and the list of who's actually on the product/design/engineering
teams live on the Product Brief page in Confluence (linked above) — PAIK only carries the
`owner` team name and a pointer to where that's documented, the same as every other example in
this repo. There is no `participants.md` here or anywhere else in PAIK.

## Implementation
- Component: [Rewards App](component.md)

## Operations
- Environments: [dev](environments/dev.md), [prod](environments/prod.md)
