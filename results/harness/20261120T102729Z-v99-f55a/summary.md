# Harness run 20261120T102729Z-v99-f55a

- Task: refresh
- Variant: v99-kitchen-sink
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 13223ca9-0cdf-4628-81f8-87d87505d5a4
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 14,722 MB, Power Query 14,643 MB, duration 1 min, CPU 231 s, rows 10,329,373, model n/a (no size)
- Refresh request 6689b874-74e1-4af2-982d-e5c20003d898, 2026-11-20T10:30:31.82 to 2026-11-20T10:31:38.253, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99-kitchen-sink on PPU data-1m-v1: refreshed, peak 26,212 MB (2026-11-20T01:12:35Z).
  - Peak change: -11,490 MB (-43.8%). **FLAG: peak changed by more than 1%**
  - **FLAG: result changed from refreshed to failed**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 14,722 MB vs 666 MB (+14,056 MB), Power Query 14,643 MB vs 591 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 626 MB. The refresh may use the SKU maximum minus this: 101,774 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,440 MB: OVER (603%); F16 4,494 MB: OVER (328%); F32 9,614 MB: OVER (153%); F64 24,974 MB: fits (59%); PPU 101,774 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec     Rows
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         17.5     2.1        0
                                     Product Date Grid.Product Date Grid            VertiPaq         11.3    11.2        0
                                     Product Date Grid.Product Date Grid             Process          9.7     9.1        0
                                     Product Date Grid.Product Date Grid      TabularRefresh          9.7     9.1        0
                                     Product Date Grid.Product Date Grid            ReadData          9.1     9.0 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          8.9     2.0        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          8.7     1.9   104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          8.5     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          3.0     0.8        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          1.8     0.0        0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.8     0.1        0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          1.4     0.0        0
```

**Screenshot: the refresh error of v99-kitchen-sink on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99-kitchen-sink-refresh-error.png**

## Log

```
2026-11-20T10:29:45Z run 20261120T102729Z-v99-f55a: variant=v99-kitchen-sink data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T10:29:54Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T10:30:03Z PPU: v99-kitchen-sink is 67527e72-ce42-4278-b95a-711034a934b6, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T10:30:28Z PPU: model size in memory before the refresh: 626.4 MB
2026-11-20T10:30:31Z PPU: trace started (full)
2026-11-20T10:30:31Z PPU: refresh started, request 6689b874-74e1-4af2-982d-e5c20003d898
2026-11-20T10:31:42Z PPU: refresh failed (Failed) other
2026-11-20T10:32:12Z PPU: trace captured 253 events: ProgressReportEnd 218, ExecutionMetrics 22, CommandEnd 8, Error 5
```
