# Harness run 20261120T072411Z-v20-ce5e

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ac07a8df-9a11-4b52-9de8-556bdde1b84b
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 7 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 0d5d1da1-a04b-4e05-af27-e53d8194b6f2, 2026-11-20T07:25:22.077Z to 2026-11-20T07:32:28.687Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v20-pq-sort on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T00:11:28Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T07:24:53Z run 20261120T072411Z-v20-ce5e: variant=v20-pq-sort data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T07:24:55Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T07:25:12Z Pro: updated v20-pq-sort from the F64 workspace (12 files)
2026-11-20T07:25:14Z Pro: v20-pq-sort is 9ba227b5-b6d9-4408-802d-1748ad2c3722, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:25:21Z Pro: model size in memory before the refresh: None MB
2026-11-20T07:25:22Z Pro: standard refresh started
2026-11-20T07:32:53Z Pro: refresh refreshed (Completed) 
2026-11-20T07:32:53Z Pro: model size in memory right after the refresh: None MB
```
