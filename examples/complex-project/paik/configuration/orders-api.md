---
paik_version: "2.0"
doc_type: configuration
id: orders-api-configuration
name: Orders API — Configuration
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/orders.md
visibility: internal
tool: vault
location: https://vault.nimbus.example/ui/vault/secrets/nimbus
key_naming_convention: "nimbus/<environment>/orders-api/<key>"
environment_mapping:
  dev: secret/nimbus/dev/orders-api
  staging: secret/nimbus/staging/orders-api
  prod-eu: secret/nimbus/prod-eu/orders-api
  prod-us: secret/nimbus/prod-us/orders-api
rotation_policy_ref: ../systems/knowledge-base.md
feature_flag_system: see shared.md
---

# Orders API — Configuration

- Tool: `vault`
- Key naming convention: `nimbus/<environment>/orders-api/<key>`
- Per-environment mapping: see `environment_mapping` above
- Shared config (auth, feature flags): see [shared.md](shared.md)
- Owner: [Orders team](../teams/orders.md)

## Database connections

### dev orders database
Connection string: Vault path `secret/nimbus/dev/orders-api/db-url`.

### staging orders database
Connection string: Vault path `secret/nimbus/staging/orders-api/db-url`.

### prod-eu orders database
Connection string: Vault path `secret/nimbus/prod-eu/orders-api/db-url`.

### prod-us orders database
Connection string: Vault path `secret/nimbus/prod-us/orders-api/db-url`.

No connection string, password, or Vault token is stored in this document — only the path.
