# Harness run 20261119T224949Z-v28-9352

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: d51c1ffd-8516-4de9-abd4-b4fa145f231a
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 172 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request c808e794-c409-43e8-bb28-55b47ef67047, 2026-11-19T22:50:39.163 to 2026-11-19T22:51:43.45, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v28-types-all-text on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T13:15:30Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 96 MB. The refresh may use the SKU maximum minus this: 2,970 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T22:50:14Z run 20261119T224949Z-v28-9352: variant=v28-types-all-text data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T22:50:21Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:50:26Z F2: v28-types-all-text is 527da1e4-4584-4e41-aae4-fc3fd0387f67, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:50:39Z F2: model size in memory before the refresh: 95.8 MB
2026-11-19T22:50:41Z F2: refresh started, request c808e794-c409-43e8-bb28-55b47ef67047
2026-11-19T22:51:51Z F2: refresh refreshed (Completed) 
2026-11-19T22:51:55Z F2: model size in memory right after the refresh: 171.5 MB
```
