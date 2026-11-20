# Harness run 20261120T110455Z-v99g-ce5e

- Task: refresh
- Variant: v99g-sales-copy
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 2c46ab3e-f1b4-42c7-a5fd-bd9aef61aa63
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 9 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request e5bf21e6-6e14-4a0c-a1d2-8a826d3e4fca, 2026-11-20T11:08:05.307Z to 2026-11-20T11:16:40.83Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99g-sales-copy on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T04:54:32Z).
  - **FLAG: result changed from refreshed to failed**
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
```

**Screenshot: the refresh error of v99g-sales-copy on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v99g-sales-copy-refresh-error.png**

## Log

```
2026-11-20T11:07:09Z run 20261120T110455Z-v99g-ce5e: variant=v99g-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T11:07:12Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T11:07:46Z Pro: updated v99g-sales-copy from the F64 workspace (23 files)
2026-11-20T11:07:47Z Pro: v99g-sales-copy is 365c91bc-922d-40fa-af7b-6ca43099dddb, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:08:05Z Pro: model size in memory before the refresh: None MB
2026-11-20T11:08:05Z Pro: standard refresh started
2026-11-20T11:17:06Z Pro: refresh failed (Failed) other
```
