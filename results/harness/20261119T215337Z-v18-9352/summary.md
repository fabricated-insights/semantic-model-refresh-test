# Harness run 20261119T215337Z-v18-9352

- Task: refresh
- Variant: v18-pq-10m-summary
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6cfe371e-c48a-4612-8e69-ae7566e207b4
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 2 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 27d87823-9894-4569-a8cf-fc2816a7ac37, 2026-11-19T21:54:35.213 to 2026-11-19T21:56:05.927, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v18-pq-10m-summary on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 3,000 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T21:54:13Z run 20261119T215337Z-v18-9352: variant=v18-pq-10m-summary data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T21:54:18Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T21:54:19Z F2: v18-pq-10m-summary is 3277d7bd-9d18-4604-ac9f-0503dfe4d3e8, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T21:54:35Z F2: model size in memory before the refresh: 66.2 MB
2026-11-19T21:54:35Z F2: refresh started, request 27d87823-9894-4569-a8cf-fc2816a7ac37
2026-11-19T21:56:15Z F2: refresh refreshed (Completed) 
2026-11-19T21:56:17Z F2: model size in memory right after the refresh: 92.7 MB
```
