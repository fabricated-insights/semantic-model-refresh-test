# Harness run 20261120T011656Z-v34-ce5e

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: b25cb7b6-f301-4b0c-bbbc-e2c3e4ad7b47
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request e61d64ac-5e34-488d-9009-9b9428ddb63c, 2026-11-20T01:17:55.637Z to 2026-11-20T01:18:41.87Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v34-auto-date-time-no-date-table on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T08:54:16Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T01:17:23Z run 20261120T011656Z-v34-ce5e: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T01:17:26Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T01:17:45Z Pro: updated v34-auto-date-time-no-date-table from the F64 workspace (18 files)
2026-11-20T01:17:46Z Pro: v34-auto-date-time-no-date-table is e7b5d152-c532-43e2-9408-761272f88a1c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T01:17:55Z Pro: model size in memory before the refresh: None MB
2026-11-20T01:17:55Z Pro: standard refresh started
2026-11-20T01:18:55Z Pro: refresh refreshed (Completed) 
2026-11-20T01:18:55Z Pro: model size in memory right after the refresh: None MB
```
