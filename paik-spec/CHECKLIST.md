# Is this `paik/` folder "done"?

There's no single right answer — a project in planning and a payments platform in production are
both valid PAIK. This is a documentation checklist for three honest levels, not a new schema
profile or a `lifecycle` value; nothing here is enforced by `paik_validate.py` beyond what the
schemas already require (a `components`/`environments` array is allowed to be empty, full stop).
Use it to describe where a project actually is, not to gate anything.

## Minimal
- [ ] `project.md` exists, validates, and has a real `owner` (`name` +, ideally, `ref`).
- [ ] At least one `links[]` entry beyond just `kind` — a Jira project, a Confluence page,
      anything that's actually true today.
- [ ] `components`/`environments` are either populated or honestly empty (`[]`) — see
      `examples/minimal-planning-project`.

## Development-ready
- [ ] Every component that exists has its own `component.md`/`components/*.md`, listed in
      `project.md`'s `components`.
- [ ] Each component's `repository` link resolves to a real repo (or, for a monorepo, carries a
      `purpose` naming its subpath — see `examples/monorepo-project`).
- [ ] Each component's `depends_on` reflects its actual internal dependencies, and
      `python tools/paik_validate.py` reports no unknown-dependency or cycle errors.
- [ ] Each component is deployed to at least one `environments/*.md` entry (or, for a `library`,
      has an empty `environments: []` on purpose — see `examples/mixed-components-project`).

## Operations-ready
- [ ] Every environment a component runs in has: `health_endpoint` (or a per-component
      `kind: health-check` link when the environment serves more than one app - see
      `examples/operations-ready-project`), a `deploy-pipeline` link, and an `access` statement.
- [ ] Every component with an owning on-call rotation has a `pagerduty` (or equivalent) link,
      tagged with `component:` if the environment is shared.
- [ ] A `secrets` link exists wherever configuration/credentials are actually managed - never a
      value, just the location.
- [ ] Dashboards, runbooks, and logs links exist for anything a real incident would need -
      `dashboard`, `runbook`, `logs` `kind`s, tagged per component when shared.

## What "done" doesn't mean
None of this requires a new component/environment or a heavier schema — every checkbox above is
satisfied with fields the v0.4 schemas already have room for. If you find yourself wanting a
field that doesn't fit anywhere, that's `SPEC.md` section 10 (deferred work) or
`paik-spec/LINKS.md` (a new `kind`), not a reason to add a new document type.
