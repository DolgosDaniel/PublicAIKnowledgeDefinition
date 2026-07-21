# PAIK Specification v1

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
  participants.md            required, exactly one (a heading per person; large orgs may
                              split into participants/*.md + an index, see examples/complex-project)
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
| `paik_version` | string | Spec version this document conforms to (`"1.0"`)                        |
| `doc_type`     | string | One of: `project`, `ticketing-system`, `knowledge-base`, `api-spec`, `source-repo`, `participants`, `environment`, `configuration` |
| `id`           | string | Stable slug, unique within the project (`kebab-case`)                   |
| `name`         | string | Human-readable name                                                     |
| `status`       | string | `planning` \| `active` \| `maintenance` \| `sunset`                     |
| `last_updated` | date   | `YYYY-MM-DD`, updated whenever the document changes                     |
| `owner_ref`    | string | Link into `participants.md`, e.g. `participants.md#alice-kovacs`         |

Document-type-specific keys are defined by the matching schema in `schema/`. Unknown systems
(a ticketing tool, wiki, or API catalog not in the enum) use `type: other` plus a free-form
`custom_fields` map — never leave the schema to invent a one-off doc type.

## 3. Cross-referencing convention

- Links between PAIK documents are relative Markdown links with anchors:
  `[Alice Kovacs](../participants.md#alice-kovacs)`.
- Anchors are the slugified `name` of the row/section being referenced (GitHub-style: lowercase,
  spaces to hyphens).
- `project.md` is the entry point: it links out to every `systems/*`, `participants.md`,
  `environments/*`, and `configuration*` file that belongs to the project. A reader (human or
  agent) should be able to reach any fact in the project within two hops of `project.md`.
- Links to *external* systems (the actual Jira board, the actual Grafana dashboard) are absolute
  URLs in the frontmatter (`base_url`, `board_url`, `status_page`, ...), never embedded API
  credentials or tokens.

## 4. Secrets policy

PAIK documents may reference **where** configuration and secrets live (a Vault path, an env var
name, a Secrets Manager ARN) but must never contain actual secret values. This is what makes a
`paik/` folder safe to commit to a public or shared repo — the reason for the project's name.

## 5. Document types

### `project` — `templates/project.md`
The entry point. Name, one-paragraph description, lifecycle `status`, and links to every other
document in the project.

### `ticketing-system` — `templates/systems/ticketing.md`
Where planning/work-tracking happens. Key fields: `type` (`jira` \| `azure-boards` \| `linear` \|
`github-issues` \| `other`), `base_url`, `project_key`, `board_url`.

### `knowledge-base` — `templates/systems/knowledge-base.md`
Where design docs/runbooks live. Key fields: `type` (`confluence` \| `notion` \| `sharepoint` \|
`other`), `base_url`, `space_key`, `root_page_url`.

### `api-spec` — `templates/systems/api-spec.md`
The contract a service exposes. Key fields: `type` (`swaggerhub` \| `stoplight` \| `redocly` \|
`openapi-file` \| `other`), `base_url`, `api_id`, `version`, `spec_url`, `served_by_env` (a map
of environment id → spec version actually deployed there).

### `source-repo` — `templates/systems/source-repo.md`
Where the code lives. Key fields: `type` (`github` \| `gitlab` \| `bitbucket` \| `other`), `url`,
`default_branch`, `ci_pipeline_url`.

### `participants` — `templates/participants.md`
A list of everyone with a stake in the project, one heading per person (so
`participants.md#alice-kovacs`-style anchors resolve): role, team, contact, on-call link,
timezone. `owner_ref` fields throughout the rest of the project point back into this file.

### `environment` — `templates/environments/environment.md`
One running instance of the system. Key fields: `app_url`, `health_endpoint`, `status_page`,
`database` (type + host reference, never a credential), `deploy_pipeline_ref`, `config_ref`,
`access` (who/how, e.g. VPN required).

### `configuration` — `templates/configuration.md`
How config and secrets are managed. Key fields: `tool` (`vault` \| `aws-secrets-manager` \|
`consul` \| `dotenv` \| `spring-cloud-config` \| `helm-values` \| `other`), `location`, key-naming
convention, per-environment mapping, `rotation_policy_ref`, `feature_flag_system`.

## 6. Versioning

This is `paik_version: "1.0"`. Backward-incompatible changes to required fields bump the major
version; new optional fields bump the minor version. A document always states the version it was
authored against so tooling can detect drift.
