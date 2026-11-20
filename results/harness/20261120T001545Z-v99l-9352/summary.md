# Harness run 20261120T001545Z-v99l-9352

- Task: refresh
- Variant: v99l-no-calc-columns
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f85cbe25-14e7-4380-8ec8-92b87dfc3378
- Refresh parallelism requested: 6

## F2

- Result: **failed** (resource governance)
- Peak n/a, Power Query n/a, duration 0 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request c8270729-5f20-481e-b41c-ccae73ff56be, 2026-11-20T00:18:18.62 to 2026-11-20T00:18:36.563, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99l-no-calc-columns on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- Engine cancelled at 3,063 MB against a limit of 3,063 MB (database size before the command 8 MB).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3063 MB, memory limit 3063 MB, database size before command execution 8 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3063 MB, memory limit 3063 MB, database size before command execution 8 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

**Screenshot: the refresh error of v99l-no-calc-columns on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v99l-no-calc-columns-resource-governance.png**

## Log

```
2026-11-20T00:17:49Z run 20261120T001545Z-v99l-9352: variant=v99l-no-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-20T00:17:56Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T00:17:59Z F2: v99l-no-calc-columns is 3c1a3f1f-dc2f-4d85-aabb-533c2857603f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:18:18Z F2: model size in memory before the refresh: 0.3 MB
2026-11-20T00:18:18Z F2: refresh started, request c8270729-5f20-481e-b41c-ccae73ff56be
2026-11-20T00:18:44Z F2: refresh failed (Failed) resource governance
```
