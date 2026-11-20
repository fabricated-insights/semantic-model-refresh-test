# Harness run 20261120T100456Z-v99c-ce5e

- Task: refresh
- Variant: v99c-crossjoin-only
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 507d2fd1-a78e-412c-bdcf-3d965f481b3b
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 13 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 44df1cba-90f8-45fe-99ed-0487bff4bfd8, 2026-11-20T10:08:04.683Z to 2026-11-20T10:20:40.187Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99c-crossjoin-only on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T03:33:19Z).
  - **FLAG: result changed from refreshed to failed**
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
```

**Screenshot: the refresh error of v99c-crossjoin-only on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v99c-crossjoin-only-refresh-error.png**

## Log

```
2026-11-20T10:07:09Z run 20261120T100456Z-v99c-ce5e: variant=v99c-crossjoin-only data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T10:07:14Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T10:07:47Z Pro: updated v99c-crossjoin-only from the F64 workspace (18 files)
2026-11-20T10:07:49Z Pro: v99c-crossjoin-only is 6af71876-9875-4b2d-8a55-fbde4a52de4f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T10:08:04Z Pro: model size in memory before the refresh: None MB
2026-11-20T10:08:04Z Pro: standard refresh started
2026-11-20T10:21:06Z Pro: refresh failed (Failed) other
```
