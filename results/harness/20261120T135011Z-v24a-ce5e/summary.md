# Harness run 20261120T135011Z-v24a-ce5e

- Task: refresh
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1213d5d8-c410-499c-8258-37e83112d4a6
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request cc6d210a-d164-4b07-98dc-3cc6c6431708, 2026-11-20T13:53:02.32Z to 2026-11-20T13:53:50.853Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v24a-second-fact on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T07:55:48Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T13:52:30Z run 20261120T135011Z-v24a-ce5e: variant=v24a-second-fact data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T13:52:33Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T13:52:44Z Pro: updated v24a-second-fact from the F64 workspace (13 files)
2026-11-20T13:52:45Z Pro: v24a-second-fact is 1010796b-d670-4f9d-a35e-9823ea1138f1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:53:02Z Pro: model size in memory before the refresh: None MB
2026-11-20T13:53:02Z Pro: standard refresh started
2026-11-20T13:54:02Z Pro: refresh refreshed (Completed) 
2026-11-20T13:54:02Z Pro: model size in memory right after the refresh: None MB
```
