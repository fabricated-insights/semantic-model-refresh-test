# Harness run 20261120T001857Z-v99m-9352

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 77c4891b-9614-4e87-a19a-9465fd83094d
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 136 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 4e9501b8-8990-4cd9-8a6c-7c518d74ab4e, 2026-11-20T00:21:41.323 to 2026-11-20T00:23:00.9, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99m-baseline-pq on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 101 MB. The refresh may use the SKU maximum minus this: 2,965 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T00:21:12Z run 20261120T001857Z-v99m-9352: variant=v99m-baseline-pq data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-20T00:21:18Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T00:21:21Z F2: v99m-baseline-pq is 0a694766-b436-46c3-af72-c14052c8b3d2, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:21:41Z F2: model size in memory before the refresh: 101.3 MB
2026-11-20T00:21:41Z F2: refresh started, request 4e9501b8-8990-4cd9-8a6c-7c518d74ab4e
2026-11-20T00:23:21Z F2: refresh refreshed (Completed) 
2026-11-20T00:23:23Z F2: model size in memory right after the refresh: 136.1 MB
```
