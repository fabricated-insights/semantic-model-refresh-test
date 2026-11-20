# Harness run 20261120T001200Z-v99k-9352

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3e77a318-1dda-4689-8479-2169e438d2f7
- Refresh parallelism requested: 6

## F2

- Result: **failed** (resource governance)
- Peak n/a, Power Query n/a, duration 0 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request db876b0b-2d14-44da-a89a-dd5a98eede70, 2026-11-20T00:14:55.643 to 2026-11-20T00:15:18, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99k-no-buffers on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- Engine cancelled at 3,080 MB against a limit of 3,063 MB (database size before the command 8 MB).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3080 MB, memory limit 3063 MB, database size before command execution 8 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3080 MB, memory limit 3063 MB, database size before command execution 8 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

**Screenshot: the refresh error of v99k-no-buffers on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v99k-no-buffers-resource-governance.png**

## Log

```
2026-11-20T00:14:25Z run 20261120T001200Z-v99k-9352: variant=v99k-no-buffers data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-20T00:14:31Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T00:14:34Z F2: v99k-no-buffers is 45c193ee-19a0-48d8-a030-9548eb98832a, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:14:55Z F2: model size in memory before the refresh: 0.3 MB
2026-11-20T00:14:55Z F2: refresh started, request db876b0b-2d14-44da-a89a-dd5a98eede70
2026-11-20T00:15:21Z F2: refresh failed (Failed) resource governance
```
