# Harness run 20261120T151126Z-v99-ce5e

- Task: refresh
- Variant: v99-kitchen-sink
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 66e8de0e-b534-47ca-ab73-29709b3bd435
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 12 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 62c76fdc-f26b-4ca9-ba79-e0641e27335d, 2026-11-20T15:14:41.61Z to 2026-11-20T15:26:43.723Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99-kitchen-sink on Pro data-1m-v1: failed, peak n/a (2026-11-20T09:25:43Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
```

**Screenshot: the refresh error of v99-kitchen-sink on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v99-kitchen-sink-refresh-error.png**

## Log

```
2026-11-20T15:13:47Z run 20261120T151126Z-v99-ce5e: variant=v99-kitchen-sink data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T15:13:49Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T15:14:22Z Pro: updated v99-kitchen-sink from the F64 workspace (18 files)
2026-11-20T15:14:23Z Pro: v99-kitchen-sink is 4af1fdd1-397f-427c-be5d-3ea9bc11943d, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T15:14:41Z Pro: model size in memory before the refresh: None MB
2026-11-20T15:14:41Z Pro: standard refresh started
2026-11-20T15:27:13Z Pro: refresh failed (Failed) other
```
