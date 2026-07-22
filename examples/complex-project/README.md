# Example: complex-project — Nimbus Commerce

The multi-service instance of the PAIK v0.4 standard: 3 services (frontend, orders-api,
catalog-api), 5 owning teams, 4 environments across 2 regions — all expressed with just
`project.md` + `components/*.md` + `environments/*.md`. Teams have no file of their own; each
component/environment carries its owner inline, and everything that used to be a separate
ticketing/wiki/repo/config document is now a typed `links[]` entry. Start at
[`paik/project.md`](paik/project.md).

See [`../simple-project/`](../simple-project/) for the minimal single-service version of the same
standard — same three document kinds, just one file instead of one-per-service/one-per-region.
