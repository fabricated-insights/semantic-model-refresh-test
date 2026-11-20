# Harness run 20261120T183611Z-v99m-ce5e

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 39bb430b-4995-4c3f-a7db-15a74f9fe338
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 2a4add99-b3e8-4655-9eaa-98fccf710d50, 2026-11-20T18:37:11.387Z to 2026-11-20T18:38:04.513Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99m-baseline-pq on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T12:49:59Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T18:36:36Z run 20261120T183611Z-v99m-ce5e: variant=v99m-baseline-pq data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T18:36:40Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T18:36:59Z Pro: updated v99m-baseline-pq from the F64 workspace (16 files)
2026-11-20T18:37:00Z Pro: v99m-baseline-pq is 5a069a77-4a12-426b-9c17-c69217c2a77f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T18:37:11Z Pro: model size in memory before the refresh: None MB
2026-11-20T18:37:11Z Pro: standard refresh started
2026-11-20T18:38:11Z Pro: refresh refreshed (Completed) 
2026-11-20T18:38:11Z Pro: model size in memory right after the refresh: None MB
```
