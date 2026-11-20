# Harness run 20261120T135836Z-v25-ce5e

- Task: refresh
- Variant: v25-many-to-many
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ca883dc5-0395-4bfc-a885-13eba2f40f48
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 75c7fde4-dc4c-491b-b59b-c9914d2b0028, 2026-11-20T14:00:07.39Z to 2026-11-20T14:00:58.487Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v25-many-to-many on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T08:07:04Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T13:59:41Z run 20261120T135836Z-v25-ce5e: variant=v25-many-to-many data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T13:59:45Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T13:59:56Z Pro: updated v25-many-to-many from the F64 workspace (13 files)
2026-11-20T13:59:57Z Pro: v25-many-to-many is 61112feb-5659-4f15-b98d-a38763ac31b2, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:00:07Z Pro: model size in memory before the refresh: None MB
2026-11-20T14:00:07Z Pro: standard refresh started
2026-11-20T14:01:07Z Pro: refresh refreshed (Completed) 
2026-11-20T14:01:07Z Pro: model size in memory right after the refresh: None MB
```
