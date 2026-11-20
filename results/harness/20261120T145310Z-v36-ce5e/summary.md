# Harness run 20261120T145310Z-v36-ce5e

- Task: refresh
- Variant: v36-calc-summary-month-grain
- Data tag: data-10m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3796d269-ffa8-4c40-9323-8dd0eac17324
- Refresh parallelism requested: 6

## Pro

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 15 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 3b6094ff-2508-4711-8312-01c915523fe1, 2026-11-20T14:55:41.643Z to 2026-11-20T15:10:43Z, workspace at ?, DataTag read back data-10m-v1
- Numbers from: refresh API
- Previous harness run of v36-calc-summary-month-grain on Pro data-10m-v1: failed, peak n/a (2026-11-20T09:06:24Z).
- No v00-baseline harness run with a measured peak on Pro data-10m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Unable to save the changes since the new dataset of size 1095 MB exceeds the limit of 1024 MB. If the dataset is hosted on a PowerBI Premium capacity, you may also reach out to your capacity administrator to see if the limit can be adjusted.
```

**Screenshot: the refresh error of v36-calc-summary-month-grain on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v36-calc-summary-month-grain-refresh-error.png**

## Log

```
2026-11-20T14:55:16Z run 20261120T145310Z-v36-ce5e: variant=v36-calc-summary-month-grain data_tag=data-10m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T14:55:18Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T14:55:23Z Pro: updated v36-calc-summary-month-grain from the F64 workspace (16 files)
2026-11-20T14:55:24Z Pro: v36-calc-summary-month-grain is a8869fbf-57b2-47cc-b053-c1fc95363f49, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T14:55:41Z Pro: model size in memory before the refresh: None MB
2026-11-20T14:55:41Z Pro: standard refresh started
2026-11-20T15:10:44Z Pro: refresh failed (Failed) other
```
