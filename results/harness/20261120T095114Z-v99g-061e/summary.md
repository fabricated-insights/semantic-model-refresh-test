# Harness run 20261120T095114Z-v99g-061e

- Task: refresh
- Variant: v99g-sales-copy
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 91982397-170f-4a31-81ce-ba5be58303b0
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 398 MB, Power Query 321 MB, duration 0 min, CPU 16 s, rows 1,133,525, model n/a (no size)
- Refresh request a76394f4-9f4c-411d-9845-63ffff027c1b, 2026-11-20T09:54:36.207 to 2026-11-20T09:54:41.403, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99g-sales-copy on F64 data-1m-v1: refreshed, peak 22,952 MB (2026-11-20T03:28:57Z).
  - Peak change: -22,554 MB (-98.3%). **FLAG: peak changed by more than 1%**
  - **FLAG: result changed from refreshed to failed**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 398 MB vs 716 MB (-318 MB), Power Query 321 MB vs 527 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 663 MB. The refresh may use the SKU maximum minus this: 24,937 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,403 MB: fits (17%); F16 4,457 MB: fits (9%); F32 9,577 MB: fits (4%); F64 24,937 MB: fits (2%); PPU 101,737 MB: fits (0%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
```

**Screenshot: the refresh error of v99g-sales-copy on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99g-sales-copy-refresh-error.png**

## Log

```
2026-11-20T09:53:58Z run 20261120T095114Z-v99g-061e: variant=v99g-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T09:54:07Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T09:54:09Z F64: v99g-sales-copy is 7019bbb5-e7cd-4985-bc14-7af18c43cc4e, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:54:36Z F64: model size in memory before the refresh: 662.8 MB
2026-11-20T09:54:36Z F64: refresh started, request a76394f4-9f4c-411d-9845-63ffff027c1b
2026-11-20T09:54:46Z F64: refresh failed (Failed) other
2026-11-20T09:54:46Z F64: monitoring database Monitoring KQL database
2026-11-20T09:55:36Z F64: ExecutionMetrics event found
```
