# Harness run 20261120T190005Z-v99p-ce5e

- Task: refresh
- Variant: v99p-high-cardinality
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ebdf0119-4471-402e-8ba4-3ae897a461c0
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 41b55790-96c2-42c5-9926-00d2e9621fef, 2026-11-20T19:03:38.15Z to 2026-11-20T19:04:38.467Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99p-high-cardinality on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T13:14:32Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T19:02:52Z run 20261120T190005Z-v99p-ce5e: variant=v99p-high-cardinality data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T19:02:54Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T19:03:18Z Pro: updated v99p-high-cardinality from the F64 workspace (17 files)
2026-11-20T19:03:19Z Pro: v99p-high-cardinality is 5489ea18-9291-4d57-a7b5-c8ad13e93441, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T19:03:37Z Pro: model size in memory before the refresh: None MB
2026-11-20T19:03:38Z Pro: standard refresh started
2026-11-20T19:05:08Z Pro: refresh refreshed (Completed) 
2026-11-20T19:05:08Z Pro: model size in memory right after the refresh: None MB
```
