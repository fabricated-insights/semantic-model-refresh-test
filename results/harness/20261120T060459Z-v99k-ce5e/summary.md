# Harness run 20261120T060459Z-v99k-ce5e

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: abf01494-742b-4b33-921d-0d1b5c04b8a8
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 15 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 15ce7ca6-2db0-459a-ae78-76723b503d46, 2026-11-20T06:08:06.66Z to 2026-11-20T06:23:10.18Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99k-no-buffers on Pro data-1m-v1: refreshed, peak n/a (2026-11-16T23:43:58Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T06:07:29Z run 20261120T060459Z-v99k-ce5e: variant=v99k-no-buffers data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T06:07:32Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T06:07:49Z Pro: updated v99k-no-buffers from the F64 workspace (18 files)
2026-11-20T06:07:50Z Pro: v99k-no-buffers is 6d087e69-54e7-429e-93c1-4264a5d3b2e7, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T06:08:06Z Pro: model size in memory before the refresh: None MB
2026-11-20T06:08:06Z Pro: standard refresh started
2026-11-20T06:23:38Z Pro: refresh refreshed (Completed) 
2026-11-20T06:23:38Z Pro: model size in memory right after the refresh: None MB
```
