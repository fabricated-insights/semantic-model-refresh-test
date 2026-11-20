# Harness run 20261120T175838Z-v99k-ce5e

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 4a136451-6ea7-4d62-bf82-65f5c4250091
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 18 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 84457d93-9e75-4127-b205-d198589c7fc1, 2026-11-20T17:59:40.683Z to 2026-11-20T18:18:05.8Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99k-no-buffers on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T12:22:27Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T17:59:04Z run 20261120T175838Z-v99k-ce5e: variant=v99k-no-buffers data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T17:59:07Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T17:59:30Z Pro: updated v99k-no-buffers from the F64 workspace (18 files)
2026-11-20T17:59:31Z Pro: v99k-no-buffers is 6d087e69-54e7-429e-93c1-4264a5d3b2e7, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T17:59:40Z Pro: model size in memory before the refresh: None MB
2026-11-20T17:59:40Z Pro: standard refresh started
2026-11-20T18:18:13Z Pro: refresh refreshed (Completed) 
2026-11-20T18:18:13Z Pro: model size in memory right after the refresh: None MB
```
