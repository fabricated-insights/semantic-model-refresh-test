# Harness run 20261120T071631Z-v00-ce5e

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 5aa0de6f-84cb-433a-995b-6d6558692126
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 455c672f-f989-4a4f-afb8-82fa21624087, 2026-11-20T07:19:45.847Z to 2026-11-20T07:20:38.307Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v00-baseline on Pro data-1m-v1: refreshed, peak n/a (2026-11-19T21:54:57Z).
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T07:19:02Z run 20261120T071631Z-v00-ce5e: variant=v00-baseline data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T07:19:05Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T07:19:24Z Pro: updated v00-baseline from the F64 workspace (12 files)
2026-11-20T07:19:25Z Pro: v00-baseline is d617fd07-8a52-4fda-ab69-2b58d0426997, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:19:45Z Pro: model size in memory before the refresh: None MB
2026-11-20T07:19:45Z Pro: standard refresh started
2026-11-20T07:20:46Z Pro: refresh refreshed (Completed) 
2026-11-20T07:20:46Z Pro: model size in memory right after the refresh: None MB
```
