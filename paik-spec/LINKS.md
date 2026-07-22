# PAIK Link-Kind Cookbook

This document is **non-normative** — it doesn't add anything to `paik-spec/schema/` and nothing
here is enforced beyond what `SPEC.md` section 4 already requires (`kind` is the only mandatory
field on a `links[]` entry). What follows is a set of recommendations for the fields worth
including on the `kind` values that show up repeatedly in practice, so that two PAIK projects
authored by different teams end up shaping the same `kind` the same way, without a schema forcing
either of them to.

If you need a `kind` that isn't here, invent one — see SPEC.md section 4's own note that the list
there is illustrative, not exhaustive. If it turns out to be broadly useful, it's worth proposing
an addition to this file.

## How to read the tables

- **Recommended fields** are what a link of that `kind` typically needs to be useful to a reader
  or a tool — not a requirement. `kind` alone is always valid; everything past it is a judgment
  call about what's actually worth writing down.
- `component` / `environment` (see SPEC.md section 4) apply to *any* `kind`, whenever the
  document carrying the link is shared across more than one component or environment. They're
  omitted from the per-kind tables below since they're not specific to any one kind.
- `purpose` also applies to any `kind` and is omitted from the tables for the same reason — use
  it whenever a `kind` appears more than once on the same document and the entries need
  disambiguating (two `confluence` links, two `api` links with different `purpose: provides` /
  `purpose: consumes`, ...) or whenever a short human-readable label helps (see the `repository`
  row below for the monorepo case).

## Planning & delivery

| `kind`          | Recommended fields                          | Notes |
|-----------------|----------------------------------------------|-------|
| `jira-project`  | `id`, `url`                                   | One per ticketing system the project/component uses; `id` is the project key. |
| `jira-epic`     | `id`, `url`                                   | Scope a component's work to an epic instead of (or in addition to) a project. |
| `jira-component`| `id`, `url`                                   | Scope a component's work to a Jira component within a shared project. |
| `confluence`    | `purpose`, `url`                              | `purpose` disambiguates when a project has more than one (e.g. `project-home` vs `architecture`). |
| `figma`         | `purpose`, `url`                              | Product/UX design files - `purpose: product-design` or similar. |
| `analytics`     | `provider`, `purpose`, `url`                  | `provider`: `amplitude`, `mixpanel`, `google-analytics`, ... |
| `roadmap`       | `url`                                         | A roadmap tool or a Confluence/Notion page - use `provider` if it's a dedicated tool. |

Participants, stakeholders, and decision-makers are **never** a PAIK `links[]` entry or field -
they live in whatever system the project already uses (Confluence, a wiki page, a roster) and
`owner.ref` or a `confluence`/`roadmap` link points there. PAIK does not have, and will not grow,
a `participants`-shaped kind.

## Implementation

| `kind`             | Recommended fields                                    | Notes |
|--------------------|--------------------------------------------------------|-------|
| `repository`       | `provider`, `url`, `purpose`                            | `purpose` names the subpath when several components share one monorepo URL, e.g. `purpose: packages/orders-api` - see `examples/monorepo-project`. |
| `api`              | `purpose` (`provides`/`consumes`), `provider`, `protocol`, `format`, `id`, `url` | `provider` is the vendor/host (`swaggerhub`, ...); `protocol` (`grpc`, `graphql`, `rest`, `soap`) and `format` (`openapi`, `asyncapi`) describe the contract shape - never put a protocol/format value in `provider`. |
| `package-registry` | `provider`, `id`, `url`                                 | For a `library` component with no `environments` - `provider`: `npm`, `pypi`, `maven`, ... |
| `secrets`          | `provider`, `purpose`, `url`                            | The **location** configuration/secrets are managed, never a value. `purpose` is a good place for a key-naming convention or path pattern. |
| `external-service` | `vendor`, `url`, `docs_url`, `status_page`, `data_shared`, `secret_ref` | A third-party dependency the component calls but doesn't operate. `secret_ref` is a free-text pointer to where that vendor's credential lives - never the credential. |

## Operations

There is no dedicated "operations" document kind - all of the following are `links[]` entries on
a `component.md` or `environment.md`, tagged with `component`/`environment` per SPEC.md section 4
whenever the document is shared. See `examples/operations-ready-project` for all of these used
together on one environment shared by two components.

| `kind`            | Recommended fields                    | Notes |
|-------------------|-----------------------------------------|-------|
| `dashboard`       | `provider`, `purpose`, `url`            | A metrics/monitoring dashboard (Grafana, Datadog, a BI tool, ...). |
| `runbook`         | `purpose`, `url`                        | `purpose` distinguishes an incident runbook from e.g. a backup/restore procedure. |
| `pagerduty`       | `url`                                    | Or the equivalent for another on-call tool - the `kind` itself names the tool. |
| `status-page`     | `url`                                    | |
| `deploy-pipeline` | `url`, `purpose`                        | `purpose` is a good place for approval requirements or (for a scheduled job) a cron expression. |
| `logs`            | `provider`, `url`                       | Where to query logs for this component/environment (CloudWatch, Datadog, Loki, ...). |
| `slo`             | `url`                                    | The SLO/SLA document - usually a Confluence/Notion page, not a PAIK document. |
| `backup-restore`  | `url`                                    | The backup/restore runbook, if it's kept separate from the incident runbook. |

## Extending this cookbook

Adding a row here should never require a spec or schema change - that's the entire point of
`links[]` being open. If a `kind` needs a *required* field or cross-document validation beyond
what a recommendation can express, that's a sign it might deserve a first-class field instead
(the way `component`/`environment`/`depends_on` graduated out of being link-only conventions) -
raise it against `SPEC.md` section 10, not by trying to force `links[]` items closed.
