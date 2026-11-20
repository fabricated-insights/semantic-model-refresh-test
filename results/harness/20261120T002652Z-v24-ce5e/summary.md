# Harness run 20261120T002652Z-v24-ce5e

- Task: refresh
- Variant: v24-bidirectional
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: d8bbb7a9-3eb8-4b74-be03-78e4727fa074
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 64718bdf-22e9-4b92-afe1-474d66c7098c, 2026-11-20T00:29:40.763Z to 2026-11-20T00:30:27.53Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v24-bidirectional on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T05:59:40Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T00:29:07Z run 20261120T002652Z-v24-ce5e: variant=v24-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T00:29:09Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T00:29:26Z Pro: updated v24-bidirectional from the F64 workspace (12 files)
2026-11-20T00:29:27Z Pro: v24-bidirectional is 2ffad2da-054f-4e22-a193-a672b0711d93, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:29:40Z Pro: model size in memory before the refresh: None MB
2026-11-20T00:29:40Z Pro: standard refresh started
2026-11-20T00:30:40Z Pro: refresh refreshed (Completed) 
2026-11-20T00:30:40Z Pro: model size in memory right after the refresh: None MB
```
