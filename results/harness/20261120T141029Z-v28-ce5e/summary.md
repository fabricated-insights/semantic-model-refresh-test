# Harness run 20261120T141029Z-v28-ce5e

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: c0f1dca2-c83c-4c5a-b610-c76f220ed47f
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request cfd36c3f-a600-4e71-864b-3c41b498e57f, 2026-11-20T14:11:31.053Z to 2026-11-20T14:12:28.707Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v28-types-all-text on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T08:16:43Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T14:11:07Z run 20261120T141029Z-v28-ce5e: variant=v28-types-all-text data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T14:11:10Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T14:11:19Z Pro: updated v28-types-all-text from the F64 workspace (12 files)
2026-11-20T14:11:20Z Pro: v28-types-all-text is 6391583e-bd04-41bb-9d15-92bd6c0a4db7, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:11:29Z Pro: model size in memory before the refresh: None MB
2026-11-20T14:11:31Z Pro: standard refresh started
2026-11-20T14:12:31Z Pro: refresh refreshed (Completed) 
2026-11-20T14:12:31Z Pro: model size in memory right after the refresh: None MB
```
