# PAIK Specification v0.3

PAIK (Public AI Knowledge Definition) is a tool-agnostic, Markdown-based standard for describing
a software project end-to-end — planning, implementation, and operations — by **linking** the
systems a team already uses instead of duplicating their content.

A PAIK document is never a copy of a Jira ticket, a Confluence page, or a database password. It
is a small, structured pointer: what system, which identifier, whose responsibility, and how to
reach it. The systems stay the source of truth; PAIK stays the map.

v0.3 is a deliberate reset from the earlier `2.x` line: rather than a document type per external
system (ticketing, wiki, API spec, repo, external service, config manager, team roster), PAIK now
has three real entities — `project`, `component`, `environment` — and one generic, typed `links[]`
list that covers everything else.

## 1. Directory convention

Every PAIK-described project has a `paik/` folder (any name/location is fine, but tooling that
auto-discovers PAIK data looks for this name first) shaped like this:

```
paik/
  project.md                 required, exactly one - the entry point
  component.md                or components/*.md for multiple deployable/runnable units
  environments/
    <env-name>.md              one file per environment (dev.md, staging.md, prod.md, ...)
```

That's the whole shape. There is no `systems/`, `teams/`, `configuration/`, or
`external-services/` directory: ticketing, wikis, API specs, repos, external services, secrets
locations, and ownership all live inline as `owner` and `links[]` fields on `project.md` and
`component.md` (see sections 2-3).

Singular-file vs. directory-of-files is a scaling decision, not a spec violation: a one-service
project uses `component.md`; a multi-service project uses `components/orders-api.md`,
`components/catalog-api.md`, etc. Both are valid PAIK. Pick whichever matches how many instances
of that concern actually exist.

## 2. Common frontmatter

Every `.md` file under `paik/` opens with YAML frontmatter. These keys are shared by every
document kind:

| Key           | Required?                              | Type   | Meaning                                                                 |
|---------------|-----------------------------------------|--------|--------------------------------------------------------------------------|
| `paik`        | yes                                     | string | Spec version this document conforms to (`"0.3"`)                        |
| `kind`        | yes                                     | string | `project` \| `component` \| `environment`                               |
| `id`          | yes                                     | string | Stable slug, unique within the project (`kebab-case`)                   |
| `name`        | yes                                     | string | Human-readable name                                                     |
| `lifecycle`   | yes                                     | string | `planning` \| `active` \| `maintenance` \| `sunset`                     |
| `owner`       | yes on `project`/`component`, optional on `environment` | object | `{ name, ref? }` — see below |
| `links`       | optional                               | array  | Typed pointers to everything external — see section 3                   |
| `extensions`  | optional                               | object | Free-form, namespaced fields for org-specific needs — see section 5     |

`owner` is inline and deliberately thin — there is no separate team/roster document type. It's
`{ name: string, ref?: uri }`: a name (e.g. "Orders team") and an optional link to wherever the
org's own directory/wiki/org-chart documents that team. PAIK never lists individual people, emails,
or chat handles — that duplicates a system (an HR tool, a chat admin console, a Backstage
instance) that already owns that data more accurately than a Markdown file ever could. If several
documents share an owner, repeating `{ name, ref }` on each one is expected — it's a few bytes of
duplication in exchange for not inventing a file whose only job is to be pointed at.

Document-type-specific keys are defined by the matching schema in `schema/`. Every schema closes
itself against unknown/misspelled top-level fields (`unevaluatedProperties: false`), so typos and
stray keys fail validation instead of silently passing through — `links[]` items are the one
deliberate exception (see section 3).

## 3. The `links` convention

`links` is a flat array on `project.md` and `component.md` (and optionally `environment.md`).
Each entry is a typed pointer:

```yaml
links:
  - kind: jira-project
    id: NIM
    url: https://company.atlassian.net/jira/software/projects/NIM
  - kind: confluence
    purpose: architecture
    url: https://company.atlassian.net/wiki/spaces/NIM/pages/200/Architecture
  - kind: repository
    provider: gitlab
    url: https://gitlab.company.hu/nimbus/orders-api
  - kind: api
    provider: swaggerhub
    format: openapi
    url: https://app.swaggerhub.com/apis/nimbus/orders-api
```

`kind` is the only required field. Everything else on a link (`url`, `id`, `purpose`, `provider`,
or any other key a particular kind needs, e.g. `format`, `protocol`, `version`, `vendor`,
`data_shared`) is open — unlike the rest of a PAIK document, a `links` item is **not** closed
against extra properties, because the entire point of this convention is not needing a new schema
every time a new kind of external system shows up. `paik-spec/schema/common.schema.json` enforces
only `kind: string, required`.

`provider` is the *vendor/product* behind a link (`swaggerhub`, `github`, `pagerduty`, ...) — it
is never a protocol or file format. An `api` link's protocol and spec format are their own fields,
`protocol` (`grpc`, `graphql`, `rest`, `soap`, ...) and `format` (`openapi`, `asyncapi`, ...), so
that "who hosts this" and "what shape is this" stay independently answerable — e.g. a gRPC
contract hosted on SwaggerHub is `provider: swaggerhub, protocol: grpc`, not `provider: grpc`.

`purpose` disambiguates when the same `kind` appears more than once on a document (e.g. two
`confluence` links, one for the project home and one for an architecture doc; or `purpose:
provides` vs `purpose: consumes` on a component's `api` links).

`component` and `environment` disambiguate when a document is shared across more than one of
either — most commonly an `environment.md` deployed by several services, or (less commonly) a
`component.md` deployed to several environments with per-environment operational links. Put the
other one's `id` on the link so tooling can filter to exactly the component/environment it
concerns, instead of a link applying ambiguously to the whole shared document:

```yaml
links:
  - kind: deploy-pipeline
    component: orders-api
    url: https://github.com/nimbus-commerce/orders-api/actions/workflows/deploy-prod-eu.yml
  - kind: deploy-pipeline
    component: catalog-api
    url: https://github.com/nimbus-commerce/catalog-api/actions/workflows/deploy-prod-eu.yml
```

Omit `component`/`environment` on links that genuinely apply to the whole document (a project's
shared Jira project, an environment's overall status page).

Common `kind` values in practice (illustrative, not exhaustive — invent new ones freely):

- `repository` — where the code lives (GitHub, GitLab, Bitbucket, ...)
- `api` — a contract this component provides or consumes (SwaggerHub, a raw OpenAPI/AsyncAPI URL,
  a gRPC/GraphQL/SOAP endpoint, ...); use `purpose: provides` / `purpose: consumes` when a
  component needs both
- `jira-project`, `jira-epic`, `jira-component`, or the equivalent for another tracker
  (`linear-project`, `azure-boards-project`, `github-issues`, ...)
- `confluence`, or the equivalent for another wiki (`notion`, `sharepoint`, ...)
- `external-service` — a third-party dependency this project calls but does not operate (a
  payment processor, a mapping API, ...); put `vendor` and `data_shared` on the link itself
- `secrets` — where configuration/secrets are actually managed (a Vault path, an AWS Secrets
  Manager ARN, a `.env` convention) — the **location**, never a value
- `dashboard`, `runbook`, `pagerduty` (or another on-call tool), `status-page`,
  `deploy-pipeline`, `chat` — operational pointers; there is no separate "operations" document
  kind, these just live in `links[]`
- `other` — anything not yet listed; add a `provider` field to say what it actually is

## 4. Cross-referencing convention

- Links between PAIK documents are relative Markdown links, e.g. `[Orders API](components/orders-api.md)`.
- Component and environment documents are referenced by whole file, not by anchor — one component
  or one environment per file (or per entry in a `components/`/`environments/` directory), so
  there is no slugified-heading anchor scheme to keep in sync.
- `project.md` is the entry point: it links out to every `component*` and `environment*` file
  that belongs to the project via the `components`/`environments` arrays. A reader (human or
  agent) should be able to reach any fact in the project within two hops of `project.md`.
- Links to *external* systems (the actual Jira board, the actual Grafana dashboard) are absolute
  URLs inside a `links[]` entry, never embedded API credentials or tokens.

## 5. Extensions

Real projects always have one or two fields that don't belong in a shared standard — a
compliance tag, an internal cost-center code, a data-residency flag. Rather than growing the core
schema per organization, or letting ad-hoc top-level keys creep in and break the closed-schema
guarantee, those fields go under `extensions`, namespaced as `domain/key`:

```yaml
extensions:
  company.hu/data-owner: finance
  company.hu/regulation: pci-dss
```

`extensions` is a free-form object — PAIK doesn't validate its contents beyond it being a map.
This keeps the core small and stable while still giving every organization somewhere sanctioned
to put what it actually needs, instead of a new PAIK minor version per organization.

## 6. Secrets

PAIK documents may reference **where** configuration and secrets live (a `links[]` entry with
`kind: secrets`, an `environment.databases[].host_ref`) but must never contain actual secret
values, API keys, or passwords. This is independent of anything else in this spec: it's a hard
rule regardless of how a given `paik/` folder is otherwise classified or shared.

## 7. Document kinds

### `project` — `templates/project.md`
The entry point. `description` (one paragraph), `owner`, `links` (planning/wiki pointers that
apply project-wide, e.g. a shared Jira project or Confluence space), `components` (relative links
to every component document), `environments` (relative links to every environment document).

### `component` — `templates/components/component.md`
A deployable/runnable unit of the project (a service, library, or job) — the project graph node
an agent can actually traverse, rather than inferring the relationship between a repo, an API,
and a config from file naming alone. Key fields: `type` (`service` \| `library` \| `job` \|
`other`), `owner`, `links` (repository, API(s) provided/consumed, external services it calls,
where its secrets live, ticket scopes, runbooks, dashboards — all as typed `links[]` entries),
`environments` (relative links to where this component is deployed), `depends_on` (ids of other
components this one depends on).

### `environment` — `templates/environments/environment.md`
One running instance of the system. Key fields: `purpose`, `app_url`, `health_endpoint`,
`databases` (array of `{ type, host_ref, component? }` — `host_ref` is a free-text pointer to
where connection details actually live, never a credential; `component` names which service
owns that database when the environment is shared by several), `access` (who/how, e.g. "VPN
required"). Status pages and deploy pipelines are `links[]` entries (`kind: status-page`,
`kind: deploy-pipeline`) rather than dedicated fields — tag each with `component: <id>` when an
environment is deployed to by more than one component, per section 3.

## 8. Versioning

Current documents are authored against `paik: "0.3"`. Backward-incompatible changes to required
fields bump the minor digit until the model stabilizes enough to commit to `1.0`; a document
always states the version it was authored against so tooling can detect drift.

## 9. Deferred / future work

Not part of this spec yet — tracked here so the gap is explicit rather than implied:

- A convention (or lightweight lint) for the `kind` vocabulary in `links[]` so tooling built
  against one PAIK project's link kinds transfers cleanly to another's, without re-introducing a
  closed enum.
- Full protocol modeling for `grpc`/`graphql`/`asyncapi`/`soap-wsdl` API `links` beyond a free-text
  `format`/`protocol` field (schema introspection, codegen hooks, etc.).
