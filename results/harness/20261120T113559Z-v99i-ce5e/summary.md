# Harness run 20261120T113559Z-v99i-ce5e

- Task: refresh
- Variant: v99i-buffer-stg-sales
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 921a47ec-d3fd-4ab8-bc9f-5b472bf7ed41
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 13 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 827948e2-0205-4e18-8907-42a4116f3d2a, 2026-11-20T11:37:21.27Z to 2026-11-20T11:50:49.71Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99i-buffer-stg-sales on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T05:46:35Z).
  - **FLAG: result changed from refreshed to failed**
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
```

**Screenshot: the refresh error of v99i-buffer-stg-sales on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v99i-buffer-stg-sales-refresh-error.png**

## Log

```
2026-11-20T11:36:32Z run 20261120T113559Z-v99i-ce5e: variant=v99i-buffer-stg-sales data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T11:36:36Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T11:37:11Z Pro: updated v99i-buffer-stg-sales from the F64 workspace (23 files)
2026-11-20T11:37:12Z Pro: v99i-buffer-stg-sales is 8b00d85b-e78a-4019-865c-26c24933f52c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:37:20Z Pro: model size in memory before the refresh: None MB
2026-11-20T11:37:21Z Pro: standard refresh started
2026-11-20T11:50:53Z Pro: refresh failed (Failed) other
```
