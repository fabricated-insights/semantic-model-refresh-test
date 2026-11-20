# Harness run 20261120T181856Z-v99l-ce5e

- Task: refresh
- Variant: v99l-no-calc-columns
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 4cb77aa8-071b-474e-821c-56ff8f72fc57
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 13 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request b67d154f-90f0-45f5-92ae-c9c729cbfb97, 2026-11-20T18:21:54.777Z to 2026-11-20T18:34:58.733Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99l-no-calc-columns on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T12:44:59Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T18:21:11Z run 20261120T181856Z-v99l-ce5e: variant=v99l-no-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T18:21:14Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T18:21:37Z Pro: updated v99l-no-calc-columns from the F64 workspace (18 files)
2026-11-20T18:21:38Z Pro: v99l-no-calc-columns is 0f6c29d2-64ea-4290-8edb-60429d55affa, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T18:21:54Z Pro: model size in memory before the refresh: None MB
2026-11-20T18:21:54Z Pro: standard refresh started
2026-11-20T18:35:26Z Pro: refresh refreshed (Completed) 
2026-11-20T18:35:26Z Pro: model size in memory right after the refresh: None MB
```
