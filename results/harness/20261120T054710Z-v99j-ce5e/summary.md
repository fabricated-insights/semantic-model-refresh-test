# Harness run 20261120T054710Z-v99j-ce5e

- Task: refresh
- Variant: v99j-buffer-stg-customer
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a7ce7020-9bbb-4a78-b44d-c9fb6ffaa146
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 16 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 182309f7-f6cf-4ff1-ad64-8e8c755fa0e2, 2026-11-20T05:48:34.903Z to 2026-11-20T06:04:36.23Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99j-buffer-stg-customer on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T22:05:09Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T05:47:48Z run 20261120T054710Z-v99j-ce5e: variant=v99j-buffer-stg-customer data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T05:47:50Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T05:48:25Z Pro: updated v99j-buffer-stg-customer from the F64 workspace (23 files)
2026-11-20T05:48:26Z Pro: v99j-buffer-stg-customer is cbaa387f-25ff-4493-a117-b7450fd39e13, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T05:48:34Z Pro: model size in memory before the refresh: None MB
2026-11-20T05:48:34Z Pro: standard refresh started
2026-11-20T06:04:37Z Pro: refresh refreshed (Completed) 
2026-11-20T06:04:37Z Pro: model size in memory right after the refresh: None MB
```
