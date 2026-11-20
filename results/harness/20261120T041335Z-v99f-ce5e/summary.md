# Harness run 20261120T041335Z-v99f-ce5e

- Task: refresh
- Variant: v99f-calc-tables
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 7b2bcaa2-8eb9-43a6-b8a9-0e4cd374a58e
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 18 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 65620158-f4d0-40c6-8851-1288969fed2a, 2026-11-20T04:16:36.253Z to 2026-11-20T04:35:02.233Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99f-calc-tables on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T13:35:08Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T04:15:42Z run 20261120T041335Z-v99f-ce5e: variant=v99f-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T04:15:45Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T04:16:18Z Pro: updated v99f-calc-tables from the F64 workspace (22 files)
2026-11-20T04:16:20Z Pro: v99f-calc-tables is 0ab28c16-fec1-459d-9a1d-545cd285070a, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T04:16:35Z Pro: model size in memory before the refresh: None MB
2026-11-20T04:16:36Z Pro: standard refresh started
2026-11-20T04:35:09Z Pro: refresh refreshed (Completed) 
2026-11-20T04:35:09Z Pro: model size in memory right after the refresh: None MB
```
