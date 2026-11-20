# Harness run 20261120T071148Z-v99q-ce5e

- Task: refresh
- Variant: v99q-customer-stats
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 8be50ea8-d41a-4773-b75b-488f73c66e92
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 68effe2b-92b3-4c6c-a8c5-bd00477972de, 2026-11-20T07:14:42.673Z to 2026-11-20T07:15:57.43Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99q-customer-stats on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T15:45:47Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T07:14:03Z run 20261120T071148Z-v99q-ce5e: variant=v99q-customer-stats data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T07:14:07Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T07:14:26Z Pro: updated v99q-customer-stats from the F64 workspace (17 files)
2026-11-20T07:14:28Z Pro: v99q-customer-stats is cb418f0d-011c-4722-8b2d-68fc739e28d9, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:14:42Z Pro: model size in memory before the refresh: None MB
2026-11-20T07:14:42Z Pro: standard refresh started
2026-11-20T07:16:12Z Pro: refresh refreshed (Completed) 
2026-11-20T07:16:12Z Pro: model size in memory right after the refresh: None MB
```
