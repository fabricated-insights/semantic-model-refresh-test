# Harness run 20261120T023236Z-v99b-ce5e

- Task: refresh
- Variant: v99b-one-sales-copy
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 4d2bfac5-13f0-469e-87fc-2f2574ea088f
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 24 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 6e1f3e81-0046-41f5-b07c-dde2872b5960, 2026-11-20T02:35:48.453Z to 2026-11-20T02:59:21.303Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99b-one-sales-copy on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T18:29:53Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T02:34:50Z run 20261120T023236Z-v99b-ce5e: variant=v99b-one-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T02:34:53Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T02:35:32Z Pro: updated v99b-one-sales-copy from the F64 workspace (18 files)
2026-11-20T02:35:33Z Pro: v99b-one-sales-copy is 1c2a3fcf-c1d3-4055-9c06-ead16a7c0f62, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T02:35:48Z Pro: model size in memory before the refresh: None MB
2026-11-20T02:35:48Z Pro: standard refresh started
2026-11-20T02:59:21Z Pro: refresh refreshed (Completed) 
2026-11-20T02:59:21Z Pro: model size in memory right after the refresh: None MB
```
