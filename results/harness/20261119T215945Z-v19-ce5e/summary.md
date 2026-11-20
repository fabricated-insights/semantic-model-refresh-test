# Harness run 20261119T215945Z-v19-ce5e

- Task: refresh
- Variant: v19-pq-heavy-10m
- Data tag: data-1m-v1
- Targets: Pro
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: cbc20ad8-0fbc-42ff-8425-bcdd261694f7
- Refresh parallelism requested: 6

## Pro

- Result: **polltimeout** (other)
- Peak n/a, Power Query n/a, duration n/a, CPU n/a, rows n/a, model n/a (no size)
- Refresh request f4b0cf0a-c1e0-4093-a5b2-e3ddf2f73d0b, 2026-11-19T22:00:48.21Z to , workspace at ?, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v19-pq-heavy-10m on Pro data-1m-v1: polltimeout, peak n/a (2026-11-18T08:47:13Z).
- No v00-baseline harness run with a measured peak on Pro data-1m-v1 to compare with.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

**Screenshot: the refresh error of v19-pq-heavy-10m on Pro in the service (semantic model > Refresh history > error details), saved as docs/screenshots/pro-v19-pq-heavy-10m-refresh-error.png**

## Log

```
2026-11-19T22:00:18Z run 20261119T215945Z-v19-ce5e: variant=v19-pq-heavy-10m data_tag=data-1m-v1 source_type=parquet targets=['Pro'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=ce5e3f7a-6c58-40e3-be40-27ebfba25a08
2026-11-19T22:00:21Z Pro: not connected to Git; the model there was deployed by the driver (Pro) or by hand
2026-11-19T22:00:40Z Pro: updated v19-pq-heavy-10m from the F64 workspace (17 files)
2026-11-19T22:00:41Z Pro: v19-pq-heavy-10m is 453cdf86-f54d-4cb6-b14d-ac68bf7cf1ba, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:00:47Z Pro: model size in memory before the refresh: None MB
2026-11-19T22:00:48Z Pro: standard refresh started
2026-11-20T00:01:08Z Pro: refresh polltimeout (PollTimeout) other
```
