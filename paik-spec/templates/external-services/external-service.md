---
paik_version: "2.1"
doc_type: external-service
id: <vendor-slug>
name: <Vendor/Product Name>
status: active
last_updated: "<YYYY-MM-DD>"
owner_ref: ../teams/<owning-team>.md
visibility: internal # public | internal | confidential
type: payments # payments | communications | geo-mapping | infrastructure | analytics | other
vendor: <Company Name, Inc.>
base_url: https://<vendor>.example
docs_url: https://docs.<vendor>.example/api
status_page: https://status.<vendor>.example
contract_ref: ../systems/knowledge-base.md
data_shared: <one line: what data flows to this vendor, e.g. "payment card tokens, vendor-hosted checkout">
---

# <Vendor/Product Name>

A third-party dependency this project calls but does not operate.

- Type: `payments`
- Vendor: <Company Name, Inc.>
- Docs: <docs_url>
- Status page: <status_page>
- Contract/SLA: see [knowledge-base.md](../systems/knowledge-base.md)
- Data shared: <data_shared>
- Owner: [<Owning Team>](../teams/<owning-team>.md)
