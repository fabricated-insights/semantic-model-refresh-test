# Harness run 20261120T052752Z-v99i-ce5e

- Task: refresh
- Variant: v99i-buffer-stg-sales
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: b93836ac-7291-4dbe-868b-e4761b3618ae
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 15 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 136d370d-536c-4129-9a40-52e169948256, 2026-11-20T05:31:03.373Z to 2026-11-20T05:46:22.393Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v99i-buffer-stg-sales on Pro data-1m-v1: refreshed, peak n/a (2026-11-18T10:29:47Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T05:30:10Z run 20261120T052752Z-v99i-ce5e: variant=v99i-buffer-stg-sales data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T05:30:12Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T05:30:47Z Pro: updated v99i-buffer-stg-sales from the F64 workspace (23 files)
2026-11-20T05:30:48Z Pro: v99i-buffer-stg-sales is 8b00d85b-e78a-4019-865c-26c24933f52c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T05:31:03Z Pro: model size in memory before the refresh: None MB
2026-11-20T05:31:03Z Pro: standard refresh started
2026-11-20T05:46:35Z Pro: refresh refreshed (Completed) 
2026-11-20T05:46:35Z Pro: model size in memory right after the refresh: None MB
```
