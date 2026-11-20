# Harness run 20261120T013555Z-v36-ce5e

- Task: refresh
- Variant: v36-calc-summary-month-grain
- Data tag: data-10m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: fd4bcec9-988b-4ab2-ad47-0b030a25fce4
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 10 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request cbd562ec-12bd-46a2-afcd-8bd4966348a0, 2026-11-20T01:38:58.223Z to 2026-11-20T01:48:44.49Z, workspace at ?, DataTag read back data-10m-v1
- Numbers from: refresh API
- Previous harness run of v36-calc-summary-month-grain on Pro data-10m-v1: failed, peak n/a (2026-11-17T10:52:27Z).
- No v00-baseline harness run with a measured peak on Pro data-10m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Unable to save the changes since the new dataset of size 1100 MB exceeds the limit of 1024 MB. If the dataset is hosted on a PowerBI Premium capacity, you may also reach out to your capacity administrator to see if the limit can be adjusted.
```

**Screenshot: the refresh error of v36-calc-summary-month-grain on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v36-calc-summary-month-grain-refresh-error.png**

## Log

```
2026-11-20T01:38:21Z run 20261120T013555Z-v36-ce5e: variant=v36-calc-summary-month-grain data_tag=data-10m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T01:38:23Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T01:38:40Z Pro: updated v36-calc-summary-month-grain from the F64 workspace (16 files)
2026-11-20T01:38:41Z Pro: v36-calc-summary-month-grain is a8869fbf-57b2-47cc-b053-c1fc95363f49, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T01:38:57Z Pro: model size in memory before the refresh: None MB
2026-11-20T01:38:58Z Pro: standard refresh started
2026-11-20T01:48:59Z Pro: refresh failed (Failed) other
```
