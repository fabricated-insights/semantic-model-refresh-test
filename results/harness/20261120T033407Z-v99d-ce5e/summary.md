# Harness run 20261120T033407Z-v99d-ce5e

- Task: refresh
- Variant: v99d-power-query
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 28a59a1a-050f-4bcb-9518-24e8a51a1c9e
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 17 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request ec4ce7aa-b970-4e22-be73-2b1cbb859980, 2026-11-20T03:37:11.633Z to 2026-11-20T03:54:22.23Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99d-power-query on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T10:05:05Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T03:36:18Z run 20261120T033407Z-v99d-ce5e: variant=v99d-power-query data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T03:36:21Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T03:36:57Z Pro: updated v99d-power-query from the F64 workspace (18 files)
2026-11-20T03:36:58Z Pro: v99d-power-query is 553edd0b-c792-40ee-876c-a6ffab6df3eb, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T03:37:10Z Pro: model size in memory before the refresh: None MB
2026-11-20T03:37:11Z Pro: standard refresh started
2026-11-20T03:54:44Z Pro: refresh refreshed (Completed) 
2026-11-20T03:54:44Z Pro: model size in memory right after the refresh: None MB
```
