# Harness run 20261119T221209Z-v23-9352

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e8e49baa-f1ca-416c-8e9e-6bbd3252cf03
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 2 min, CPU n/a, rows n/a, model 186 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 073da17f-c1bb-48b9-ad74-1bbb86129d69, 2026-11-19T22:15:28.963 to 2026-11-19T22:17:18.96, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v23-dax-calc-tables on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 150 MB. The refresh may use the SKU maximum minus this: 2,916 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T22:14:26Z run 20261119T221209Z-v23-9352: variant=v23-dax-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T22:14:40Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:15:04Z F2: v23-dax-calc-tables is 2f4dfbe3-0124-42a5-9c38-727f92a830a9, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:15:28Z F2: model size in memory before the refresh: 149.9 MB
2026-11-19T22:15:29Z F2: refresh started, request 073da17f-c1bb-48b9-ad74-1bbb86129d69
2026-11-19T22:17:40Z F2: refresh refreshed (Completed) 
2026-11-19T22:17:41Z F2: model size in memory right after the refresh: 185.5 MB
```
