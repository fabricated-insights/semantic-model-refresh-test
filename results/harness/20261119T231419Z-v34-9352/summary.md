# Harness run 20261119T231419Z-v34-9352

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 399984c8-82dc-4c72-856b-36560e19484a
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 97 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request ab33f834-f075-4b6b-9774-4f9cd7f37a68, 2026-11-19T23:15:19.14 to 2026-11-19T23:16:44.823, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v34-auto-date-time-no-date-table on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T13:47:14Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 2,996 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T23:14:54Z run 20261119T231419Z-v34-9352: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T23:15:02Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:15:05Z F2: v34-auto-date-time-no-date-table is 3a018001-17d2-4978-b22c-79cf3b55216c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:15:19Z F2: model size in memory before the refresh: 70.3 MB
2026-11-19T23:15:19Z F2: refresh started, request ab33f834-f075-4b6b-9774-4f9cd7f37a68
2026-11-19T23:16:59Z F2: refresh refreshed (Completed) 
2026-11-19T23:17:01Z F2: model size in memory right after the refresh: 96.9 MB
```
