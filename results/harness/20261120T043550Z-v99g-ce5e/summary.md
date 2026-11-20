# Harness run 20261120T043550Z-v99g-ce5e

- Task: refresh
- Variant: v99g-sales-copy
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: c4e41d75-6e95-4d16-8330-6285343e1a08
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 15 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 06601e13-5fae-4864-bea4-91d74b688cb6, 2026-11-20T04:38:59.897Z to 2026-11-20T04:54:23.993Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99g-sales-copy on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T21:26:46Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T04:38:06Z run 20261120T043550Z-v99g-ce5e: variant=v99g-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T04:38:10Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T04:38:43Z Pro: updated v99g-sales-copy from the F64 workspace (23 files)
2026-11-20T04:38:44Z Pro: v99g-sales-copy is 365c91bc-922d-40fa-af7b-6ca43099dddb, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T04:38:59Z Pro: model size in memory before the refresh: None MB
2026-11-20T04:38:59Z Pro: standard refresh started
2026-11-20T04:54:32Z Pro: refresh refreshed (Completed) 
2026-11-20T04:54:32Z Pro: model size in memory right after the refresh: None MB
```
