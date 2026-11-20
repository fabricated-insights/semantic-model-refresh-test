# Harness run 20261120T173139Z-v99e-f55a

- Task: refresh
- Variant: v99e-sales-flat
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 698cd5f2-8e92-42da-9e8b-b0fc2c74991a
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 1,086 MB, Power Query 1,055 MB, duration 0 min, CPU 16 s, rows 173,886, model n/a (no size)
- Refresh request 99a058ee-077e-4cb6-8d11-342000ac5ecd, 2026-11-20T17:33:03.62 to 2026-11-20T17:33:16.14, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99e-sales-flat on PPU data-1m-v1: failed, peak 284 MB (2026-11-20T11:32:11Z).
  - Peak change: +802 MB (+282.4%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 1,086 MB vs 604 MB (+482 MB), Power Query 1,055 MB vs 529 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 357 MB. The refresh may use the SKU maximum minus this: 102,043 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,709 MB: fits (40%); F16 4,763 MB: fits (23%); F32 9,883 MB: fits (11%); F64 25,243 MB: fits (4%); PPU 102,043 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          5.5     0.2      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          5.3     1.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          4.1     0.2      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          4.0     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          3.3     0.1      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          3.3     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          3.3     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          3.2     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          1.9     0.9      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          1.8     0.9 100450
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18             Process          1.4     0.1      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18            ReadData          1.3     0.1   2517
```

**Screenshot: the refresh error of v99e-sales-flat on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99e-sales-flat-refresh-error.png**

## Log

```
2026-11-20T17:32:26Z run 20261120T173139Z-v99e-f55a: variant=v99e-sales-flat data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T17:32:36Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T17:32:43Z PPU: v99e-sales-flat is a580ec47-fa81-43a8-98d8-f79d00b354d1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T17:32:59Z PPU: model size in memory before the refresh: 356.6 MB
2026-11-20T17:33:03Z PPU: trace started (full)
2026-11-20T17:33:03Z PPU: refresh started, request 99a058ee-077e-4cb6-8d11-342000ac5ecd
2026-11-20T17:33:28Z PPU: refresh failed (Failed) other
2026-11-20T17:33:59Z PPU: trace captured 234 events: ProgressReportEnd 211, ExecutionMetrics 10, CommandEnd 8, Error 5
```
