---
paik_version: "1.0"
doc_type: configuration
id: nimbus-shared-configuration
name: Nimbus Commerce — Shared Configuration
status: active
last_updated: 2026-07-21
owner_ref: ../participants.md#adam-fekete
tool: vault
location: https://vault.nimbus.example/ui/vault/secrets/nimbus
key_naming_convention: "nimbus/<environment>/shared/<key>"
environment_mapping:
  dev: secret/nimbus/dev/shared
  staging: secret/nimbus/staging/shared
  prod-eu: secret/nimbus/prod-eu/shared
  prod-us: secret/nimbus/prod-us/shared
rotation_policy_ref: ../systems/knowledge-base.md
feature_flag_system: LaunchDarkly — https://app.launchdarkly.com/nimbus-commerce
---

# Nimbus Commerce — Shared Configuration

Cross-service config (auth signing keys, shared rate-limit settings, feature flags). Per-service
config lives in [orders-api.md](orders-api.md) and [catalog-api.md](catalog-api.md) instead.

- Tool: `vault`
- Location: https://vault.nimbus.example/ui/vault/secrets/nimbus
- Key naming convention: `nimbus/<environment>/shared/<key>`
- Per-environment mapping: see `environment_mapping` above
- Rotation policy: see [knowledge-base.md](../systems/knowledge-base.md)
- Feature flags: LaunchDarkly — https://app.launchdarkly.com/nimbus-commerce
- Owner: [Adam Fekete](../participants.md#adam-fekete)
