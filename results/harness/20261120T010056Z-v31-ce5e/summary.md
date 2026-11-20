# Harness run 20261120T010056Z-v31-ce5e

- Task: refresh
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 190e2cb1-78c8-4abb-8f1b-883408359195
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 26575390-905b-4aa6-a390-702144607505, 2026-11-20T01:05:27.763Z to 2026-11-20T01:06:30.84Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v31-calc-columns-row on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T14:34:59Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T01:04:27Z run 20261120T010056Z-v31-ce5e: variant=v31-calc-columns-row data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T01:04:30Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T01:05:09Z Pro: updated v31-calc-columns-row from the F64 workspace (12 files)
2026-11-20T01:05:10Z Pro: v31-calc-columns-row is 9294e5ca-efe7-40c2-be3f-9ea4bb8bf562, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T01:05:27Z Pro: model size in memory before the refresh: None MB
2026-11-20T01:05:27Z Pro: standard refresh started
2026-11-20T01:06:57Z Pro: refresh refreshed (Completed) 
2026-11-20T01:06:57Z Pro: model size in memory right after the refresh: None MB
```
