# Harness run 20261119T234622Z-v99a-9352

- Task: refresh
- Variant: v99a-no-big-calc-tables
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 7c4c4b3a-7a0c-43f8-83f9-357f4da3329f
- Refresh parallelism requested: 6

## F2

- Result: **failed** (resource governance)
- Peak n/a, Power Query n/a, duration 0 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request a9e3b158-3e7a-4588-af1a-1fd171bf04c8, 2026-11-19T23:48:56.277 to 2026-11-19T23:49:19.727, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99a-no-big-calc-tables on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- Engine cancelled at 3,461 MB against a limit of 3,063 MB (database size before the command 8 MB).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3461 MB, memory limit 3063 MB, database size before command execution 8 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3461 MB, memory limit 3063 MB, database size before command execution 8 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

**Screenshot: the refresh error of v99a-no-big-calc-tables on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v99a-no-big-calc-tables-resource-governance.png**

## Log

```
2026-11-19T23:48:26Z run 20261119T234622Z-v99a-9352: variant=v99a-no-big-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T23:48:33Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:48:36Z F2: v99a-no-big-calc-tables is aab4eaf3-544f-4e74-8a3a-14378dfda5f0, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:48:56Z F2: model size in memory before the refresh: 0.3 MB
2026-11-19T23:48:56Z F2: refresh started, request a9e3b158-3e7a-4588-af1a-1fd171bf04c8
2026-11-19T23:49:21Z F2: refresh failed (Failed) resource governance
```
