---
paik_version: "2.1"
doc_type: configuration
id: aurora-shared-configuration
name: Aurora Logistics — Shared Configuration
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/platform.md
visibility: internal
tool: vault
location: https://vault.aurora-logistics.example/ui/vault/secrets/aurora
key_naming_convention: "aurora/<environment>/shared/<key>"
environment_mapping:
  dev: secret/aurora/dev/shared
  staging: secret/aurora/staging/shared
  prod: secret/aurora/prod/shared
rotation_policy_ref: ../systems/knowledge-base.md
feature_flag_system: LaunchDarkly — https://app.launchdarkly.com/aurora-logistics
---

# Aurora Logistics — Shared Configuration

Cross-service config (auth signing keys, shared rate-limit settings, feature flags). Per-service
config lives in `orders-service.md`, `routing-service.md`, `fleet-service.md`, and
`notifications-service.md` instead.

- Tool: `vault`
- Location: https://vault.aurora-logistics.example/ui/vault/secrets/aurora
- Key naming convention: `aurora/<environment>/shared/<key>`
- Per-environment mapping: see `environment_mapping` above
- Rotation policy: see [knowledge-base.md](../systems/knowledge-base.md)
- Feature flags: LaunchDarkly — https://app.launchdarkly.com/aurora-logistics
- Owner: [Platform](../teams/platform.md)
