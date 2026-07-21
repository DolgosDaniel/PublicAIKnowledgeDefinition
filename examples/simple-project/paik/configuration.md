---
paik_version: "2.0"
doc_type: configuration
id: configuration
name: TaskFlow Lite Configuration Management
status: active
last_updated: "2026-07-21"
owner_ref: team.md
visibility: internal
tool: dotenv
location: https://dashboard.render.com/web/taskflow-lite/env
key_naming_convention: "TFL_<COMPONENT>_<KEY>, upper snake case"
environment_mapping:
  dev: Render service "taskflow-lite-dev" environment tab
  prod: Render service "taskflow-lite-prod" environment tab
rotation_policy_ref: systems/knowledge-base.md
feature_flag_system: none
---

# TaskFlow Lite Configuration Management

- Tool: `dotenv` (managed per-service in the Render dashboard, not committed to the repo)
- Location: https://dashboard.render.com/web/taskflow-lite/env
- Key naming convention: `TFL_<COMPONENT>_<KEY>`, upper snake case
- Per-environment mapping: see `environment_mapping` above
- Rotation policy: see [knowledge-base.md](systems/knowledge-base.md)
- Feature flags: none — this project is small enough to ship behind short-lived branches instead
- Owner: [TaskFlow Lite team](team.md)

## Database connections

### dev database
Connection string lives in env var `TFL_DB_URL` on the `taskflow-lite-dev` Render service.

### prod database
Connection string lives in env var `TFL_DB_URL` on the `taskflow-lite-prod` Render service.

Neither value is stored in this repository or in this document — only the pointer above.
