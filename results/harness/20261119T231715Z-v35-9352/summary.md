# Harness run 20261119T231715Z-v35-9352

- Task: refresh
- Variant: v35-calc-tables-four-copies
- Data tag: data-10m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: bbc4ca93-ba61-4f7c-a1ee-944bb67d8ea0
- Refresh parallelism requested: 6

## F2

- Result: **failed** (resource governance)
- Peak n/a, Power Query n/a, duration 9 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 83cb1c47-5cbd-4b79-bce7-9a9db8919987, 2026-11-19T23:20:24.843 to 2026-11-19T23:29:45.687, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: refresh API
- Previous harness run of v35-calc-tables-four-copies on F2 data-10m-v1: failed, peak n/a (2026-11-18T14:39:30Z).
- No v00-baseline harness run with a measured peak on F2 data-10m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- Engine cancelled at 3,071 MB against a limit of 3,066 MB (database size before the command 5 MB).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3071 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3071 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3071 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3069 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3072 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3112 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3066 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The current operation was cancelled because another operation in the transaction failed.
```

**Screenshot: the refresh error of v35-calc-tables-four-copies on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v35-calc-tables-four-copies-resource-governance.png**

## Log

```
2026-11-19T23:19:53Z run 20261119T231715Z-v35-9352: variant=v35-calc-tables-four-copies data_tag=data-10m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T23:19:58Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:20:03Z F2: v35-calc-tables-four-copies is 086f3aaf-fc4b-43bf-885c-2588495308bb, DataTag reads back data-10m-v1, SourceType parquet
2026-11-19T23:20:24Z F2: model size in memory before the refresh: 0.1 MB
2026-11-19T23:20:25Z F2: refresh started, request 83cb1c47-5cbd-4b79-bce7-9a9db8919987
2026-11-19T23:30:06Z F2: refresh failed (Failed) resource governance
```
