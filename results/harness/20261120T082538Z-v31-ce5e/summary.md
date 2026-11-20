# Harness run 20261120T082538Z-v31-ce5e

- Task: refresh
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: c7ed7223-48bc-4139-beeb-defafae6a713
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 13bd39b6-940e-4024-8860-84a58c5c5612, 2026-11-20T08:26:46.19Z to 2026-11-20T08:27:51.633Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v31-calc-columns-row on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T01:06:57Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T08:26:15Z run 20261120T082538Z-v31-ce5e: variant=v31-calc-columns-row data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T08:26:18Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T08:26:35Z Pro: updated v31-calc-columns-row from the F64 workspace (12 files)
2026-11-20T08:26:36Z Pro: v31-calc-columns-row is 9294e5ca-efe7-40c2-be3f-9ea4bb8bf562, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:26:45Z Pro: model size in memory before the refresh: None MB
2026-11-20T08:26:46Z Pro: standard refresh started
2026-11-20T08:28:16Z Pro: refresh refreshed (Completed) 
2026-11-20T08:28:16Z Pro: model size in memory right after the refresh: None MB
```
