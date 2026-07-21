---
paik_version: "2.1"
doc_type: external-service
id: aurora-stripe
name: Stripe
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/orders.md
visibility: internal
type: payments
vendor: Stripe, Inc.
base_url: https://stripe.com
docs_url: https://docs.stripe.com/api
status_page: https://status.stripe.com
contract_ref: ../systems/knowledge-base.md
data_shared: payment card tokens and delivery-fee charge amounts; card numbers never touch our systems (Stripe-hosted checkout)
---

# Stripe

Payment processor for delivery fees. `orders-service` calls Stripe's API directly; Aurora
Logistics does not operate or host any part of this.

- Type: `payments`
- Vendor: Stripe, Inc.
- Docs: https://docs.stripe.com/api
- Status page: https://status.stripe.com
- Contract/SLA: see [knowledge-base.md](../systems/knowledge-base.md)
- Data shared: payment card tokens and delivery-fee charge amounts; card numbers never touch our
  systems (Stripe-hosted checkout)
- Owner: [Orders team](../teams/orders.md)
