# Harness run 20261119T222103Z-v24a-9352

- Task: refresh
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 461f9ad7-5a12-4781-b8b5-563bdb285739
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model 110 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request b1582155-8059-431c-8499-cfd0ae581446, 2026-11-19T22:24:44.293 to 2026-11-19T22:26:04.767, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v24a-second-fact on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T12:53:09Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 82 MB. The refresh may use the SKU maximum minus this: 2,984 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T22:23:52Z run 20261119T222103Z-v24a-9352: variant=v24a-second-fact data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T22:24:02Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:24:18Z F2: v24a-second-fact is 00e9cd53-9bde-4c52-b82c-ef14e342e946, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:24:44Z F2: model size in memory before the refresh: 82.4 MB
2026-11-19T22:24:46Z F2: refresh started, request b1582155-8059-431c-8499-cfd0ae581446
2026-11-19T22:26:27Z F2: refresh refreshed (Completed) 
2026-11-19T22:26:28Z F2: model size in memory right after the refresh: 110.0 MB
```
