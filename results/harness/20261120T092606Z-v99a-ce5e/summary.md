# Harness run 20261120T092606Z-v99a-ce5e

- Task: refresh
- Variant: v99a-no-big-calc-tables
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a1d60e65-ed70-42ef-ae0e-17c0cfa4a581
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 18 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 0d53f5e6-29ac-46e8-9c41-c3f3d86c76e1, 2026-11-20T09:29:24.707Z to 2026-11-20T09:47:48.47Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99a-no-big-calc-tables on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T02:31:53Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T09:28:43Z run 20261120T092606Z-v99a-ce5e: variant=v99a-no-big-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T09:28:49Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T09:29:06Z Pro: updated v99a-no-big-calc-tables from the F64 workspace (18 files)
2026-11-20T09:29:07Z Pro: v99a-no-big-calc-tables is dd227607-351c-4da2-9567-c2fd3fd51c22, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:29:24Z Pro: model size in memory before the refresh: None MB
2026-11-20T09:29:24Z Pro: standard refresh started
2026-11-20T09:47:58Z Pro: refresh refreshed (Completed) 
2026-11-20T09:47:58Z Pro: model size in memory right after the refresh: None MB
```
