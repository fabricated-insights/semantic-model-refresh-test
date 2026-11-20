# Harness run 20261119T225644Z-v30-9352

- Task: refresh
- Variant: v30-double-instead-of-fixed
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f1af260a-a419-42d6-82c4-db8b6775c4d1
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request c210646e-c5dc-49bc-8f9c-e445f24c236b, 2026-11-19T22:57:43.44 to 2026-11-19T22:58:42.25, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v30-double-instead-of-fixed on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T13:26:28Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 3,000 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T22:57:20Z run 20261119T225644Z-v30-9352: variant=v30-double-instead-of-fixed data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T22:57:25Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:57:28Z F2: v30-double-instead-of-fixed is e71e9c1f-9d96-4a79-af3c-f3d7d43f5d66, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:57:43Z F2: model size in memory before the refresh: 66.4 MB
2026-11-19T22:57:43Z F2: refresh started, request c210646e-c5dc-49bc-8f9c-e445f24c236b
2026-11-19T22:58:53Z F2: refresh refreshed (Completed) 
2026-11-19T22:58:55Z F2: model size in memory right after the refresh: 92.9 MB
```
