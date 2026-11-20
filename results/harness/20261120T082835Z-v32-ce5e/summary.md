# Harness run 20261120T082835Z-v32-ce5e

- Task: refresh
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 0a150587-e711-40b4-8f3a-5b18038f439b
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request d4e27061-e138-474f-b90c-66eaf26aadd4, 2026-11-20T08:31:27.513Z to 2026-11-20T08:32:32.903Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v32-calc-columns-aggregate on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T01:11:54Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T08:30:51Z run 20261120T082835Z-v32-ce5e: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T08:30:54Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T08:31:12Z Pro: updated v32-calc-columns-aggregate from the F64 workspace (12 files)
2026-11-20T08:31:13Z Pro: v32-calc-columns-aggregate is 2d29c913-d071-455f-bc94-f8955108bb1b, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:31:27Z Pro: model size in memory before the refresh: None MB
2026-11-20T08:31:27Z Pro: standard refresh started
2026-11-20T08:32:57Z Pro: refresh refreshed (Completed) 
2026-11-20T08:32:57Z Pro: model size in memory right after the refresh: None MB
```
