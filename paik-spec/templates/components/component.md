---
paik: "0.4"
type: paik-component
id: <component-slug>
title: <Component Name>
lifecycle: active
owner:
  name: <Owning team name>
  ref: <optional link to the team in your org's own directory/wiki>
component_type: service # service | library | job | other
links:
  - kind: repository
    provider: github # or gitlab, bitbucket, ...
    url: <https://.../repo>
  - kind: api
    purpose: provides # or "consumes" for an API this component calls but doesn't own
    provider: swaggerhub # the vendor/host, e.g. swaggerhub - never a protocol/format
    format: openapi # or asyncapi; use protocol: grpc / graphql / soap instead for non-REST APIs
    url: <https://.../api-spec>
  - kind: jira-epic # or jira-component, linear-project, ...
    id: <PROJ-123>
    url: <https://.../PROJ-123>
environments:
  - ../environments/dev.md
  - ../environments/prod.md
depends_on: []
---

# <Component Name>

<One paragraph: what this component does.>

- Type: `service`
- Repository / API / ticket scope: see `links` above
- Deployed to: [dev](../environments/dev.md), [prod](../environments/prod.md)
- Depends on: <other components, or "none">
- Owner: <Owning team name>
