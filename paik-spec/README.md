# paik-spec

This directory contains the PAIK standard itself: the normative spec, the JSON Schemas that
validate each document type, and blank templates you copy into a new project — plus four
non-normative companions that don't change what's enforced, only how to use it well:
[`LINKS.md`](LINKS.md) (recommended fields per `links[]` `kind`), [`ROLES.md`](ROLES.md) (who
typically edits what), [`CHECKLIST.md`](CHECKLIST.md) (three "is this done?" tiers), and
[`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) (common validator errors, explained).

## Adopting PAIK in a project

1. Copy `templates/` into your repository as a `paik/` folder:

   ```
   your-repo/
     paik/
       project.md
       component.md
       environments/
         environment.md   (duplicate per environment: dev.md, staging.md, prod.md, ...)
   ```

   That's the whole shape — ticketing, wiki, API spec, repo, external services, secrets
   location, and ownership all live inline as `owner` and `links[]` fields on `project.md` and
   `component.md` rather than as separate files. See `SPEC.md` sections 3-4.

2. Fill in the frontmatter of each file. Every field is documented in `SPEC.md` and enforced by
   the matching schema in `schema/` — except `links[]` items, which only require a `kind`.
3. Delete/duplicate files that don't apply to your project shape — see `../examples/` for nine
   instances of this standard: single- and multi-service, still in planning, product/design-led,
   every `component_type`, a monorepo, third-party dependencies, a full operations map, and an
   explicit Open Knowledge Format conformance walkthrough.
4. Optionally wire up `../mcp/` (live access to the systems referenced) and `../skills/` (agent
   workflows that scaffold, maintain, sync, and health-check a `paik/` folder).

Read `SPEC.md` before authoring a new document type or extending the schema.
