# Harness run 20261119T230505Z-v32-9352

- Task: refresh
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 9d334d35-e267-4d46-b7d0-dd8c4778e842
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 368 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 4914ba25-be26-4b50-9ce0-83458491fb59, 2026-11-19T23:07:55.56 to 2026-11-19T23:09:19.917, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v32-calc-columns-aggregate on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T13:38:25Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 341 MB. The refresh may use the SKU maximum minus this: 2,725 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T23:07:22Z run 20261119T230505Z-v32-9352: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T23:07:30Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:07:35Z F2: v32-calc-columns-aggregate is 775d81dc-8a41-4f8d-aa5e-a88a0f85de57, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:07:55Z F2: model size in memory before the refresh: 341.3 MB
2026-11-19T23:07:55Z F2: refresh started, request 4914ba25-be26-4b50-9ce0-83458491fb59
2026-11-19T23:09:36Z F2: refresh refreshed (Completed) 
2026-11-19T23:09:38Z F2: model size in memory right after the refresh: 367.9 MB
```
