# Harness run 20261120T003724Z-v99o-9352

- Task: refresh
- Variant: v99o-sorts
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e670a755-1a5b-4e25-9f85-8abe88c0cb60
- Refresh parallelism requested: 6

## F2

- Result: **failed** (resource governance)
- Peak n/a, Power Query n/a, duration 1 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request c8029f6a-d263-4d93-bdbf-6d77124aa574, 2026-11-20T00:38:27.117 to 2026-11-20T00:39:20, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- No earlier harness run of v99o-sorts on F2 data-1m-v1.
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 3,066 MB on F2.
- Engine cancelled at 3,265 MB against a limit of 3,064 MB (database size before the command 7 MB).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 3265 MB, memory limit 3064 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

**Screenshot: the refresh error of v99o-sorts on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v99o-sorts-resource-governance.png**

## Log

```
2026-11-20T00:38:01Z run 20261120T003724Z-v99o-9352: variant=v99o-sorts data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-20T00:38:11Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T00:38:14Z F2: v99o-sorts is 402bd6c5-91ff-4d55-bcb0-de57409ac4af, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:38:27Z F2: model size in memory before the refresh: 0.3 MB
2026-11-20T00:38:27Z F2: refresh started, request c8029f6a-d263-4d93-bdbf-6d77124aa574
2026-11-20T00:39:37Z F2: refresh failed (Failed) resource governance
```
