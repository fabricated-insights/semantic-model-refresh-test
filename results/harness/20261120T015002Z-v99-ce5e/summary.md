# Harness run 20261120T015002Z-v99-ce5e

- Task: refresh
- Variant: v99-kitchen-sink
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: fc785f92-1351-4ef4-9adc-7db18d809c75
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 16 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 9185f2ae-30a8-4eda-8cf5-f1b5ac7b70d5, 2026-11-20T01:51:46.113Z to 2026-11-20T02:07:51.083Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99-kitchen-sink on Pro data-1m-v1: refreshed, peak n/a (2026-11-18T00:32:16Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T01:51:01Z run 20261120T015002Z-v99-ce5e: variant=v99-kitchen-sink data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T01:51:04Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T01:51:37Z Pro: updated v99-kitchen-sink from the F64 workspace (18 files)
2026-11-20T01:51:38Z Pro: v99-kitchen-sink is 4af1fdd1-397f-427c-be5d-3ea9bc11943d, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T01:51:45Z Pro: model size in memory before the refresh: None MB
2026-11-20T01:51:46Z Pro: standard refresh started
2026-11-20T02:08:18Z Pro: refresh refreshed (Completed) 
2026-11-20T02:08:18Z Pro: model size in memory right after the refresh: None MB
```
