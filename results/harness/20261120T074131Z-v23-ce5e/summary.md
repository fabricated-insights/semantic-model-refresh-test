# Harness run 20261120T074131Z-v23-ce5e

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 0f77035e-54e4-4c1e-b3d5-decc1694013e
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 5ac4a4a6-fc27-472f-93ad-a5e929a2bda1, 2026-11-20T07:44:22.973Z to 2026-11-20T07:45:25.897Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v23-dax-calc-tables on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T00:26:20Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T07:43:46Z run 20261120T074131Z-v23-ce5e: variant=v23-dax-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T07:43:49Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T07:44:06Z Pro: updated v23-dax-calc-tables from the F64 workspace (16 files)
2026-11-20T07:44:07Z Pro: v23-dax-calc-tables is bba19b1a-80c0-4e0d-9deb-14134f1a4c29, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:44:22Z Pro: model size in memory before the refresh: None MB
2026-11-20T07:44:22Z Pro: standard refresh started
2026-11-20T07:45:53Z Pro: refresh refreshed (Completed) 
2026-11-20T07:45:53Z Pro: model size in memory right after the refresh: None MB
```
