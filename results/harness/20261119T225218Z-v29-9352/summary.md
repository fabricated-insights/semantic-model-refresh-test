# Harness run 20261119T225218Z-v29-9352

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 8e332fee-f823-4de9-9e9e-23741cd06e1b
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 142 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request c5c42177-9e24-4466-8e66-8820e9e5106b, 2026-11-19T22:55:10.983 to 2026-11-19T22:56:11.693, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v29-keys-as-text on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T13:21:05Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 94 MB. The refresh may use the SKU maximum minus this: 2,972 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T22:54:42Z run 20261119T225218Z-v29-9352: variant=v29-keys-as-text data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T22:54:49Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:54:52Z F2: v29-keys-as-text is eb86148d-c52d-4cf3-9274-8cadec698b9f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:55:10Z F2: model size in memory before the refresh: 93.8 MB
2026-11-19T22:55:11Z F2: refresh started, request c5c42177-9e24-4466-8e66-8820e9e5106b
2026-11-19T22:56:21Z F2: refresh refreshed (Completed) 
2026-11-19T22:56:22Z F2: model size in memory right after the refresh: 141.9 MB
```
