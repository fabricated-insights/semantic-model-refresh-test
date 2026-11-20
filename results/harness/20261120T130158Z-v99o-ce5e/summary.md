# Harness run 20261120T130158Z-v99o-ce5e

- Task: refresh
- Variant: v99o-sorts
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 4069362b-c748-4373-b19e-dd774387e7b0
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 4 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 8283da4c-2c25-4eb1-9e4f-1c1ca990edd2, 2026-11-20T13:05:10.817Z to 2026-11-20T13:09:30.81Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99o-sorts on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T07:05:40Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T13:04:35Z run 20261120T130158Z-v99o-ce5e: variant=v99o-sorts data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T13:04:38Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T13:04:50Z Pro: updated v99o-sorts from the F64 workspace (16 files)
2026-11-20T13:04:51Z Pro: v99o-sorts is e2e544a9-720c-4719-97eb-0294c6aec895, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:05:10Z Pro: model size in memory before the refresh: None MB
2026-11-20T13:05:10Z Pro: standard refresh started
2026-11-20T13:09:41Z Pro: refresh refreshed (Completed) 
2026-11-20T13:09:41Z Pro: model size in memory right after the refresh: None MB
```
