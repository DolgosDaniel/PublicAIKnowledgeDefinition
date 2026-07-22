# Example: monorepo-project — Vertex Platform

The instance of the PAIK v0.4 standard that shows a component is not the same thing as a
repository: `api-gateway`, `billing-service`, and `web-client` all point their `repository` link
at the same `url` (`github.com/vertex-robotics/platform`), each disambiguated with a `purpose`
naming its subpath (`apps/api-gateway`, `services/billing`, `apps/web-client`). Environments
carry one path-filtered `deploy-pipeline` link per component, tagged with `component`.

Start at [`paik/project.md`](paik/project.md).
