# Harness run 20261120T161432Z-v99-f55a

- Task: refresh
- Variant: v99-kitchen-sink
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 192add89-6d20-480a-9fff-518ea7abca67
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 14,648 MB, Power Query 14,569 MB, duration 1 min, CPU 273 s, rows 10,329,373, model n/a (no size)
- Refresh request 6b08dfe4-f717-4bc4-9eea-749ef421a233, 2026-11-20T16:15:48.787 to 2026-11-20T16:17:08.583, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99-kitchen-sink on PPU data-1m-v1: failed, peak 14,722 MB (2026-11-20T10:32:13Z).
  - Peak change: -74 MB (-0.5%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 14,648 MB vs 604 MB (+14,044 MB), Power Query 14,569 MB vs 529 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 626 MB. The refresh may use the SKU maximum minus this: 101,774 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,440 MB: OVER (600%); F16 4,494 MB: OVER (326%); F32 9,614 MB: OVER (152%); F64 24,974 MB: fits (59%); PPU 101,774 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         20.7     2.7        0
                                     Product Date Grid.Product Date Grid            VertiPaq         17.1    16.4        0
                                     Product Date Grid.Product Date Grid      TabularRefresh         13.1    11.9        0
                                     Product Date Grid.Product Date Grid             Process         13.0    11.9        0
                                     Product Date Grid.Product Date Grid            ReadData         12.2    11.8 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process         10.9     2.6        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData         10.8     2.5   104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          9.7     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          2.3     1.1        0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.4     0.1        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          1.3     1.1        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          1.2     1.0   100450
```

**Screenshot: the refresh error of v99-kitchen-sink on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99-kitchen-sink-refresh-error.png**

## Log

```
2026-11-20T16:15:08Z run 20261120T161432Z-v99-f55a: variant=v99-kitchen-sink data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T16:15:16Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T16:15:28Z PPU: v99-kitchen-sink is 67527e72-ce42-4278-b95a-711034a934b6, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T16:15:45Z PPU: model size in memory before the refresh: 626.4 MB
2026-11-20T16:15:48Z PPU: trace started (full)
2026-11-20T16:15:48Z PPU: refresh started, request 6b08dfe4-f717-4bc4-9eea-749ef421a233
2026-11-20T16:17:29Z PPU: refresh failed (Failed) other
2026-11-20T16:18:00Z PPU: trace captured 241 events: ProgressReportEnd 218, ExecutionMetrics 10, CommandEnd 8, Error 5
```
