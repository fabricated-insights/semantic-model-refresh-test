# Harness run 20261119T215902Z-v20-9352

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 017eecff-b80e-44b6-8ff7-67fa92d77d8f
- Refresh parallelism requested: 6

## F2

- Result: **failed** (resource governance)
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request e796f9d9-52bd-4f45-8b58-1ba003f9889b, 2026-11-19T22:01:37.713 to 2026-11-19T22:02:30.367, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v20-pq-sort on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- Engine cancelled at 3,120 MB against a limit of 3,067 MB (database size before the command 4 MB).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3120 MB, memory limit 3067 MB, database size before command execution 4 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

**Screenshot: the refresh error of v20-pq-sort on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v20-pq-sort-resource-governance.png**

## Log

```
2026-11-19T22:01:07Z run 20261119T215902Z-v20-9352: variant=v20-pq-sort data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T22:01:14Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:01:17Z F2: v20-pq-sort is e70f98a2-f0fa-4535-9cdb-7f162422b8cc, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:01:37Z F2: model size in memory before the refresh: 0.0 MB
2026-11-19T22:01:37Z F2: refresh started, request e796f9d9-52bd-4f45-8b58-1ba003f9889b
2026-11-19T22:02:48Z F2: refresh failed (Failed) resource governance
```
