# Harness run 20261120T073820Z-v22-ce5e

- Task: refresh
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: c08b6201-5268-4b02-9336-f918e7438143
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 779278a4-bfb5-4c26-9b6a-b30eafd3e308, 2026-11-20T07:39:40.083Z to 2026-11-20T07:40:46.65Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v22-dax-calc-columns on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T00:21:17Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T07:39:07Z run 20261120T073820Z-v22-ce5e: variant=v22-dax-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T07:39:11Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T07:39:28Z Pro: updated v22-dax-calc-columns from the F64 workspace (12 files)
2026-11-20T07:39:29Z Pro: v22-dax-calc-columns is 1c294d69-ca0d-4f75-8938-a00dc5a173ae, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:39:39Z Pro: model size in memory before the refresh: None MB
2026-11-20T07:39:40Z Pro: standard refresh started
2026-11-20T07:41:10Z Pro: refresh refreshed (Completed) 
2026-11-20T07:41:10Z Pro: model size in memory right after the refresh: None MB
```
