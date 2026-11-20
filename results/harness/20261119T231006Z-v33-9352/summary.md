# Harness run 20261119T231006Z-v33-9352

- Task: refresh
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e4557dd9-a2a6-4641-b053-77324298ef9a
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 96 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 3d7b27db-41e2-4741-a06d-d1009c294c1a, 2026-11-19T23:12:55.333 to 2026-11-19T23:14:03.82, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v33-auto-date-time on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T13:42:08Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 2,996 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T23:12:24Z run 20261119T231006Z-v33-9352: variant=v33-auto-date-time data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T23:12:31Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:12:34Z F2: v33-auto-date-time is 30e0e36a-643f-49ab-82af-1f8214be1ba6, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:12:55Z F2: model size in memory before the refresh: 69.7 MB
2026-11-19T23:12:55Z F2: refresh started, request 3d7b27db-41e2-4741-a06d-d1009c294c1a
2026-11-19T23:14:05Z F2: refresh refreshed (Completed) 
2026-11-19T23:14:07Z F2: model size in memory right after the refresh: 96.2 MB
```
