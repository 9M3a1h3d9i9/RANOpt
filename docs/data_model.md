# Data Model

## RANKPI

One `RANKPI` record represents one cell observation at one timestamp.

Required fields:

| Field | Meaning |
|---|---|
| `cell_id` | Cell identifier |
| `timestamp` | Observation time |
| `rsrp_dbm` | Reference signal received power |
| `rsrq_db` | Reference signal received quality |
| `sinr_db` | Signal-to-interference-plus-noise ratio |
| `dl_throughput_mbps` | Downlink throughput |
| `ul_throughput_mbps` | Uplink throughput |
| `drop_rate_pct` | Call/session drop rate |
| `handover_success_pct` | Handover success percentage |
| `availability_pct` | Cell/service availability |

## Design principles

1. Raw observations are validated before analytics.
2. Cell metadata is separate from time-varying KPI observations.
3. Synthetic data is deterministic for tests and examples.
4. Thresholds are configuration, not hard-coded operator policy.
5. No real operator data is included in the repository.
