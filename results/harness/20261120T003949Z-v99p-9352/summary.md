# Harness run 20261120T003949Z-v99p-9352

- Task: refresh
- Variant: v99p-high-cardinality
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 18151e22-fab5-4320-bd0b-d9dcb1ca83c8
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 2 min, CPU n/a, rows n/a, model 209 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 842724ee-632a-48f0-942a-c13a9b5f17a1, 2026-11-20T00:40:40.813 to 2026-11-20T00:42:22.803, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99p-high-cardinality on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 174 MB. The refresh may use the SKU maximum minus this: 2,892 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T00:40:17Z run 20261120T003949Z-v99p-9352: variant=v99p-high-cardinality data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-20T00:40:24Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T00:40:28Z F2: v99p-high-cardinality is cfcfa966-a20a-4051-9ef8-fe02c433ee06, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:40:40Z F2: model size in memory before the refresh: 174.2 MB
2026-11-20T00:40:41Z F2: refresh started, request 842724ee-632a-48f0-942a-c13a9b5f17a1
2026-11-20T00:42:51Z F2: refresh refreshed (Completed) 
2026-11-20T00:42:52Z F2: model size in memory right after the refresh: 209.0 MB
```
