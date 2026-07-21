---
paik_version: "1.0"
doc_type: configuration
id: configuration
name: Configuration Management
status: active
last_updated: "<YYYY-MM-DD>"
owner_ref: participants.md#<owner-anchor>
tool: vault # vault | aws-secrets-manager | consul | dotenv | spring-cloud-config | helm-values | other
location: https://vault.example.com/ui/vault/secrets/<project>
key_naming_convention: "<project>/<environment>/<component>/<key>"
environment_mapping:
  dev: secret/<project>/dev
  prod: secret/<project>/prod
rotation_policy_ref: systems/knowledge-base.md
feature_flag_system: <name/URL, or "none">
---

# Configuration Management

How configuration and secrets are managed for this project. This document links to *where*
config lives — it never contains an actual secret value.

- Tool: `vault`
- Location: <location>
- Key naming convention: `<project>/<environment>/<component>/<key>`
- Per-environment mapping: see `environment_mapping` above
- Rotation policy: [<link>](systems/knowledge-base.md)
- Feature flags: <feature_flag_system>
- Owner: [<Owner Name>](participants.md#<owner-anchor>)
