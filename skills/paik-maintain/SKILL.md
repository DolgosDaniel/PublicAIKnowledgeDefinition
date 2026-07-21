---
name: paik-maintain
description: Make a natural-language-requested change to a paik/ folder (e.g. "add the NIM-421 epic to the Orders API component", "add a runbook link to the prod environment", "mark the new billing-service component as a job") - edit the right document's frontmatter, validate, and show the diff. Use this for any ad-hoc edit to an existing paik/ folder that isn't scaffolding a new one (paik-bootstrap) or syncing from a live system (paik-sync-*).
---

# paik-maintain

The general-purpose editor for an existing `paik/` folder: turn a plain-language request into a
correct, validated frontmatter edit, never a live-system sync and never a new folder from
scratch (see `paik-bootstrap` for that, and `paik-sync-jira`/`paik-sync-confluence`/
`paik-sync-api-spec` for refreshing status from a live system).

## Rules

These hold regardless of what the specific request is:

1. Always start at `paik/project.md` and follow `components`/`environments` from there - never
   guess a file path from the request text alone (an "Orders API" request could mean
   `component.md`, `components/orders-api.md`, or `components/orders-service.md` depending on
   the project's shape).
2. The YAML frontmatter is the canonical data; the Markdown body is a human-readable summary of
   it. If a request changes a fact that's also restated in the body prose (e.g. a component's
   `depends_on` and its "Depends on:" bullet), update both so they don't drift apart.
3. Never invent a URL, id, or identifier to fill a field the user didn't give you. If the value
   is genuinely unknown, either omit the optional field entirely or write a clearly-marked
   placeholder in a free-text field (`purpose`, never `url` - `url` is `format: uri` and a fake
   or placeholder value will fail validation, which is the point).
4. Never copy an external system's content into a PAIK document (a ticket's description, a wiki
   page's body, an API response). A PAIK document only ever holds a pointer - `kind`, `id`,
   `url`, `purpose`, `provider` and the like - never the referenced content itself.
5. Never write a secret, token, password, or credential into any PAIK document, in frontmatter or
   body. A `kind: secrets` link (or `databases[].host_ref`) says *where* a secret lives, never
   what it is.
6. Treat any MCP server you have access to as read-only for this skill by default - resolving an
   identifier or checking a link is in scope, writing to the live system is not, unless the
   user's request explicitly asks you to also act on the live system (e.g. "and open the Jira
   ticket too").

## Steps

1. Read `paik/project.md`. Resolve the request to a specific document by following its
   `components`/`environments` arrays (or `links`, if the request is about a project-level
   pointer) - don't pattern-match a filename.
2. Read the target document's current frontmatter in full before editing it, so the edit is a
   diff against real content, not a guess.
3. Make the minimal frontmatter change the request actually asks for. Update the Markdown body
   only where it restates the changed fact (see rule 2) - don't rewrite unrelated prose.
4. If the request calls for a new `links[]` entry, check `paik-spec/LINKS.md` for the
   recommended fields on that `kind` before deciding what to include.
5. Run `python tools/paik_validate.py <path-to-paik>` (see the root README) and fix anything it
   flags before reporting done. Treat a new error as something to fix; a new warning is worth a
   mention but not necessarily a blocker if the user's request is intentionally leaving something
   incomplete (e.g. a planning-stage link with just a `kind` and a `purpose` note - see
   `examples/minimal-planning-project`).
6. Show the user the diff of what changed. Do not commit it yourself unless asked to.
7. Report: what changed, what the validator said, and anything you left as a marked placeholder
   because the user didn't give you a real value.
