# Harness run 20261120T045505Z-v99h-ce5e

- Task: refresh
- Variant: v99h-staging-buffers
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 94de3c4b-1feb-47e5-bdff-861a9a70c8f5
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 29 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 6fc42b14-75e1-4305-8caa-d72aef61a262, 2026-11-20T04:58:15.11Z to 2026-11-20T05:27:06.05Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99h-staging-buffers on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T23:41:34Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T04:57:21Z run 20261120T045505Z-v99h-ce5e: variant=v99h-staging-buffers data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T04:57:24Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T04:57:59Z Pro: updated v99h-staging-buffers from the F64 workspace (23 files)
2026-11-20T04:58:00Z Pro: v99h-staging-buffers is f80e532f-84c0-4fd5-95ad-f4fcbae06174, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T04:58:14Z Pro: model size in memory before the refresh: None MB
2026-11-20T04:58:15Z Pro: standard refresh started
2026-11-20T05:27:20Z Pro: refresh refreshed (Completed) 
2026-11-20T05:27:20Z Pro: model size in memory right after the refresh: None MB
```
