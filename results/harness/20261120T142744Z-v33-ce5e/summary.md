# Harness run 20261120T142744Z-v33-ce5e

- Task: refresh
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6e89d350-c746-4422-83e6-d3ce0176cc97
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request b09057ac-e3d0-423d-8b20-f496d8a07c43, 2026-11-20T14:30:25.08Z to 2026-11-20T14:31:10.557Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v33-auto-date-time on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T08:35:15Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T14:29:56Z run 20261120T142744Z-v33-ce5e: variant=v33-auto-date-time data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T14:29:58Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T14:30:08Z Pro: updated v33-auto-date-time from the F64 workspace (16 files)
2026-11-20T14:30:09Z Pro: v33-auto-date-time is 19dc9ffc-6b26-46b1-b855-4c4f620ad74b, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:30:24Z Pro: model size in memory before the refresh: None MB
2026-11-20T14:30:25Z Pro: standard refresh started
2026-11-20T14:31:25Z Pro: refresh refreshed (Completed) 
2026-11-20T14:31:25Z Pro: model size in memory right after the refresh: None MB
```
