# Harness run 20261120T011911Z-v35-ce5e

- Task: refresh
- Variant: v35-calc-tables-four-copies
- Data tag: data-10m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: b9b768a0-0c0a-4b72-8786-776b6d665219
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 13 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request f254af0b-9068-4a46-b7cd-7cc3069f7d23, 2026-11-20T01:21:57.833Z to 2026-11-20T01:35:14.6Z, workspace at ?, DataTag read back data-10m-v1
- Numbers from: refresh API
- Previous harness run of v35-calc-tables-four-copies on Pro data-10m-v1: failed, peak n/a (2026-11-17T10:19:09Z).
- No v00-baseline harness run with a measured peak on Pro data-10m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Unable to save the changes since the new dataset of size 2189 MB exceeds the limit of 1024 MB. If the dataset is hosted on a PowerBI Premium capacity, you may also reach out to your capacity administrator to see if the limit can be adjusted.
```

**Screenshot: the refresh error of v35-calc-tables-four-copies on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v35-calc-tables-four-copies-refresh-error.png**

## Log

```
2026-11-20T01:21:24Z run 20261120T011911Z-v35-ce5e: variant=v35-calc-tables-four-copies data_tag=data-10m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T01:21:26Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T01:21:43Z Pro: updated v35-calc-tables-four-copies from the F64 workspace (16 files)
2026-11-20T01:21:44Z Pro: v35-calc-tables-four-copies is efd608fe-a1a6-4cac-9fa4-0d7057cd6624, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T01:21:57Z Pro: model size in memory before the refresh: None MB
2026-11-20T01:21:57Z Pro: standard refresh started
2026-11-20T01:35:29Z Pro: refresh failed (Failed) other
```
