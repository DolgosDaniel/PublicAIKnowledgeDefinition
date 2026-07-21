---
paik: "0.3"
kind: environment
id: dev
name: Development
lifecycle: active
purpose: shared developer integration environment for all three components, auto-deployed from main
app_url: https://dev.vertex-robotics.example
health_endpoint: https://dev.vertex-robotics.example/health
access: VPN required
links:
  - kind: deploy-pipeline
    component: api-gateway
    url: https://github.com/vertex-robotics/platform/actions/workflows/deploy-api-gateway-dev.yml
  - kind: deploy-pipeline
    component: billing-service
    url: https://github.com/vertex-robotics/platform/actions/workflows/deploy-billing-service-dev.yml
  - kind: deploy-pipeline
    component: web-client
    url: https://github.com/vertex-robotics/platform/actions/workflows/deploy-web-client-dev.yml
---

# Development

- Purpose: shared developer integration environment for all three components, auto-deployed
  from `main` on every merge
- App URL: https://dev.vertex-robotics.example
- Health endpoint: https://dev.vertex-robotics.example/health
- Deploy pipelines: one path-filtered workflow per component in the same monorepo — see `links`
  above (each tagged with the `component` it deploys)
- Access: VPN required
