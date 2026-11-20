# Harness run 20261120T102142Z-v99d-ce5e

- Task: refresh
- Variant: v99d-power-query
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: d4d3e352-4ed5-4cfb-8087-ec2cb9ba4f43
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 18 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 82c5635f-4930-4c3c-924c-2af2d7734b1a, 2026-11-20T10:22:54.373Z to 2026-11-20T10:40:53.633Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99d-power-query on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T03:54:44Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T10:22:21Z run 20261120T102142Z-v99d-ce5e: variant=v99d-power-query data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T10:22:24Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T10:22:44Z Pro: updated v99d-power-query from the F64 workspace (18 files)
2026-11-20T10:22:45Z Pro: v99d-power-query is 553edd0b-c792-40ee-876c-a6ffab6df3eb, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T10:22:54Z Pro: model size in memory before the refresh: None MB
2026-11-20T10:22:54Z Pro: standard refresh started
2026-11-20T10:40:57Z Pro: refresh refreshed (Completed) 
2026-11-20T10:40:57Z Pro: model size in memory right after the refresh: None MB
```
