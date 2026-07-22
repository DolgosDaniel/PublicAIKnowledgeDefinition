# Who touches what in a `paik/` folder

This is a responsibility guide, not an access-control model — PAIK doesn't enforce any of this,
it's a convention for who typically edits which part of a `paik/` folder so changes land with the
person who actually has the context to make them correctly. See the optional
[`CODEOWNERS.example`](templates/CODEOWNERS.example) if you want to make some of it enforced by
your Git host's review rules instead of just documented here.

## Product owner
- Owns `project.md`: `description`, `lifecycle`, and the project-wide `links` (roadmap, delivery
  ticketing, product brief).
- Doesn't typically touch `component.md`/`environment.md` frontmatter directly — flags a needed
  change to whoever owns that component instead.

## Designer
- Owns the `figma`/design-related `links` entries on `project.md` (see
  `examples/cross-functional-product`).
- Same boundary as the product owner: the engineering-facing documents belong to engineering.

## Engineer
- Owns `component.md`/`components/*.md`: `component_type`, `repository`/`api` links,
  `depends_on`, `environments`, and the component's `secrets` link (the *location*, never a
  value).
- Adds new components to `project.md`'s `components` array when a new one is created — this is
  the step `paik_validate.py` catches if it's forgotten (see the "component exists but isn't
  listed" error in `paik-spec/TROUBLESHOOTING.md`).

## Operator / SRE
- Owns `environments/*.md`: `app_url`, `health_endpoint`, `databases`, `access`, and the
  operational `links` (`deploy-pipeline`, `dashboard`, `runbook`, `pagerduty`, `status-page`,
  `logs`, `slo`, `backup-restore` — see `examples/operations-ready-project`).
- Owns the `component`/`environment` qualifiers on a shared environment's `links[]`/`databases[]`
  entries, since getting those right requires knowing the actual deployment topology.

## Everyone
- `owner` is always a team, never an individual — PAIK does not name people anywhere in a
  document (see `SPEC.md` section 3). If you need to know who's actually on a team right now,
  follow `owner.ref` into the org's own directory/wiki; don't add a name to a PAIK document to
  answer that instead.
- Anyone can run `python tools/paik_validate.py <paik-dir>` before committing a change — it
  doesn't require write access to anything but the `paik/` folder itself.

## A note on enforcement

None of the above is checked by `paik_validate.py` or the schemas — a designer editing
`component.md` isn't a validation error, just a sign the change might be missing engineering
context. If your org wants this enforced rather than just documented, that's exactly what a
`CODEOWNERS` file is for; see the example below.
