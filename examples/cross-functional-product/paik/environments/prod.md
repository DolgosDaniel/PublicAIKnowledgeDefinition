---
paik: "0.3"
kind: environment
id: prod
name: Production
lifecycle: active
purpose: customer-facing production
app_url: https://rewards.solstice-app.example
health_endpoint: https://rewards.solstice-app.example/health
databases:
  - type: postgres
    host_ref: env var REWARDS_DB_URL on the Render service "rewards-app-prod"
access: public
links:
  - kind: status-page
    url: https://status.solstice-app.example
  - kind: deploy-pipeline
    url: https://github.com/solstice-app/rewards-app/actions/workflows/deploy-prod.yml
---

# Production

- Purpose: customer-facing production
- App URL: https://rewards.solstice-app.example
- Health endpoint: https://rewards.solstice-app.example/health
- Database: Postgres — connection string lives in env var `REWARDS_DB_URL`, never in this file
- Status page / deploy pipeline: see `links` above
- Access: public
