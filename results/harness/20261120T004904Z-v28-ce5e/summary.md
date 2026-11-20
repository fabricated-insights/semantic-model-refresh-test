# Harness run 20261120T004904Z-v28-ce5e

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f24ae210-0194-4340-ab5a-cdc81b6dcc2e
- Refresh parallelism requested: 6

## Pro

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 0f96c808-dcef-44a4-871c-afd27fd09532, 2026-11-20T00:51:45.49Z to 2026-11-20T00:52:28.68Z, workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v28-types-all-text on Pro data-1m-v1: refreshed, peak n/a (2026-11-17T06:40:04Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-20T00:51:08Z run 20261120T004904Z-v28-ce5e: variant=v28-types-all-text data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-20T00:51:11Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-20T00:51:30Z Pro: updated v28-types-all-text from the F64 workspace (12 files)
2026-11-20T00:51:31Z Pro: v28-types-all-text is 6391583e-bd04-41bb-9d15-92bd6c0a4db7, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:51:44Z Pro: model size in memory before the refresh: None MB
2026-11-20T00:51:45Z Pro: standard refresh started
2026-11-20T00:52:45Z Pro: refresh refreshed (Completed) 
2026-11-20T00:52:45Z Pro: model size in memory right after the refresh: None MB
```
