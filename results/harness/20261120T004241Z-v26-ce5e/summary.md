# Harness run 20261120T004241Z-v26-ce5e

- Task: refresh
- Variant: v26-bad-dax
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f71425e9-0f98-4553-8866-d8402e80bbe6
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 020ee5e6-4094-4fbf-845e-e7b195c4cc7e, 2026-11-20T00:43:43.323Z to 2026-11-20T00:44:28.393Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v26-bad-dax on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T06:27:32Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T00:43:13Z run 20261120T004241Z-v26-ce5e: variant=v26-bad-dax data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T00:43:16Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T00:43:36Z Pro: updated v26-bad-dax from the F64 workspace (12 files)
2026-11-20T00:43:37Z Pro: v26-bad-dax is fd7a0114-741d-460c-8d6e-3c5c90d18558, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:43:43Z Pro: model size in memory before the refresh: None MB
2026-11-20T00:43:43Z Pro: standard refresh started
2026-11-20T00:44:43Z Pro: refresh refreshed (Completed) 
2026-11-20T00:44:43Z Pro: model size in memory right after the refresh: None MB
```
