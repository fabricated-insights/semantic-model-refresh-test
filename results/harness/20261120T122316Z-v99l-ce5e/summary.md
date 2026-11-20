# Harness run 20261120T122316Z-v99l-ce5e

- Task: refresh
- Variant: v99l-no-calc-columns
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ba57d6d5-6881-455d-aad8-27cfccb3d7fe
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 18 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 4eba39f9-9af6-4694-b6d2-8adacf116a42, 2026-11-20T12:26:26.113Z to 2026-11-20T12:44:49.373Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99l-no-calc-columns on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T06:42:17Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T12:25:42Z run 20261120T122316Z-v99l-ce5e: variant=v99l-no-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T12:25:45Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T12:26:08Z Pro: updated v99l-no-calc-columns from the F64 workspace (18 files)
2026-11-20T12:26:09Z Pro: v99l-no-calc-columns is 0f6c29d2-64ea-4290-8edb-60429d55affa, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:26:25Z Pro: model size in memory before the refresh: None MB
2026-11-20T12:26:26Z Pro: standard refresh started
2026-11-20T12:44:59Z Pro: refresh refreshed (Completed) 
2026-11-20T12:44:59Z Pro: model size in memory right after the refresh: None MB
```
