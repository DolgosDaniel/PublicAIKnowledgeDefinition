---
paik_version: "1.0"
doc_type: configuration
id: catalog-api-configuration
name: Catalog API — Configuration
status: active
last_updated: 2026-07-21
owner_ref: ../participants.md#zsofia-kiss
tool: vault
location: https://vault.nimbus.example/ui/vault/secrets/nimbus
key_naming_convention: "nimbus/<environment>/catalog-api/<key>"
environment_mapping:
  dev: secret/nimbus/dev/catalog-api
  staging: secret/nimbus/staging/catalog-api
  prod-eu: secret/nimbus/prod-eu/catalog-api
  prod-us: secret/nimbus/prod-us/catalog-api
rotation_policy_ref: ../systems/knowledge-base.md
feature_flag_system: see shared.md
---

# Catalog API — Configuration

- Tool: `vault`
- Key naming convention: `nimbus/<environment>/catalog-api/<key>`
- Per-environment mapping: see `environment_mapping` above
- Shared config (auth, feature flags): see [shared.md](shared.md)
- Owner: [Zsofia Kiss](../participants.md#zsofia-kiss)

## Database connections

### dev catalog database
Connection string: Vault path `secret/nimbus/dev/catalog-api/db-url`.

### staging catalog database
Connection string: Vault path `secret/nimbus/staging/catalog-api/db-url`.

### prod-eu catalog database
Connection string: Vault path `secret/nimbus/prod-eu/catalog-api/db-url`.

### prod-us catalog database
Connection string: Vault path `secret/nimbus/prod-us/catalog-api/db-url`.

No connection string, password, or Vault token is stored in this document — only the path.
