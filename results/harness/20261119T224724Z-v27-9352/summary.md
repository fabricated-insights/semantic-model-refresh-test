# Harness run 20261119T224724Z-v27-9352

- Task: refresh
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: baa880e6-1cb1-4487-af2d-9d43351049f0
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 93 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request affb54d5-39ca-4cdb-b702-08a61d58b7c2, 2026-11-19T22:48:23.517 to 2026-11-19T22:49:33.503, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v27-high-cardinality-visuals on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T13:12:59Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 3,000 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T22:47:57Z run 20261119T224724Z-v27-9352: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T22:48:04Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:48:08Z F2: v27-high-cardinality-visuals is d131c50b-c0d3-4117-869e-232e7514754a, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:48:23Z F2: model size in memory before the refresh: 66.2 MB
2026-11-19T22:48:23Z F2: refresh started, request affb54d5-39ca-4cdb-b702-08a61d58b7c2
2026-11-19T22:49:34Z F2: refresh refreshed (Completed) 
2026-11-19T22:49:35Z F2: model size in memory right after the refresh: 92.7 MB
```
