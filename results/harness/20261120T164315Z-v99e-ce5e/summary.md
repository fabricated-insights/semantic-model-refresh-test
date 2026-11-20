# Harness run 20261120T164315Z-v99e-ce5e

- Task: refresh
- Variant: v99e-sales-flat
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 00e34ab0-7dd2-4d05-84fd-056533bba7a7
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 8 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 9fe819c7-38fc-44ea-aa73-94ed6f96f8c1, 2026-11-20T16:44:47.61Z to 2026-11-20T16:52:58.39Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99e-sales-flat on Pro data-1m-v1: failed, peak n/a (2026-11-20T10:51:54Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
```

**Screenshot: the refresh error of v99e-sales-flat on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v99e-sales-flat-refresh-error.png**

## Log

```
2026-11-20T16:43:53Z run 20261120T164315Z-v99e-ce5e: variant=v99e-sales-flat data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T16:43:57Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T16:44:36Z Pro: updated v99e-sales-flat from the F64 workspace (20 files)
2026-11-20T16:44:37Z Pro: v99e-sales-flat is 501ed679-2c3e-4eb5-9103-ebd582eec18f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T16:44:47Z Pro: model size in memory before the refresh: None MB
2026-11-20T16:44:47Z Pro: standard refresh started
2026-11-20T16:53:18Z Pro: refresh failed (Failed) other
```
