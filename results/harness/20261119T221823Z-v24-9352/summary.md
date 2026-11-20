# Harness run 20261119T221823Z-v24-9352

- Task: refresh
- Variant: v24-bidirectional
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: d7b21631-526a-4d91-b69e-985ce35fd650
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request cdbef4fb-4d5d-4595-9659-690f3ed8733e, 2026-11-19T22:19:34.353 to 2026-11-19T22:20:41.94, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v24-bidirectional on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T12:45:17Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 3,000 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T22:18:58Z run 20261119T221823Z-v24-9352: variant=v24-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T22:19:08Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:19:16Z F2: v24-bidirectional is cdbee253-9936-4702-b957-38fbad3272fa, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:19:34Z F2: model size in memory before the refresh: 66.2 MB
2026-11-19T22:19:35Z F2: refresh started, request cdbef4fb-4d5d-4595-9659-690f3ed8733e
2026-11-19T22:20:45Z F2: refresh refreshed (Completed) 
2026-11-19T22:20:47Z F2: model size in memory right after the refresh: 92.7 MB
```
