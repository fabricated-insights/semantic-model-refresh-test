# Harness run 20261119T215012Z-v00-9352

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 8a592588-5c60-45d2-ae5a-519e6ff5afdf
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request a83cc273-c788-47bb-aa1e-e0900ec1d324, 2026-11-19T21:51:22.483 to 2026-11-19T21:52:36.297, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v00-baseline on F2 data-1m-v1: failed, peak n/a (2026-11-19T21:41:44Z).
  - **FLAG: result changed from failed to refreshed**
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 3,000 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T21:50:36Z run 20261119T215012Z-v00-9352: variant=v00-baseline data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T21:50:45Z F2: update from Git f20fbcf1c0f30239000712aeb1056d5b8bcf2fa1 -> eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T21:51:09Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T21:51:22Z F2: model size in memory before the refresh: 66.2 MB
2026-11-19T21:51:22Z F2: refresh started, request a83cc273-c788-47bb-aa1e-e0900ec1d324
2026-11-19T21:53:02Z F2: refresh refreshed (Completed) 
2026-11-19T21:53:06Z F2: model size in memory right after the refresh: 92.7 MB
```
