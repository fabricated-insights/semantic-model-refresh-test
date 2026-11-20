# Harness run 20261120T011212Z-v33-ce5e

- Task: refresh
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 64b04f27-8a2f-4c02-aa43-650c651220c4
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request cfade68b-b309-4486-ade3-b7ef210c737d, 2026-11-20T01:15:26.107Z to 2026-11-20T01:16:13.92Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v33-auto-date-time on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T14:41:05Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T01:14:30Z run 20261120T011212Z-v33-ce5e: variant=v33-auto-date-time data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T01:14:35Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T01:15:10Z Pro: updated v33-auto-date-time from the F64 workspace (16 files)
2026-11-20T01:15:12Z Pro: v33-auto-date-time is 19dc9ffc-6b26-46b1-b855-4c4f620ad74b, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T01:15:25Z Pro: model size in memory before the refresh: None MB
2026-11-20T01:15:26Z Pro: standard refresh started
2026-11-20T01:16:26Z Pro: refresh refreshed (Completed) 
2026-11-20T01:16:26Z Pro: model size in memory right after the refresh: None MB
```
