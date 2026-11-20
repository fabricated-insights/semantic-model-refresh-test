# Harness run 20261120T094825Z-v99b-ce5e

- Task: refresh
- Variant: v99b-one-sales-copy
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: b3774714-f077-4b3e-b511-0ac2ae50ee62
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 12 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 62c9afc7-4d29-418e-a4a3-abfb19403ad5, 2026-11-20T09:52:26.457Z to 2026-11-20T10:04:14.2Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99b-one-sales-copy on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T02:59:21Z).
  - **FLAG: result changed from refreshed to failed**
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
```

**Screenshot: the refresh error of v99b-one-sales-copy on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v99b-one-sales-copy-refresh-error.png**

## Log

```
2026-11-20T09:51:25Z run 20261120T094825Z-v99b-ce5e: variant=v99b-one-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T09:51:28Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T09:52:03Z Pro: updated v99b-one-sales-copy from the F64 workspace (18 files)
2026-11-20T09:52:05Z Pro: v99b-one-sales-copy is 1c2a3fcf-c1d3-4055-9c06-ead16a7c0f62, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:52:26Z Pro: model size in memory before the refresh: None MB
2026-11-20T09:52:26Z Pro: standard refresh started
2026-11-20T10:04:28Z Pro: refresh failed (Failed) other
```
