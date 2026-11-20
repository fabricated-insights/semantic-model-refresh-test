# Harness run 20261120T081151Z-v27-ce5e

- Task: refresh
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 18a20247-36ad-4dfc-8a6e-09b984055e54
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request aa80147b-1e64-46d7-a955-f16de77bf79f, 2026-11-20T08:12:58.047Z to 2026-11-20T08:13:58.863Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v27-high-cardinality-visuals on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T00:48:47Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T08:12:34Z run 20261120T081151Z-v27-ce5e: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T08:12:36Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T08:12:48Z Pro: updated v27-high-cardinality-visuals from the F64 workspace (12 files)
2026-11-20T08:12:49Z Pro: v27-high-cardinality-visuals is 747cf1df-8e4c-4923-80cf-8a35631068a1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:12:57Z Pro: model size in memory before the refresh: None MB
2026-11-20T08:12:58Z Pro: standard refresh started
2026-11-20T08:14:28Z Pro: refresh refreshed (Completed) 
2026-11-20T08:14:28Z Pro: model size in memory right after the refresh: None MB
```
