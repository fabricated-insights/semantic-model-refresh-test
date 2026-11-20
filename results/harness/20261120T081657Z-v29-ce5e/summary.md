# Harness run 20261120T081657Z-v29-ce5e

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 06838dc7-0928-401b-9506-48c3f90bf68b
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 587b34c9-3200-450f-8aae-690ec7b49ff4, 2026-11-20T08:20:03.507Z to 2026-11-20T08:20:49.867Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v29-keys-as-text on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T00:56:40Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T08:19:33Z run 20261120T081657Z-v29-ce5e: variant=v29-keys-as-text data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T08:19:36Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T08:19:45Z Pro: updated v29-keys-as-text from the F64 workspace (12 files)
2026-11-20T08:19:46Z Pro: v29-keys-as-text is ac88cedc-9084-411b-8388-2fd68c96a7ee, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:20:03Z Pro: model size in memory before the refresh: None MB
2026-11-20T08:20:03Z Pro: standard refresh started
2026-11-20T08:21:03Z Pro: refresh refreshed (Completed) 
2026-11-20T08:21:03Z Pro: model size in memory right after the refresh: None MB
```
