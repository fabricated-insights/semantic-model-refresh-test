# Harness run 20261119T225923Z-v31-9352

- Task: refresh
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 50e92a88-9641-4378-b812-c06ab498e05f
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 2 min, CPU n/a, rows n/a, model 317 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request b8368cc1-6420-4ec2-b26a-1d7a45252e46, 2026-11-19T23:02:10.543 to 2026-11-19T23:03:58.17, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v31-calc-columns-row on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T13:32:46Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 234 MB. The refresh may use the SKU maximum minus this: 2,832 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T23:01:38Z run 20261119T225923Z-v31-9352: variant=v31-calc-columns-row data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T23:01:45Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:01:51Z F2: v31-calc-columns-row is a58404cc-fc6f-49b8-acb7-d6337e669dd6, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:02:10Z F2: model size in memory before the refresh: 233.5 MB
2026-11-19T23:02:11Z F2: refresh started, request b8368cc1-6420-4ec2-b26a-1d7a45252e46
2026-11-19T23:04:21Z F2: refresh refreshed (Completed) 
2026-11-19T23:04:23Z F2: model size in memory right after the refresh: 316.8 MB
```
