---
paik_version: "2.1"
doc_type: configuration
id: fleet-service-configuration
name: Fleet Service — Configuration
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/fleet.md
visibility: internal
tool: vault
location: https://vault.aurora-logistics.example/ui/vault/secrets/aurora
key_naming_convention: "aurora/<environment>/fleet-service/<key>"
environment_mapping:
  dev: secret/aurora/dev/fleet-service
  staging: secret/aurora/staging/fleet-service
  prod: secret/aurora/prod/fleet-service
rotation_policy_ref: ../systems/knowledge-base.md
feature_flag_system: see shared.md
---

# Fleet Service — Configuration

- Tool: `vault`
- Key naming convention: `aurora/<environment>/fleet-service/<key>`
- Per-environment mapping: see `environment_mapping` above
- Shared config (auth, feature flags): see [shared.md](shared.md)
- Owner: [Fleet team](../teams/fleet.md)

## Database connections

### dev fleet database
Connection string: Vault path `secret/aurora/dev/fleet-service/db-url`.

### staging fleet database
Connection string: Vault path `secret/aurora/staging/fleet-service/db-url`.

### prod fleet database
Connection string: Vault path `secret/aurora/prod/fleet-service/db-url`.

No connection string, password, or Vault token is stored in this document — only the path.
