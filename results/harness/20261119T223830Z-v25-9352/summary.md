# Harness run 20261119T223830Z-v25-9352

- Task: refresh
- Variant: v25-many-to-many
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 63136441-189a-484a-8566-20a1eaeb58c1
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 98 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 99eb8e57-065b-41d7-8ddb-62aeb98ddd71, 2026-11-19T22:41:30.223 to 2026-11-19T22:42:33.62, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v25-many-to-many on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T13:04:59Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 71 MB. The refresh may use the SKU maximum minus this: 2,995 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T22:40:48Z run 20261119T223830Z-v25-9352: variant=v25-many-to-many data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T22:41:00Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:41:05Z F2: v25-many-to-many is 482ccae8-be74-482a-9196-84137a9ecb4a, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:41:30Z F2: model size in memory before the refresh: 70.6 MB
2026-11-19T22:41:30Z F2: refresh started, request 99eb8e57-065b-41d7-8ddb-62aeb98ddd71
2026-11-19T22:42:40Z F2: refresh refreshed (Completed) 
2026-11-19T22:42:41Z F2: model size in memory right after the refresh: 98.1 MB
```
