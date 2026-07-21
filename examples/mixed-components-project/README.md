# Example: mixed-components-project — DataForge Analytics

The instance of the PAIK v0.3 standard that exercises every `component.type` value, since the
other examples might otherwise leave the impression that every component is an HTTP service:

- `ingest-api` — `service`, the familiar shape.
- `shared-validation-lib` — `library`, `environments: []` (never deployed, consumed as a
  package dependency via `depends_on`).
- `nightly-etl` — `job`, a scheduled batch process (`links[].schedule` on its `deploy-pipeline`
  entry - a free-form field, since `links[]` items aren't closed).
- `reporting-dashboard` — `other`, a hosted no-code BI tool with no repository at all.

Start at [`paik/project.md`](paik/project.md).
