# Harness run 20261120T003344Z-v24b-ce5e

- Task: refresh
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 44245246-8238-4747-8210-166be207fe76
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request e2601d8d-d82a-42f4-a051-fafb95d86d06, 2026-11-20T00:36:56.863Z to 2026-11-20T00:37:46.933Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v24b-second-fact-bidirectional on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T06:14:46Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T00:36:19Z run 20261120T003344Z-v24b-ce5e: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T00:36:21Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T00:36:38Z Pro: updated v24b-second-fact-bidirectional from the F64 workspace (13 files)
2026-11-20T00:36:39Z Pro: v24b-second-fact-bidirectional is e87d1e39-81ef-459e-b57b-0271412bfa91, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:36:56Z Pro: model size in memory before the refresh: None MB
2026-11-20T00:36:56Z Pro: standard refresh started
2026-11-20T00:37:57Z Pro: refresh refreshed (Completed) 
2026-11-20T00:37:57Z Pro: model size in memory right after the refresh: None MB
```
