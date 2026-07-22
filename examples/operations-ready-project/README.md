# Example: operations-ready-project — Helios Payments

The instance of the PAIK v0.4 standard that shows a complete per-component operational map on a
single shared production environment: health check, deploy pipeline, dashboard, incident
runbook, backup/restore runbook, on-call, logs, and an SLO document for each of two components —
all as `links[]` entries tagged with `component:` (per SPEC.md section 4), with no dedicated
"operations" document kind. See [`paik-spec/LINKS.md`](../../paik-spec/LINKS.md) for the
recommended fields behind each `kind` used here.

Start at [`paik/project.md`](paik/project.md), then read
[`paik/environments/prod.md`](paik/environments/prod.md) for the operational map itself.
