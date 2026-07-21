---
name: paik-bootstrap
description: Scaffold a new paik/ folder for a project from the PAIK templates in paik-spec/templates. Use when a project has no PAIK documentation yet, or the user asks to "set up PAIK", "adopt PAIK", or "add a paik folder" to a repo.
---

# paik-bootstrap

Scaffold a new `paik/` folder for a project that hasn't adopted PAIK yet.

## Steps

1. Locate `paik-spec/templates/` (in this repo, or wherever PAIK was vendored into the target
   project). Read `paik-spec/SPEC.md` first if you haven't already — it defines every field you
   are about to fill in. There are only three document kinds: `project`, `component`,
   `environment`.
2. Ask the user (or infer from the repo) for: project name/description, owner (a team name plus
   an optional link to where that team is documented in the org's own directory/wiki), the
   ticketing/knowledge-base/repo/API-spec systems actually in use (these become `links[]` entries,
   not separate files), the components/services and each one's owner, the list of environments,
   and where secrets/configuration are actually managed (also a `links[]` entry, `kind: secrets`).
3. Decide single-file vs. directory-per-concern shape (see SPEC.md section 1): one repo/one
   service stays single-file (`component.md`); multiple services use a directory
   (`components/*.md`). Look at `examples/simple-project` vs `examples/complex-project` for both
   shapes.
4. Copy the matching templates into `<target-repo>/paik/`, replacing every `<placeholder>` with
   real values. Do not invent URLs or identifiers — leave a clearly marked `TODO` if a value is
   genuinely unknown, never a plausible-looking fake one.
5. For each `links[]` entry, only `kind` is required — but fill in `url`/`id`/`provider` whenever
   you actually have them, since a link with just a `kind` isn't useful to anyone reading it back.
6. Validate frontmatter against `paik-spec/schema/*.schema.json` before reporting done.
7. Report which files were created and which fields still need a human to fill in.
