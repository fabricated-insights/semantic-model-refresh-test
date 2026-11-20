# Harness run 20261120T030004Z-v99c-ce5e

- Task: refresh
- Variant: v99c-crossjoin-only
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: fdce2d06-bfbb-45ab-adb9-b3856fd7d8b7
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 29 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 275c4823-b94b-4e4c-8b46-d84d94264820, 2026-11-20T03:03:45.187Z to 2026-11-20T03:33:12.213Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99c-crossjoin-only on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T20:52:55Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T03:02:47Z run 20261120T030004Z-v99c-ce5e: variant=v99c-crossjoin-only data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T03:02:50Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T03:03:25Z Pro: updated v99c-crossjoin-only from the F64 workspace (18 files)
2026-11-20T03:03:27Z Pro: v99c-crossjoin-only is 6af71876-9875-4b2d-8a55-fbde4a52de4f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T03:03:44Z Pro: model size in memory before the refresh: None MB
2026-11-20T03:03:45Z Pro: standard refresh started
2026-11-20T03:33:19Z Pro: refresh refreshed (Completed) 
2026-11-20T03:33:19Z Pro: model size in memory right after the refresh: None MB
```
