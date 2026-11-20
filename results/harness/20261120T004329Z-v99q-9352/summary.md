# Harness run 20261120T004329Z-v99q-9352

- Task: refresh
- Variant: v99q-customer-stats
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 338c04a0-18fa-4978-a640-6aa318b1a11f
- Refresh parallelism requested: 6

## F2

- Result: **failed** (resource governance)
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request c1cb8f15-47bf-4cd1-9ea4-66753a3c47d2, 2026-11-20T00:44:26.833 to 2026-11-20T00:45:23.033, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99q-customer-stats on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- Engine cancelled at 3,181 MB against a limit of 3,063 MB (database size before the command 8 MB).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3181 MB, memory limit 3063 MB, database size before command execution 8 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3181 MB, memory limit 3063 MB, database size before command execution 8 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3181 MB, memory limit 3063 MB, database size before command execution 8 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3181 MB, memory limit 3063 MB, database size before command execution 8 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

**Screenshot: the refresh error of v99q-customer-stats on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v99q-customer-stats-resource-governance.png**

## Log

```
2026-11-20T00:44:02Z run 20261120T004329Z-v99q-9352: variant=v99q-customer-stats data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-20T00:44:11Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T00:44:13Z F2: v99q-customer-stats is 82cb0596-b1d7-4c0f-8e9e-b153a32d75ae, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:44:26Z F2: model size in memory before the refresh: 0.3 MB
2026-11-20T00:44:27Z F2: refresh started, request c1cb8f15-47bf-4cd1-9ea4-66753a3c47d2
2026-11-20T00:45:37Z F2: refresh failed (Failed) resource governance
```
