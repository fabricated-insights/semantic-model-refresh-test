# Harness run 20261120T115144Z-v99j-ce5e

- Task: refresh
- Variant: v99j-buffer-stg-customer
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6ed7e94d-40a4-475d-809a-090ce2d00a96
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 8 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 15f64d2d-5ae9-4c53-b267-65946ee2254d, 2026-11-20T11:54:55.503Z to 2026-11-20T12:03:04.843Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99j-buffer-stg-customer on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T06:04:37Z).
  - **FLAG: result changed from refreshed to failed**
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
```

**Screenshot: the refresh error of v99j-buffer-stg-customer on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v99j-buffer-stg-customer-refresh-error.png**

## Log

```
2026-11-20T11:54:03Z run 20261120T115144Z-v99j-ce5e: variant=v99j-buffer-stg-customer data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T11:54:06Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T11:54:39Z Pro: updated v99j-buffer-stg-customer from the F64 workspace (23 files)
2026-11-20T11:54:40Z Pro: v99j-buffer-stg-customer is cbaa387f-25ff-4493-a117-b7450fd39e13, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:54:55Z Pro: model size in memory before the refresh: None MB
2026-11-20T11:54:55Z Pro: standard refresh started
2026-11-20T12:03:26Z Pro: refresh failed (Failed) other
```
