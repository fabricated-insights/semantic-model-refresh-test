# Harness run 20261119T235652Z-v99e-9352

- Task: refresh
- Variant: v99e-sales-flat
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: c27fc212-f9ae-4183-97e2-72d7cd80b368
- Refresh parallelism requested: 6

## F2

- Result: **failed** (resource governance)
- Peak n/a, Power Query n/a, duration 0 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 1e24b67e-d7ea-49ac-afe8-5b0d72aab179, 2026-11-19T23:57:49.17 to 2026-11-19T23:58:04.863, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99e-sales-flat on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- Engine cancelled at 3,306 MB against a limit of 3,062 MB (database size before the command 9 MB).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3306 MB, memory limit 3062 MB, database size before command execution 9 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3306 MB, memory limit 3062 MB, database size before command execution 9 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3306 MB, memory limit 3062 MB, database size before command execution 9 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

**Screenshot: the refresh error of v99e-sales-flat on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v99e-sales-flat-resource-governance.png**

## Log

```
2026-11-19T23:57:26Z run 20261119T235652Z-v99e-9352: variant=v99e-sales-flat data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T23:57:33Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:57:35Z F2: v99e-sales-flat is 749dc699-2156-4f81-8344-7e88855a6b14, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:57:49Z F2: model size in memory before the refresh: 0.4 MB
2026-11-19T23:57:49Z F2: refresh started, request 1e24b67e-d7ea-49ac-afe8-5b0d72aab179
2026-11-19T23:58:14Z F2: refresh failed (Failed) resource governance
```
