# Harness run 20261119T215518Z-v18-ce5e

- Task: refresh
- Variant: v18-pq-10m-summary
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 7a4bae5a-16f1-44c2-b959-3f9a72e4ecab
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request b3e8594b-4e3d-4b41-9abb-ebd110c94171, 2026-11-19T21:57:54.347Z to 2026-11-19T21:59:11.09Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v18-pq-10m-summary on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T09:29:48Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T21:57:21Z run 20261119T215518Z-v18-ce5e: variant=v18-pq-10m-summary data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-19T21:57:23Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-19T21:57:40Z Pro: updated v18-pq-10m-summary from the F64 workspace (13 files)
2026-11-19T21:57:41Z Pro: v18-pq-10m-summary is 45da3519-8fe1-4fbc-8ef6-9489829c8bb0, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T21:57:54Z Pro: model size in memory before the refresh: None MB
2026-11-19T21:57:54Z Pro: standard refresh started
2026-11-19T21:59:24Z Pro: refresh refreshed (Completed) 
2026-11-19T21:59:24Z Pro: model size in memory right after the refresh: None MB
```
