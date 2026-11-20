# Harness run 20261120T183837Z-v99n-ce5e

- Task: refresh
- Variant: v99n-text-staging
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3a76d0cc-daec-4441-aa5d-fb1cf8afad07
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 5 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 8c54d994-e5f4-4747-8533-8b85b3d375a7, 2026-11-20T18:39:40.24Z to 2026-11-20T18:45:07.633Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99n-text-staging on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T13:01:34Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T18:39:15Z run 20261120T183837Z-v99n-ce5e: variant=v99n-text-staging data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T18:39:17Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T18:39:28Z Pro: updated v99n-text-staging from the F64 workspace (16 files)
2026-11-20T18:39:29Z Pro: v99n-text-staging is 7a89f3dd-ca6e-4836-b3b2-383ccd224876, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T18:39:39Z Pro: model size in memory before the refresh: None MB
2026-11-20T18:39:40Z Pro: standard refresh started
2026-11-20T18:45:11Z Pro: refresh refreshed (Completed) 
2026-11-20T18:45:11Z Pro: model size in memory right after the refresh: None MB
```
