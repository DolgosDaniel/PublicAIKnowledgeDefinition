# PAIK Specification v2

PAIK (Public AI Knowledge Definition) is a tool-agnostic, Markdown-based standard for describing
a software project end-to-end — planning, implementation, and operations — by **linking** the
systems a team already uses instead of duplicating their content.

A PAIK document is never a copy of a Jira ticket, a Confluence page, or a database password. It
is a small, structured pointer: what system, which identifier, whose responsibility, and how to
reach it. The systems stay the source of truth; PAIK stays the map.

## 1. Directory convention

Every PAIK-described project has a `paik/` folder (any name/location is fine, but tooling that
auto-discovers PAIK data looks for this name first) shaped like this:

```
paik/
  project.md                 required, exactly one
  systems/
    ticketing.md              or ticketing/*.md if there's more than one ticketing system
    knowledge-base.md
    api-spec.md                or api-specs/*.md for multiple APIs/services
    source-repo.md             or source-repos/*.md for multiple repos/services
  component.md                or components/*.md for multiple services (one per
                              deployable/runnable unit - see section 5)
  team.md                     required, at least one (team.md for a single team, or
                              teams/*.md for multiple teams)
  environments/
    <env-name>.md              one file per environment (dev.md, staging.md, prod.md, ...)
  configuration.md           or configuration/*.md for multi-service configs
```

Singular-file vs. directory-of-files is a scaling decision, not a spec violation: a one-service
project uses `systems/api-spec.md`; a multi-service project uses `systems/api-specs/orders.md`,
`systems/api-specs/catalog.md`, etc. Both are valid PAIK. Pick whichever matches how many
instances of that concern actually exist.

## 2. Common frontmatter

Every `.md` file under `paik/` opens with YAML frontmatter. These keys are required on every
document type, regardless of category:

| Key            | Type   | Meaning                                                                 |
|----------------|--------|--------------------------------------------------------------------------|
| `paik_version` | string | Spec version this document conforms to (`"2.0"`)                        |
| `doc_type`     | string | One of: `project`, `ticketing-system`, `knowledge-base`, `api-spec`, `source-repo`, `component`, `team`, `environment`, `configuration` |
| `id`           | string | Stable slug, unique within the project (`kebab-case`)                   |
| `name`         | string | Human-readable name                                                     |
| `status`       | string | `planning` \| `active` \| `maintenance` \| `sunset`                     |
| `last_updated` | date   | `YYYY-MM-DD`, updated whenever the document's content changes           |
| `owner_ref`    | string | Link to the owning team's document, e.g. `team.md` or `teams/orders.md` |
| `visibility`   | string | `public` \| `internal` \| `confidential` — see section 4                |

One optional key is available on every document type: `last_verified` (date) — the last time
this document's *external* links/references were confirmed to still resolve. It's distinct from
`last_updated`: content edits are Git history and don't need a dedicated field, but "is this
still accurate" is not derivable from Git and is worth tracking explicitly.

Document-type-specific keys are defined by the matching schema in `schema/`. Unknown systems
(a ticketing tool, wiki, or API catalog not in the enum) use `type: other` plus a required
`custom_fields` map — never leave the schema to invent a one-off doc type. Every schema closes
itself against unknown/misspelled fields (`unevaluatedProperties: false`), so typos and stray
keys fail validation instead of silently passing through.

## 3. Cross-referencing convention

- Links between PAIK documents are relative Markdown links, e.g. `[Orders team](../team.md)` or
  `[Orders team](../teams/orders.md)`.
- Team and component documents are referenced by whole file, not by anchor — one team or one
  component per file (or per entry in a `teams/`/`components/` directory), so there is no
  slugified-heading anchor scheme to keep in sync.
- `project.md` is the entry point: it links out to every `systems/*`, `component*`, `team*`,
  `environments/*`, and `configuration*` file that belongs to the project. A reader (human or
  agent) should be able to reach any fact in the project within two hops of `project.md`.
- Links to *external* systems (the actual Jira board, the actual Grafana dashboard) are absolute
  URLs in the frontmatter (`base_url`, `board_url`, `status_page`, ...), never embedded API
  credentials or tokens.

## 4. Secrets and visibility policy

PAIK documents may reference **where** configuration and secrets live (a Vault path, an env var
name, a Secrets Manager ARN) but must never contain actual secret values. This is necessary but
not sufficient for treating a `paik/` folder as publishable: a document can contain zero secrets
and still carry on-call links, chat channel names, internal hostnames, health-endpoint URLs,
database topology, or deploy-pipeline details that are not meant for a public audience.

That's what the required `visibility` field is for — an explicit, per-document, human-reviewed
statement of who this document is safe to share with:

- `public` — safe to publish as-is (e.g. a public API spec pointer).
- `internal` — fine inside the org, not for a public repo (most operational documents:
  `team.md`, `environment.md`, `configuration.md`).
- `confidential` — restrict further even inside the org.

`visibility` replaces an implicit "no password = safe" assumption with a decision someone
actually has to make per document.

## 5. Document types

### `project` — `templates/project.md`
The entry point. Name, one-paragraph description, lifecycle `status`, and links to every other
document in the project (`systems`, `team_ref`, `components_ref`, `environments_ref`,
`configuration_ref`).

### `ticketing-system` — `templates/systems/ticketing.md`
Where planning/work-tracking happens. Key fields: `type` (`jira` \| `azure-boards` \| `linear` \|
`github-issues` \| `other`), `base_url`, `project_key`, `board_url`.

### `knowledge-base` — `templates/systems/knowledge-base.md`
Where design docs/runbooks live. Key fields: `type` (`confluence` \| `notion` \| `sharepoint` \|
`other`), `base_url`, `space_key`, `root_page_url`.

### `api-spec` — `templates/systems/api-spec.md`
The contract a service exposes. Key fields: `type` (`swaggerhub` \| `stoplight` \| `redocly` \|
`openapi-file` \| `grpc` \| `graphql` \| `asyncapi` \| `soap-wsdl` \| `other`), `base_url`,
`api_id`, `version`, `spec_url`, `served_by_env` (a map of environment id → spec version
actually deployed there).

### `source-repo` — `templates/systems/source-repo.md`
Where the code lives. Key fields: `type` (`github` \| `gitlab` \| `bitbucket` \| `other`), `url`,
`default_branch`, `ci_pipeline_url`.

### `component` — `templates/components/component.md`
A deployable/runnable unit of the project (a service, library, or job) and the single
structured node that ties its repository, API, environments, configuration, team, and
dependencies together — the project graph node an agent can actually traverse, rather than
inferring the relationship between a repo, an API, and a config from file naming alone. Key
fields: `type` (`service` \| `library` \| `job` \| `other`), `repository_ref`,
`provides_api_refs`, `consumes_api_refs`, `environment_refs`, `configuration_ref`, `depends_on`
(other components), `ticket_scopes` (ticketing-system epics/components this component's work is
filed under).

### `team` — `templates/team.md`
The group that owns a component, system, or environment. Deliberately thin: `description`,
`chat_channel`, `on_call_ref`, and an optional `directory_ref` pointing at the org's actual
people directory. A team document never lists individual names, emails, or chat handles — the
org's HR system, Backstage instance, or chat admin console stays the source of truth for who is
on the team, the same way PAIK never copies a Jira ticket's content. `owner_ref` fields
throughout the rest of the project point at a team document.

### `environment` — `templates/environments/environment.md`
One running instance of the system. Key fields: `app_url`, `health_endpoint`, `status_page`,
`databases` (array of type + host reference, never a credential), `deploy_pipeline_ref`,
`config_ref`, `access` (who/how, e.g. VPN required).

### `configuration` — `templates/configuration.md`
How config and secrets are managed. Key fields: `tool` (`vault` \| `aws-secrets-manager` \|
`consul` \| `dotenv` \| `spring-cloud-config` \| `helm-values` \| `other`), `location`, key-naming
convention, per-environment mapping, `rotation_policy_ref`, `feature_flag_system`.

## 6. Versioning

This is `paik_version: "2.0"`. Backward-incompatible changes to required fields bump the major
version; new optional fields bump the minor version. A document always states the version it was
authored against so tooling can detect drift.

### Changelog

- **2.0** — Removed the `participants` document type and `participants.md`/`participants_ref`
  (it duplicated PII that a real org directory already owns). Added `team` (thin, no personal
  data) as the new target of `owner_ref`, and `component` as a first-class entity tying a
  service's repo/API/environments/configuration/team/dependencies together. Added required
  `visibility` and optional `data_classification` and `last_verified` common fields. Closed
  every schema against unknown fields (`unevaluatedProperties: false`) and made `custom_fields`
  actually required when a `type`/`tool` is `other`. Widened `api-spec.type` to include `grpc`,
  `graphql`, `asyncapi`, `soap-wsdl`.
- **1.0** — Initial standard.

## 7. Deferred / future work

Not part of this spec yet — tracked here so the gap is explicit rather than implied:

- A `paik validate` CLI (JSON Schema validation, file/anchor-reference resolution, ID
  uniqueness, owner/component graph checks) and CI wiring for it.
- A Backstage Software Catalog import/export adapter — Backstage's `Component`/`API`/`Resource`/
  `System`/`Group`/`User` model is the closest existing standard, and a converter both ways
  would let PAIK act as a lightweight, repository-local profile usable with or without
  Backstage.
- Full protocol modeling for `grpc`/`graphql`/`asyncapi`/`soap-wsdl` API specs beyond the type
  enum (schema introspection, codegen hooks, etc.).
- An operations-facing schema: runbooks, monitoring/dashboards/alerts, SLI/SLO/SLA, incident and
  change management, backup/restore and RTO/RPO.
