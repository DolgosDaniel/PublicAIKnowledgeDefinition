# Example: external-dependencies-project — Aurora Logistics

The instance of the PAIK standard that demonstrates the `external-service` doc type: 5 services,
6 teams, 3 environments, and 2 third-party dependencies (Stripe for payments, Mapbox for
routing/geocoding) the project calls but does not operate. Start at
[`paik/project.md`](paik/project.md).

See [`../simple-project/`](../simple-project/) for the minimal single-service instance and
[`../complex-project/`](../complex-project/) for the region-scaled multi-service instance — this
example reuses the same doc types as both, plus `external-service` and the `component.
external_dependency_refs` / `project.external_services_ref` fields introduced in
`paik_version: "2.1"`.
