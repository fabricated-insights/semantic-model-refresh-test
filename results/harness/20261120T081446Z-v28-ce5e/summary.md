# Harness run 20261120T081446Z-v28-ce5e

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 52cf4347-897b-405c-a8b0-4b6ea1f6e9f5
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 249a3929-83de-40d2-b246-9db5a68c8247, 2026-11-20T08:15:43.05Z to 2026-11-20T08:16:32.32Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v28-types-all-text on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T00:52:45Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T08:15:20Z run 20261120T081446Z-v28-ce5e: variant=v28-types-all-text data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T08:15:23Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T08:15:32Z Pro: updated v28-types-all-text from the F64 workspace (12 files)
2026-11-20T08:15:34Z Pro: v28-types-all-text is 6391583e-bd04-41bb-9d15-92bd6c0a4db7, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:15:42Z Pro: model size in memory before the refresh: None MB
2026-11-20T08:15:42Z Pro: standard refresh started
2026-11-20T08:16:43Z Pro: refresh refreshed (Completed) 
2026-11-20T08:16:43Z Pro: model size in memory right after the refresh: None MB
```
