# Example: external-dependencies-project — Aurora Logistics

The instance of the PAIK v0.4 standard that demonstrates third-party dependencies: 5 services,
6 owning teams, 3 environments, and 2 third-party dependencies (Stripe for payments, Mapbox for
routing/geocoding) the project calls but does not operate. Start at
[`paik/project.md`](paik/project.md).

Stripe and Mapbox are not separate documents — they're `kind: external-service` entries inside
`links[]` on the one component that actually calls each vendor (`orders-service`,
`routing-service`), carrying `vendor`, `docs_url`, `status_page`, `contract_ref`, and
`data_shared` right on the link itself.

See [`../simple-project/`](../simple-project/) for the minimal single-service instance and
[`../complex-project/`](../complex-project/) for the region-scaled multi-service instance — this
example reuses the same three document kinds as both, just with a richer dependency graph and
one extra `links` kind.
