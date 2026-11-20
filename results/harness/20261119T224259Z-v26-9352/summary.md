# Harness run 20261119T224259Z-v26-9352

- Task: refresh
- Variant: v26-bad-dax
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: d7e6b639-88fe-4a3d-9034-d248d294aa2d
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 6c84d269-b5b9-4d63-a033-9b60a8cae8df, 2026-11-19T22:45:47.003 to 2026-11-19T22:46:56.723, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v26-bad-dax on F2 data-1m-v1: refreshed, peak n/a (2026-11-11T20:25:00Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 3,000 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T22:45:14Z run 20261119T224259Z-v26-9352: variant=v26-bad-dax data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T22:45:19Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:45:22Z F2: v26-bad-dax is e56036af-5114-4745-8442-72f81810a1ee, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:45:46Z F2: model size in memory before the refresh: 66.2 MB
2026-11-19T22:45:47Z F2: refresh started, request 6c84d269-b5b9-4d63-a033-9b60a8cae8df
2026-11-19T22:46:57Z F2: refresh refreshed (Completed) 
2026-11-19T22:46:58Z F2: model size in memory right after the refresh: 92.7 MB
```
