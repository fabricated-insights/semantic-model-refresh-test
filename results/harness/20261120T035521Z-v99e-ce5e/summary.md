# Harness run 20261120T035521Z-v99e-ce5e

- Task: refresh
- Variant: v99e-sales-flat
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 58c75def-8564-4b89-ae53-0e054b62f328
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 16 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 0648b86c-2607-409e-ad8b-5cf879f8f211, 2026-11-20T03:56:48.25Z to 2026-11-20T04:12:31.52Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99e-sales-flat on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T11:30:15Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T03:55:58Z run 20261120T035521Z-v99e-ce5e: variant=v99e-sales-flat data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T03:56:00Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T03:56:39Z Pro: updated v99e-sales-flat from the F64 workspace (20 files)
2026-11-20T03:56:40Z Pro: v99e-sales-flat is 501ed679-2c3e-4eb5-9103-ebd582eec18f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T03:56:48Z Pro: model size in memory before the refresh: None MB
2026-11-20T03:56:48Z Pro: standard refresh started
2026-11-20T04:12:50Z Pro: refresh refreshed (Completed) 
2026-11-20T04:12:50Z Pro: model size in memory right after the refresh: None MB
```
