# Harness run 20261120T000137Z-v20-ce5e

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 5d29d87a-4766-4d58-b037-4a889fec407c
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 6 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 02dca7cd-0546-472c-a6f6-68cc2addb515, 2026-11-20T00:04:57.367Z to 2026-11-20T00:11:06.097Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v20-pq-sort on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T09:12:08Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T00:04:20Z run 20261120T000137Z-v20-ce5e: variant=v20-pq-sort data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T00:04:22Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T00:04:39Z Pro: updated v20-pq-sort from the F64 workspace (12 files)
2026-11-20T00:04:40Z Pro: v20-pq-sort is 9ba227b5-b6d9-4408-802d-1748ad2c3722, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:04:57Z Pro: model size in memory before the refresh: None MB
2026-11-20T00:04:57Z Pro: standard refresh started
2026-11-20T00:11:28Z Pro: refresh refreshed (Completed) 
2026-11-20T00:11:28Z Pro: model size in memory right after the refresh: None MB
```
