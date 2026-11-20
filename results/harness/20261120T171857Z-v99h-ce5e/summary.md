# Harness run 20261120T171857Z-v99h-ce5e

- Task: refresh
- Variant: v99h-staging-buffers
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: cb51b87e-f2ce-4b5b-a7f1-1244f9b5b0a0
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 12 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 2b171633-39ee-42d9-ad50-95adc6a0faf4, 2026-11-20T17:20:36.63Z to 2026-11-20T17:32:37.393Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99h-staging-buffers on Pro data-1m-v1: failed, peak n/a (2026-11-20T11:35:33Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
```

**Screenshot: the refresh error of v99h-staging-buffers on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v99h-staging-buffers-refresh-error.png**

## Log

```
2026-11-20T17:19:46Z run 20261120T171857Z-v99h-ce5e: variant=v99h-staging-buffers data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T17:19:49Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T17:20:24Z Pro: updated v99h-staging-buffers from the F64 workspace (23 files)
2026-11-20T17:20:25Z Pro: v99h-staging-buffers is f80e532f-84c0-4fd5-95ad-f4fcbae06174, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T17:20:36Z Pro: model size in memory before the refresh: None MB
2026-11-20T17:20:36Z Pro: standard refresh started
2026-11-20T17:32:38Z Pro: refresh failed (Failed) other
```
