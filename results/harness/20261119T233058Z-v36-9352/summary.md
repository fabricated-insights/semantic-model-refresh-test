# Harness run 20261119T233058Z-v36-9352

- Task: refresh
- Variant: v36-calc-summary-month-grain
- Data tag: data-10m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3036fc37-c547-46c3-9f2f-15af1f9841c4
- Refresh parallelism requested: 6

## F2

- Result: **failed** (resource governance)
- Peak n/a, Power Query n/a, duration 10 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 6e913c40-ce2e-42b0-a7c6-722f9390833e, 2026-11-19T23:33:34.59 to 2026-11-19T23:44:00.65, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: refresh API
- Previous harness run of v36-calc-summary-month-grain on F2 data-10m-v1: failed, peak n/a (2026-11-18T14:55:17Z).
- No v00-baseline harness run with a measured peak on F2 data-10m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- Engine cancelled at 3,069 MB against a limit of 3,066 MB (database size before the command 5 MB).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3069 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3069 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3069 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3068 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3069 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3068 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3068 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3107 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3151 MB, memory limit 3066 MB, database size before command execution 5 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The current operation was cancelled because another operation in the transaction failed.
```

**Screenshot: the refresh error of v36-calc-summary-month-grain on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v36-calc-summary-month-grain-resource-governance.png**

## Log

```
2026-11-19T23:33:02Z run 20261119T233058Z-v36-9352: variant=v36-calc-summary-month-grain data_tag=data-10m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T23:33:12Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:33:14Z F2: v36-calc-summary-month-grain is a4311446-46ea-4497-80a1-7a0e4a156699, DataTag reads back data-10m-v1, SourceType parquet
2026-11-19T23:33:34Z F2: model size in memory before the refresh: 0.1 MB
2026-11-19T23:33:34Z F2: refresh started, request 6e913c40-ce2e-42b0-a7c6-722f9390833e
2026-11-19T23:44:16Z F2: refresh failed (Failed) resource governance
```
