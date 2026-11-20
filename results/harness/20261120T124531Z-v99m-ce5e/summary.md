# Harness run 20261120T124531Z-v99m-ce5e

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1a423890-22ee-416c-aa82-24ad08174f8d
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 31d21ef6-d3fb-483c-a78e-4b3e1da6a9f9, 2026-11-20T12:48:29.17Z to 2026-11-20T12:49:33.757Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99m-baseline-pq on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T06:46:59Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T12:47:56Z run 20261120T124531Z-v99m-ce5e: variant=v99m-baseline-pq data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T12:47:58Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T12:48:09Z Pro: updated v99m-baseline-pq from the F64 workspace (16 files)
2026-11-20T12:48:10Z Pro: v99m-baseline-pq is 5a069a77-4a12-426b-9c17-c69217c2a77f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:48:28Z Pro: model size in memory before the refresh: None MB
2026-11-20T12:48:29Z Pro: standard refresh started
2026-11-20T12:49:59Z Pro: refresh refreshed (Completed) 
2026-11-20T12:49:59Z Pro: model size in memory right after the refresh: None MB
```
