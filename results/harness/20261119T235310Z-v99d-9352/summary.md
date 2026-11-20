# Harness run 20261119T235310Z-v99d-9352

- Task: refresh
- Variant: v99d-power-query
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 705ea48e-6887-4a0a-b17a-a42c649e6ba0
- Refresh parallelism requested: 6

## F2

- Result: **failed** (resource governance)
- Peak n/a, Power Query n/a, duration 0 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request b502abc5-091d-4539-814a-05fff4a3e8d2, 2026-11-19T23:56:00.133 to 2026-11-19T23:56:21.53, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99d-power-query on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- Engine cancelled at 3,363 MB against a limit of 3,063 MB (database size before the command 8 MB).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3363 MB, memory limit 3063 MB, database size before command execution 8 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3363 MB, memory limit 3063 MB, database size before command execution 8 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

**Screenshot: the refresh error of v99d-power-query on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v99d-power-query-resource-governance.png**

## Log

```
2026-11-19T23:55:31Z run 20261119T235310Z-v99d-9352: variant=v99d-power-query data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T23:55:40Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:55:42Z F2: v99d-power-query is afa2f514-2959-442e-9c1f-571bc4435cb0, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:56:00Z F2: model size in memory before the refresh: 0.3 MB
2026-11-19T23:56:00Z F2: refresh started, request b502abc5-091d-4539-814a-05fff4a3e8d2
2026-11-19T23:56:25Z F2: refresh failed (Failed) resource governance
```
