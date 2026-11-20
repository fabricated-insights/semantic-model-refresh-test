# Harness run 20261120T003103Z-v24a-ce5e

- Task: refresh
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e6d43fa6-4f9a-44f9-92e8-a99237156ff8
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request d9d2130f-302c-4245-9c96-72bc70074d83, 2026-11-20T00:32:15.63Z to 2026-11-20T00:33:04.39Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v24a-second-fact on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T06:07:50Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T00:31:47Z run 20261120T003103Z-v24a-ce5e: variant=v24a-second-fact data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T00:31:49Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T00:32:06Z Pro: updated v24a-second-fact from the F64 workspace (13 files)
2026-11-20T00:32:07Z Pro: v24a-second-fact is 1010796b-d670-4f9d-a35e-9823ea1138f1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:32:15Z Pro: model size in memory before the refresh: None MB
2026-11-20T00:32:15Z Pro: standard refresh started
2026-11-20T00:33:15Z Pro: refresh refreshed (Completed) 
2026-11-20T00:33:15Z Pro: model size in memory right after the refresh: None MB
```
