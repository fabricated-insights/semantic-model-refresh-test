# Harness run 20261120T141521Z-v30-ce5e

- Task: refresh
- Variant: v30-double-instead-of-fixed
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6c536aff-b598-42c8-8cf6-5257cf684b79
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request e2db041f-cb15-49df-bd4b-f8c58ca7a8f1, 2026-11-20T14:18:09.547Z to 2026-11-20T14:18:49.773Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v30-double-instead-of-fixed on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T08:25:21Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T14:17:37Z run 20261120T141521Z-v30-ce5e: variant=v30-double-instead-of-fixed data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T14:17:41Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T14:17:52Z Pro: updated v30-double-instead-of-fixed from the F64 workspace (12 files)
2026-11-20T14:17:53Z Pro: v30-double-instead-of-fixed is f5ade11e-0d70-4124-9864-769370fc626d, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:18:09Z Pro: model size in memory before the refresh: None MB
2026-11-20T14:18:09Z Pro: standard refresh started
2026-11-20T14:19:09Z Pro: refresh refreshed (Completed) 
2026-11-20T14:19:09Z Pro: model size in memory right after the refresh: None MB
```
