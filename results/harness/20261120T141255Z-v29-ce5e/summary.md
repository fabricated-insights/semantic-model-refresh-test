# Harness run 20261120T141255Z-v29-ce5e

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 0a7f9a3b-61c7-413b-a570-f7f12f19ce7f
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request d650b692-52d0-4c74-b6d0-21ab683123a2, 2026-11-20T14:14:05.46Z to 2026-11-20T14:14:52.633Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v29-keys-as-text on Pro data-1m-v1: refreshed, peak n/a (2026-11-20T08:21:03Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T14:13:39Z run 20261120T141255Z-v29-ce5e: variant=v29-keys-as-text data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T14:13:43Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T14:13:54Z Pro: updated v29-keys-as-text from the F64 workspace (12 files)
2026-11-20T14:13:55Z Pro: v29-keys-as-text is ac88cedc-9084-411b-8388-2fd68c96a7ee, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:14:05Z Pro: model size in memory before the refresh: None MB
2026-11-20T14:14:05Z Pro: standard refresh started
2026-11-20T14:15:05Z Pro: refresh refreshed (Completed) 
2026-11-20T14:15:05Z Pro: model size in memory right after the refresh: None MB
```
