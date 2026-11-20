# Harness run 20261120T165357Z-v99f-ce5e

- Task: refresh
- Variant: v99f-calc-tables
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 030a549b-e566-454d-b139-6f9ce7db7987
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 8 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request b4bbfb24-f655-44ff-879b-723ca501682a, 2026-11-20T16:57:13.977Z to 2026-11-20T17:05:23.527Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99f-calc-tables on Pro data-1m-v1: failed, peak n/a (2026-11-20T11:04:13Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
```

**Screenshot: the refresh error of v99f-calc-tables on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v99f-calc-tables-refresh-error.png**

## Log

```
2026-11-20T16:56:14Z run 20261120T165357Z-v99f-ce5e: variant=v99f-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T16:56:17Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T16:56:56Z Pro: updated v99f-calc-tables from the F64 workspace (22 files)
2026-11-20T16:56:57Z Pro: v99f-calc-tables is 0ab28c16-fec1-459d-9a1d-545cd285070a, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T16:57:13Z Pro: model size in memory before the refresh: None MB
2026-11-20T16:57:13Z Pro: standard refresh started
2026-11-20T17:05:45Z Pro: refresh failed (Failed) other
```
