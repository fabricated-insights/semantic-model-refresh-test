# Harness run 20261120T132539Z-v20-ce5e

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 9719d01d-9461-48da-a56e-85836d9f0bde
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 7 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request a1c4984a-0ec8-4755-a5b3-84277b72142f, 2026-11-20T13:26:42.06Z to 2026-11-20T13:33:22.527Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v20-pq-sort on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T07:32:53Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T13:26:13Z run 20261120T132539Z-v20-ce5e: variant=v20-pq-sort data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T13:26:15Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T13:26:31Z Pro: updated v20-pq-sort from the F64 workspace (12 files)
2026-11-20T13:26:32Z Pro: v20-pq-sort is 9ba227b5-b6d9-4408-802d-1748ad2c3722, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:26:41Z Pro: model size in memory before the refresh: None MB
2026-11-20T13:26:41Z Pro: standard refresh started
2026-11-20T13:33:43Z Pro: refresh refreshed (Completed) 
2026-11-20T13:33:43Z Pro: model size in memory right after the refresh: None MB
```
