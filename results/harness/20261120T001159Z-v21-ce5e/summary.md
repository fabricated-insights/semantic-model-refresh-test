# Harness run 20261120T001159Z-v21-ce5e

- Task: refresh
- Variant: v21-pq-group-by
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 34e7869e-7f8a-465b-806e-26980c8084eb
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request d8cea3fb-b004-47a0-ac63-78c01a8b3fb9, 2026-11-20T00:14:59.373Z to 2026-11-20T00:16:27.813Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v21-pq-group-by on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T09:21:01Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T00:14:24Z run 20261120T001159Z-v21-ce5e: variant=v21-pq-group-by data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T00:14:27Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T00:14:44Z Pro: updated v21-pq-group-by from the F64 workspace (13 files)
2026-11-20T00:14:45Z Pro: v21-pq-group-by is 70ddbd03-fc62-414e-86c4-ca217ba22a7c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:14:59Z Pro: model size in memory before the refresh: None MB
2026-11-20T00:14:59Z Pro: standard refresh started
2026-11-20T00:16:29Z Pro: refresh refreshed (Completed) 
2026-11-20T00:16:29Z Pro: model size in memory right after the refresh: None MB
```
