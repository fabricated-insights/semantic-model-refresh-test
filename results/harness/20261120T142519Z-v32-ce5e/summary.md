# Harness run 20261120T142519Z-v32-ce5e

- Task: refresh
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a25d153c-08d1-47a5-8076-15381739b6dd
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 1bdc7146-3c5e-4460-b95c-4473c2c66c5a, 2026-11-20T14:26:21.01Z to 2026-11-20T14:27:14.59Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v32-calc-columns-aggregate on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T08:32:57Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T14:25:51Z run 20261120T142519Z-v32-ce5e: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T14:25:54Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T14:26:11Z Pro: updated v32-calc-columns-aggregate from the F64 workspace (12 files)
2026-11-20T14:26:12Z Pro: v32-calc-columns-aggregate is 2d29c913-d071-455f-bc94-f8955108bb1b, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:26:20Z Pro: model size in memory before the refresh: None MB
2026-11-20T14:26:20Z Pro: standard refresh started
2026-11-20T14:27:21Z Pro: refresh refreshed (Completed) 
2026-11-20T14:27:21Z Pro: model size in memory right after the refresh: None MB
```
