# Harness run 20261120T134316Z-v23-ce5e

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 68f73612-289b-4582-9a4c-5cecd13f46d5
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 8e8275b7-bd24-48ec-8fd5-730baa240616, 2026-11-20T13:44:24.993Z to 2026-11-20T13:45:25.83Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v23-dax-calc-tables on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T07:45:53Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T13:43:51Z run 20261120T134316Z-v23-ce5e: variant=v23-dax-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T13:43:54Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T13:44:13Z Pro: updated v23-dax-calc-tables from the F64 workspace (16 files)
2026-11-20T13:44:14Z Pro: v23-dax-calc-tables is bba19b1a-80c0-4e0d-9deb-14134f1a4c29, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:44:24Z Pro: model size in memory before the refresh: None MB
2026-11-20T13:44:24Z Pro: standard refresh started
2026-11-20T13:45:55Z Pro: refresh refreshed (Completed) 
2026-11-20T13:45:55Z Pro: model size in memory right after the refresh: None MB
```
