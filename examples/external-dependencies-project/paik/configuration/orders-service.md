---
paik_version: "2.1"
doc_type: configuration
id: orders-service-configuration
name: Orders Service — Configuration
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/orders.md
visibility: internal
tool: vault
location: https://vault.aurora-logistics.example/ui/vault/secrets/aurora
key_naming_convention: "aurora/<environment>/orders-service/<key>"
environment_mapping:
  dev: secret/aurora/dev/orders-service
  staging: secret/aurora/staging/orders-service
  prod: secret/aurora/prod/orders-service
rotation_policy_ref: ../systems/knowledge-base.md
feature_flag_system: see shared.md
---

# Orders Service — Configuration

- Tool: `vault`
- Key naming convention: `aurora/<environment>/orders-service/<key>`
- Per-environment mapping: see `environment_mapping` above
- Shared config (auth, feature flags): see [shared.md](shared.md)
- Stripe API key: Vault path `secret/aurora/<environment>/orders-service/stripe-key` — see
  [external-services/stripe.md](../external-services/stripe.md) for the vendor relationship,
  never the key itself
- Owner: [Orders team](../teams/orders.md)

## Database connections

### dev orders database
Connection string: Vault path `secret/aurora/dev/orders-service/db-url`.

### staging orders database
Connection string: Vault path `secret/aurora/staging/orders-service/db-url`.

### prod orders database
Connection string: Vault path `secret/aurora/prod/orders-service/db-url`.

No connection string, password, or Vault token is stored in this document — only the path.
