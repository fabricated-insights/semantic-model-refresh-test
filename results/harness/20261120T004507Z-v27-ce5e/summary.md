# Harness run 20261120T004507Z-v27-ce5e

- Task: refresh
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 349fe865-c5f7-42e8-a99c-5a7d10e7efa1
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 9e74ee6a-224a-41dd-8fb4-a8965a5e2118, 2026-11-20T00:47:47.327Z to 2026-11-20T00:48:33.127Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v27-high-cardinality-visuals on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T06:34:05Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T00:47:12Z run 20261120T004507Z-v27-ce5e: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T00:47:15Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T00:47:32Z Pro: updated v27-high-cardinality-visuals from the F64 workspace (12 files)
2026-11-20T00:47:33Z Pro: v27-high-cardinality-visuals is 747cf1df-8e4c-4923-80cf-8a35631068a1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:47:47Z Pro: model size in memory before the refresh: None MB
2026-11-20T00:47:47Z Pro: standard refresh started
2026-11-20T00:48:47Z Pro: refresh refreshed (Completed) 
2026-11-20T00:48:47Z Pro: model size in memory right after the refresh: None MB
```
