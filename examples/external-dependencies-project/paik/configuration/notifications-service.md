---
paik_version: "2.1"
doc_type: configuration
id: notifications-service-configuration
name: Notifications Service — Configuration
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/notifications.md
visibility: internal
tool: vault
location: https://vault.aurora-logistics.example/ui/vault/secrets/aurora
key_naming_convention: "aurora/<environment>/notifications-service/<key>"
environment_mapping:
  dev: secret/aurora/dev/notifications-service
  staging: secret/aurora/staging/notifications-service
  prod: secret/aurora/prod/notifications-service
rotation_policy_ref: ../systems/knowledge-base.md
feature_flag_system: see shared.md
---

# Notifications Service — Configuration

- Tool: `vault`
- Key naming convention: `aurora/<environment>/notifications-service/<key>`
- Per-environment mapping: see `environment_mapping` above
- Shared config (auth, feature flags): see [shared.md](shared.md)
- Owner: [Notifications team](../teams/notifications.md)

`notifications-service` is a stateless relay — no database connections to list.
