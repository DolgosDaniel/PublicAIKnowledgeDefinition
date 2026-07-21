---
paik_version: "2.1"
doc_type: configuration
id: routing-service-configuration
name: Routing Service — Configuration
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/routing.md
visibility: internal
tool: vault
location: https://vault.aurora-logistics.example/ui/vault/secrets/aurora
key_naming_convention: "aurora/<environment>/routing-service/<key>"
environment_mapping:
  dev: secret/aurora/dev/routing-service
  staging: secret/aurora/staging/routing-service
  prod: secret/aurora/prod/routing-service
rotation_policy_ref: ../systems/knowledge-base.md
feature_flag_system: see shared.md
---

# Routing Service — Configuration

- Tool: `vault`
- Key naming convention: `aurora/<environment>/routing-service/<key>`
- Per-environment mapping: see `environment_mapping` above
- Shared config (auth, feature flags): see [shared.md](shared.md)
- Mapbox API token: Vault path `secret/aurora/<environment>/routing-service/mapbox-token` — see
  [external-services/mapbox.md](../external-services/mapbox.md) for the vendor relationship,
  never the token itself
- Owner: [Routing team](../teams/routing.md)

`routing-service` is stateless — no database connections to list.
