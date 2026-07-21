---
name: paik-bootstrap
description: Scaffold a new paik/ folder for a project from the PAIK templates in paik-spec/templates. Use when a project has no PAIK documentation yet, or the user asks to "set up PAIK", "adopt PAIK", or "add a paik folder" to a repo.
---

# paik-bootstrap

Scaffold a new `paik/` folder for a project that hasn't adopted PAIK yet.

## Steps

1. Locate `paik-spec/templates/` (in this repo, or wherever PAIK was vendored into the target
   project). Read `paik-spec/SPEC.md` first if you haven't already — it defines every field you
   are about to fill in.
2. Ask the user (or infer from the repo) for: project name/description, which ticketing/knowledge
   base/API-spec/source-repo systems are actually in use, the list of participants, the list of
   environments, and the configuration management tool.
3. Decide single-file vs. directory-per-concern shape (see SPEC.md section 1): one repo/one
   service stays single-file (`systems/ticketing.md`); multiple services use directories
   (`systems/source-repos/*.md`). Look at `examples/simple-project` vs `examples/complex-project`
   for both shapes.
4. Copy the matching templates into `<target-repo>/paik/`, replacing every `<placeholder>` with
   real values. Do not invent URLs or identifiers — leave a clearly marked `TODO` if a value is
   genuinely unknown, never a plausible-looking fake one.
5. Fill `owner_ref` fields only after `participants.md` exists, since every other document links
   into it.
6. Validate frontmatter against `paik-spec/schema/*.schema.json` before reporting done.
7. Report which files were created and which fields still need a human to fill in.
