# Harness run 20261119T220728Z-v22-9352

- Task: refresh
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 70a4e114-b87d-414b-b401-650ec8617668
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 3 min, CPU n/a, rows n/a, model 133 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 3ac4c1df-2e07-4aaf-9224-f8fe5fbb5898, 2026-11-19T22:08:30.267 to 2026-11-19T22:11:10.75, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v22-dax-calc-columns on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 98 MB. The refresh may use the SKU maximum minus this: 2,968 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T22:08:03Z run 20261119T220728Z-v22-9352: variant=v22-dax-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T22:08:11Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:08:15Z F2: v22-dax-calc-columns is 2d65ac78-c741-4dcf-8f03-cf8f3686d10f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:08:30Z F2: model size in memory before the refresh: 97.8 MB
2026-11-19T22:08:30Z F2: refresh started, request 3ac4c1df-2e07-4aaf-9224-f8fe5fbb5898
2026-11-19T22:11:40Z F2: refresh refreshed (Completed) 
2026-11-19T22:11:42Z F2: model size in memory right after the refresh: 132.6 MB
```
