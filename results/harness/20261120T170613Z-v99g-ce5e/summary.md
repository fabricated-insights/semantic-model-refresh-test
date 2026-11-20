# Harness run 20261120T170613Z-v99g-ce5e

- Task: refresh
- Variant: v99g-sales-copy
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a16b3164-d4b0-411d-84aa-0bbff53ecc5d
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 8 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 40304591-653a-432f-9495-fd30bda7b771, 2026-11-20T17:09:47.167Z to 2026-11-20T17:17:59.49Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99g-sales-copy on Pro data-1m-v1: failed, peak n/a (2026-11-20T11:17:06Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
```

**Screenshot: the refresh error of v99g-sales-copy on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v99g-sales-copy-refresh-error.png**

## Log

```
2026-11-20T17:08:50Z run 20261120T170613Z-v99g-ce5e: variant=v99g-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T17:08:53Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T17:09:26Z Pro: updated v99g-sales-copy from the F64 workspace (23 files)
2026-11-20T17:09:27Z Pro: v99g-sales-copy is 365c91bc-922d-40fa-af7b-6ca43099dddb, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T17:09:46Z Pro: model size in memory before the refresh: None MB
2026-11-20T17:09:47Z Pro: standard refresh started
2026-11-20T17:18:18Z Pro: refresh failed (Failed) other
```
