# paik-spec

This directory contains the PAIK standard itself: the normative spec, the JSON Schemas that
validate each document type, and blank templates you copy into a new project.

## Adopting PAIK in a project

1. Copy `templates/` into your repository as a `paik/` folder:

   ```
   your-repo/
     paik/
       project.md
       systems/
         ticketing.md
         knowledge-base.md
         api-spec.md
         source-repo.md
       component.md
       team.md
       environments/
         environment.md   (duplicate per environment: dev.md, staging.md, prod.md, ...)
       configuration.md
   ```

   Projects that depend on third-party services they don't operate (a payment processor, a
   mapping API, ...) can optionally add `external-service.md` (or `external-services/*.md`) —
   see `SPEC.md` section 5. Omit it entirely if there are none.

2. Fill in the frontmatter of each file. Every field is documented in `SPEC.md` and enforced by
   the matching schema in `schema/`.
3. Delete/duplicate files that don't apply to your project shape — see `../examples/` for a
   single-service and a multi-service instance of this same standard.
4. Optionally wire up `../mcp/` (live access to the systems referenced) and `../skills/` (agent
   workflows that read/refresh a `paik/` folder).

Read `SPEC.md` before authoring a new document type or extending the schema.
