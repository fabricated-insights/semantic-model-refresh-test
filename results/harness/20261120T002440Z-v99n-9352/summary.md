# Harness run 20261120T002440Z-v99n-9352

- Task: refresh
- Variant: v99n-text-staging
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 950466af-b5f3-44f6-a8cc-49125493bd43
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 9 min, CPU n/a, rows n/a, model 124 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request a5f37f2f-e7b9-46a0-aa96-4ec87ee2f54c, 2026-11-20T00:27:34.71 to 2026-11-20T00:36:23.95, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99n-text-staging on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 91 MB. The refresh may use the SKU maximum minus this: 2,975 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T00:27:04Z run 20261120T002440Z-v99n-9352: variant=v99n-text-staging data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-20T00:27:12Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T00:27:15Z F2: v99n-text-staging is b2065aaa-ade1-440a-a047-065386e3f814, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:27:34Z F2: model size in memory before the refresh: 90.7 MB
2026-11-20T00:27:35Z F2: refresh started, request a5f37f2f-e7b9-46a0-aa96-4ec87ee2f54c
2026-11-20T00:36:46Z F2: refresh refreshed (Completed) 
2026-11-20T00:36:48Z F2: model size in memory right after the refresh: 124.3 MB
```
