# Harness run 20261120T062410Z-v99l-ce5e

- Task: refresh
- Variant: v99l-no-calc-columns
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1cba1b8d-ca27-4db3-a5fa-fb39fab84cb4
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 16 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request eca6645c-9806-4c00-aa52-6c9780cd9910, 2026-11-20T06:25:45.003Z to 2026-11-20T06:41:49.177Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99l-no-calc-columns on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T16:16:52Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T06:24:43Z run 20261120T062410Z-v99l-ce5e: variant=v99l-no-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T06:24:47Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T06:25:34Z Pro: updated v99l-no-calc-columns from the F64 workspace (18 files)
2026-11-20T06:25:36Z Pro: v99l-no-calc-columns is 0f6c29d2-64ea-4290-8edb-60429d55affa, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T06:25:44Z Pro: model size in memory before the refresh: None MB
2026-11-20T06:25:44Z Pro: standard refresh started
2026-11-20T06:42:17Z Pro: refresh refreshed (Completed) 
2026-11-20T06:42:17Z Pro: model size in memory right after the refresh: None MB
```
