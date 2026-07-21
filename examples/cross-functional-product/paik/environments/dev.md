---
paik: "0.3"
kind: environment
id: dev
name: Development
lifecycle: active
purpose: developer integration testing, auto-deployed from main on every merge
app_url: https://rewards-app-dev.onrender.com
health_endpoint: https://rewards-app-dev.onrender.com/health
databases:
  - type: postgres
    host_ref: env var REWARDS_DB_URL on the Render service "rewards-app-dev"
access: internal only
links:
  - kind: deploy-pipeline
    url: https://github.com/solstice-app/rewards-app/actions/workflows/deploy-dev.yml
---

# Development

- Purpose: developer integration testing, auto-deployed from `main` on every merge
- App URL: https://rewards-app-dev.onrender.com
- Health endpoint: https://rewards-app-dev.onrender.com/health
- Database: Postgres — connection string lives in env var `REWARDS_DB_URL`, never in this file
- Deploy pipeline: see `links` above
- Access: internal only
