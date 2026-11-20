# Harness run 20261120T135423Z-v24b-ce5e

- Task: refresh
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3816b72b-8623-48fc-ab4b-027f0778fc6c
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 3b04d490-416a-4f0d-915b-fae1bdfed3ae, 2026-11-20T13:57:22.61Z to 2026-11-20T13:58:20.857Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v24b-second-fact-bidirectional on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T07:59:57Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T13:56:51Z run 20261120T135423Z-v24b-ce5e: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T13:56:53Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T13:57:02Z Pro: updated v24b-second-fact-bidirectional from the F64 workspace (13 files)
2026-11-20T13:57:03Z Pro: v24b-second-fact-bidirectional is e87d1e39-81ef-459e-b57b-0271412bfa91, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:57:22Z Pro: model size in memory before the refresh: None MB
2026-11-20T13:57:22Z Pro: standard refresh started
2026-11-20T13:58:22Z Pro: refresh refreshed (Completed) 
2026-11-20T13:58:22Z Pro: model size in memory right after the refresh: None MB
```
