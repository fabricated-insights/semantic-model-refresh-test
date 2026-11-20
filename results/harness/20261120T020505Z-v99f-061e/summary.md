# Harness run 20261120T020505Z-v99f-061e

- Task: refresh
- Variant: v99f-calc-tables
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: d020ada5-3d63-45c8-a576-50c46639d069
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 37 min, CPU n/a, rows n/a, model 492 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 59c4d1a8-b00c-4eec-b287-52468a1165b2, 2026-11-20T02:08:29.75 to 2026-11-20T02:45:24.95, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99f-calc-tables on F64 data-1m-v1.
- No v00-baseline harness run with a measured peak on F64 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T02:07:51Z run 20261120T020505Z-v99f-061e: variant=v99f-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T02:08:03Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T02:08:06Z F64: v99f-calc-tables is 841b2a42-15a1-46af-911e-9d8fc71b8909, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T02:08:29Z F64: model size in memory before the refresh: 0.4 MB
2026-11-20T02:08:29Z F64: refresh started, request 59c4d1a8-b00c-4eec-b287-52468a1165b2
2026-11-20T02:45:46Z F64: refresh refreshed (Completed) 
2026-11-20T02:45:46Z F64: monitoring database Monitoring KQL database
2026-11-20T03:06:44Z F64: no ExecutionMetrics event after 20 min
2026-11-20T03:06:48Z F64: model size in memory right after the refresh: 491.7 MB
```
