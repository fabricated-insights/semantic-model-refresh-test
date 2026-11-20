# Harness run 20261120T143142Z-v34-ce5e

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: b198f87b-1f0c-4e40-ac06-e19c843d1278
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request c840a348-1850-459b-a53e-8182d32a14e2, 2026-11-20T14:34:31.5Z to 2026-11-20T14:35:17.987Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v34-auto-date-time-no-date-table on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T08:37:28Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T14:33:58Z run 20261120T143142Z-v34-ce5e: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T14:34:03Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T14:34:14Z Pro: updated v34-auto-date-time-no-date-table from the F64 workspace (18 files)
2026-11-20T14:34:15Z Pro: v34-auto-date-time-no-date-table is e7b5d152-c532-43e2-9408-761272f88a1c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:34:31Z Pro: model size in memory before the refresh: None MB
2026-11-20T14:34:31Z Pro: standard refresh started
2026-11-20T14:35:31Z Pro: refresh refreshed (Completed) 
2026-11-20T14:35:31Z Pro: model size in memory right after the refresh: None MB
```
