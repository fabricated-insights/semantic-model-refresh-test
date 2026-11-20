# Harness run 20261120T173342Z-v99i-ce5e

- Task: refresh
- Variant: v99i-buffer-stg-sales
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 4fe130da-de9e-4847-b4c4-f7cb395591a5
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 12 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 6ca8d934-396a-47f4-b45e-c2b59b4ef580, 2026-11-20T17:35:13.14Z to 2026-11-20T17:46:59.787Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99i-buffer-stg-sales on Pro data-1m-v1: failed, peak n/a (2026-11-20T11:50:53Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
```

**Screenshot: the refresh error of v99i-buffer-stg-sales on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v99i-buffer-stg-sales-refresh-error.png**

## Log

```
2026-11-20T17:34:24Z run 20261120T173342Z-v99i-ce5e: variant=v99i-buffer-stg-sales data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T17:34:27Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T17:35:02Z Pro: updated v99i-buffer-stg-sales from the F64 workspace (23 files)
2026-11-20T17:35:03Z Pro: v99i-buffer-stg-sales is 8b00d85b-e78a-4019-865c-26c24933f52c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T17:35:12Z Pro: model size in memory before the refresh: None MB
2026-11-20T17:35:13Z Pro: standard refresh started
2026-11-20T17:47:15Z Pro: refresh failed (Failed) other
```
