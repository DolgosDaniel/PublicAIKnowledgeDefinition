---
paik_version: "2.1"
doc_type: external-service
id: aurora-mapbox
name: Mapbox
status: active
last_updated: "2026-07-21"
owner_ref: ../teams/routing.md
visibility: internal
type: geo-mapping
vendor: Mapbox, Inc.
base_url: https://www.mapbox.com
docs_url: https://docs.mapbox.com/api/
status_page: https://status.mapbox.com
contract_ref: ../systems/knowledge-base.md
data_shared: pickup/dropoff coordinates and driver GPS pings for route optimization and geocoding
---

# Mapbox

Route optimization and geocoding provider. `routing-service` calls Mapbox's API directly; Aurora
Logistics does not operate or host any part of this.

- Type: `geo-mapping`
- Vendor: Mapbox, Inc.
- Docs: https://docs.mapbox.com/api/
- Status page: https://status.mapbox.com
- Contract/SLA: see [knowledge-base.md](../systems/knowledge-base.md)
- Data shared: pickup/dropoff coordinates and driver GPS pings for route optimization and
  geocoding
- Owner: [Routing team](../teams/routing.md)
