# PAIK Specification v0.4

PAIK (Public AI Knowledge Definition) is a tool-agnostic, Markdown-based standard for describing
a software project end-to-end — planning, implementation, and operations — by **linking** the
systems a team already uses instead of duplicating their content.

A PAIK document is never a copy of a Jira ticket, a Confluence page, or a database password. It
is a small, structured pointer: what system, which identifier, whose responsibility, and how to
reach it. The systems stay the source of truth; PAIK stays the map.

v0.3 was a deliberate reset from the earlier `2.x` line: rather than a document type per external
system (ticketing, wiki, API spec, repo, external service, config manager, team roster), PAIK
has three real entities — `project`, `component`, `environment` — and one generic, typed
`links[]` list that covers everything else. v0.4 keeps that model and aligns its common
frontmatter fields with the Open Knowledge Format so every PAIK document is also a valid OKF
concept — see section 2.

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
`component.md` (see sections 3-4).

Singular-file vs. directory-of-files is a scaling decision, not a spec violation: a one-service
project uses `component.md`; a multi-service project uses `components/orders-api.md`,
`components/catalog-api.md`, etc. Both are valid PAIK. Pick whichever matches how many instances
of that concern actually exist.

## 2. Relationship to Open Knowledge Format

PAIK is a strict, software-project-specific domain profile of the
[Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
— a Markdown + YAML-frontmatter knowledge-bundle format Google Cloud published in June 2026. OKF
defines a portable envelope: a directory tree of Markdown concept documents, each required to
carry nothing more than a non-empty `type` field. PAIK defines the semantics, closed schemas, and
cross-reference validation a software project's topology, ownership, and operations actually
need on top of that envelope.

| OKF | PAIK |
|---|---|
| General-purpose knowledge-bundle format | Software project map |
| Arbitrary, producer-chosen concept types | `project`, `component`, `environment` only |
| One required field: `type` | A closed, fully schema-enforced frontmatter per kind |
| Concept id = file path | Explicit, stable `id` field (see below) |
| Untyped Markdown links between concepts | `depends_on`, `links[].kind`, `component`/`environment` qualifiers |
| Consumers tolerate broken links | `tools/paik_validate.py` rejects them |
| A concept document can store knowledge directly | A PAIK document only ever points at the authoritative external source |

Every PAIK v0.4 document is, by construction, a valid OKF v0.1 concept: `type` is always a
non-empty string (`paik-project`, `paik-component`, or `paik-environment` — section 3), so any
`paik/` folder is on its own a conformant OKF bundle. `tools/check_okf_conformance.py` checks
exactly and only OKF's base rule; `tools/paik_validate.py` checks that plus everything else this
spec adds. See `examples/okf-compatible-project` for a worked, file-by-file walkthrough.

### Concept identity: OKF's path vs. PAIK's `id`

OKF's concept identity is always "the file's path within the bundle, with the `.md` suffix
removed" — there is no separate identity field at the OKF level. PAIK adds an explicit `id`
(section 3) because a stable identifier that survives a file move or a `component.md` →
`components/orders-api.md` reshape is what `depends_on` and the `component`/`environment` link
qualifiers (section 4) actually need to resolve against. The two commonly agree in spirit (a
file at `components/orders-api.md` usually has `id: orders-api`) but are formally different
mechanisms with different failure modes — a rename breaks the OKF concept id silently; PAIK's
`id` only changes when someone edits the `id` field, and `tools/paik_validate.py` catches a
resulting dangling reference either way.

### What PAIK does not adopt from OKF

- **`log.md`** — OKF's optional change-history file. PAIK relies on Git history for this
  instead, the same reasoning that keeps per-document `last_updated`/`last_verified` fields out
  of the common frontmatter.
- **A hand-maintained `index.md`** — OKF's optional directory listing. `project.md` is already
  PAIK's stable entry point (section 1); a second, redundant index would just be one more file
  to keep in sync.
- **OKF tooling or a Google Cloud dependency** — nothing in this spec or its validator depends
  on anything Google-specific; OKF is a plain-text format, not a service.
- **Opening PAIK's closed schemas** — an OKF consumer must tolerate unknown types and fields; a
  PAIK consumer may enforce a much stricter domain profile on top of that tolerance. Being a
  valid OKF bundle does not mean loosening `unevaluatedProperties: false` anywhere in `schema/`.
- **Moving Jira/Confluence content into OKF concepts** — PAIK still only ever *points at* those
  systems via `links[]` (section 4). OKF alignment changes how a PAIK document identifies
  itself, not the metadata-reference model the rest of this spec is built on.

## 3. Common frontmatter

Every `.md` file under `paik/` opens with YAML frontmatter. These keys are shared by every
document kind, and (aside from `paik`/`id`/`lifecycle`/`owner`/`links`/`extensions`, which are
PAIK-specific extensions OKF simply tolerates and preserves) map onto OKF's own base fields:

| Key           | Required?                              | Type   | Meaning                                                                 |
|---------------|-----------------------------------------|--------|--------------------------------------------------------------------------|
| `type`        | yes                                     | string | OKF concept type: `paik-project` \| `paik-component` \| `paik-environment` |
| `title`       | yes                                     | string | Human-readable name (OKF's `title`)                                     |
| `paik`        | yes                                     | string | Spec version this document conforms to (`"0.4"`)                        |
| `id`          | yes                                     | string | Stable slug, unique within the project (`kebab-case`) — see section 2 for how this differs from OKF's own concept identity |
| `lifecycle`   | yes                                     | string | `planning` \| `active` \| `maintenance` \| `sunset`                     |
| `description` | required on `project`, optional elsewhere | string | OKF-recommended single-sentence summary; `project.md` requires a fuller one-paragraph version — see section 8 |
| `owner`       | yes on `project`/`component`, optional on `environment` | object | `{ name, ref? }` — see below |
| `links`       | optional                               | array  | Typed pointers to everything external — see section 4                   |
| `extensions`  | optional                               | object | Free-form, namespaced fields for org-specific needs — see section 6     |

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
deliberate exception (see section 4).

## 4. The `links` convention

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

`kind` is the only required field on a link (this `kind` is a nested, PAIK-only field — unrelated
to a document's own top-level `type` from section 3). Everything else on a link (`url`, `id`,
`purpose`, `provider`, or any other key a particular kind needs, e.g. `format`, `protocol`,
`version`, `vendor`, `data_shared`) is open — unlike the rest of a PAIK document, a `links` item
is **not** closed against extra properties, because the entire point of this convention is not
needing a new schema every time a new kind of external system shows up.
`paik-spec/schema/common.schema.json` enforces only `kind: string, required`.

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

`paik-spec/LINKS.md` is a non-normative cookbook of which fields are worth setting on each of
these `kind` values in practice — nothing there is schema-enforced, it's a shared convention so
two projects shape the same `kind` the same way.

## 5. Cross-referencing convention

- Links between PAIK documents are relative Markdown links, e.g. `[Orders API](components/orders-api.md)`.
- Component and environment documents are referenced by whole file, not by anchor — one component
  or one environment per file (or per entry in a `components/`/`environments/` directory), so
  there is no slugified-heading anchor scheme to keep in sync.
- `project.md` is the entry point: it links out to every `component*` and `environment*` file
  that belongs to the project via the `components`/`environments` arrays. A reader (human or
  agent) should be able to reach any fact in the project within two hops of `project.md`.
- Links to *external* systems (the actual Jira board, the actual Grafana dashboard) are absolute
  URLs inside a `links[]` entry, never embedded API credentials or tokens.

## 6. Extensions

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
to put what it actually needs, instead of a new PAIK minor version per organization. This is also
exactly the mechanism an OKF consumer already expects: OKF producers may add arbitrary key-value
pairs beyond its own base fields, and OKF consumers preserve rather than reject them.

## 7. Secrets

PAIK documents may reference **where** configuration and secrets live (a `links[]` entry with
`kind: secrets`, an `environment.databases[].host_ref`) but must never contain actual secret
values, API keys, or passwords. This is independent of anything else in this spec: it's a hard
rule regardless of how a given `paik/` folder is otherwise classified or shared.

## 8. Document kinds

### `project` — `templates/project.md`
The entry point. `description` (one paragraph), `owner`, `links` (planning/wiki pointers that
apply project-wide, e.g. a shared Jira project or Confluence space), `components` (relative links
to every component document), `environments` (relative links to every environment document).

### `component` — `templates/components/component.md`
A deployable/runnable unit of the project (a service, library, or job) — the project graph node
an agent can actually traverse, rather than inferring the relationship between a repo, an API,
and a config from file naming alone. Key fields: `component_type` (`service` \| `library` \|
`job` \| `other`, named `component_type` rather than `type` so it doesn't collide with the
document's own OKF `type` from section 3), `owner`, `links` (repository, API(s)
provided/consumed, external services it calls, where its secrets live, ticket scopes, runbooks,
dashboards — all as typed `links[]` entries), `environments` (relative links to where this
component is deployed), `depends_on` (ids of other components this one depends on).

### `environment` — `templates/environments/environment.md`
One running instance of the system. Key fields: `purpose`, `app_url`, `health_endpoint`,
`databases` (array of `{ type, host_ref, component? }` — `host_ref` is a free-text pointer to
where connection details actually live, never a credential; `component` names which service
owns that database when the environment is shared by several), `access` (who/how, e.g. "VPN
required"). Status pages and deploy pipelines are `links[]` entries (`kind: status-page`,
`kind: deploy-pipeline`) rather than dedicated fields — tag each with `component: <id>` when an
environment is deployed to by more than one component, per section 4.

## 9. Versioning

Current documents are authored against `paik: "0.4"`. Backward-incompatible changes to required
fields bump the minor digit until the model stabilizes enough to commit to `1.0`; a document
always states the version it was authored against so tooling can detect drift.

## 10. Deferred / future work

Not part of this spec yet — tracked here so the gap is explicit rather than implied:

- A convention (or lightweight lint) for the `kind` vocabulary in `links[]` so tooling built
  against one PAIK project's link kinds transfers cleanly to another's, without re-introducing a
  closed enum.
- Full protocol modeling for `grpc`/`graphql`/`asyncapi`/`soap-wsdl` API `links` beyond a free-text
  `format`/`protocol` field (schema introspection, codegen hooks, etc.).
- Submitting the PAIK profile (or one of its examples) to the OKF repository as a worked
  software-project domain application, once the profile itself has had more real-world use.
