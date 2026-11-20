# Harness run 20261120T112747Z-v99e-f55a

- Task: refresh
- Variant: v99e-sales-flat
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: d73eeb41-5b98-4207-8f91-b60cb72eeb37
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 284 MB, Power Query 250 MB, duration 0 min, CPU 11 s, rows 175,502, model n/a (no size)
- Refresh request 7c594f7d-4fa7-44af-93a7-65c1d8766bf6, 2026-11-20T11:31:30.123 to 2026-11-20T11:31:35.423, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99e-sales-flat on PPU data-1m-v1: refreshed, peak 23,036 MB (2026-11-20T02:58:07Z).
  - Peak change: -22,752 MB (-98.8%). **FLAG: peak changed by more than 1%**
  - **FLAG: result changed from refreshed to failed**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 284 MB vs 666 MB (-382 MB), Power Query 250 MB vs 591 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 357 MB. The refresh may use the SKU maximum minus this: 102,043 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,709 MB: fits (10%); F16 4,763 MB: fits (6%); F32 9,883 MB: fits (3%); F64 25,243 MB: fits (1%); PPU 102,043 MB: fits (0%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          2.2     0.6      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          2.1     0.1      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          2.0     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          2.0     0.0      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.5     0.1      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          1.3     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          1.2     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          0.9     0.6      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          0.8     0.5 100450
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          0.6     0.1      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b             Process          0.3     0.1      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b            ReadData          0.3     0.1   4018
```

**Screenshot: the refresh error of v99e-sales-flat on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99e-sales-flat-refresh-error.png**

## Log

```
2026-11-20T11:30:39Z run 20261120T112747Z-v99e-f55a: variant=v99e-sales-flat data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T11:30:50Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:31:00Z PPU: v99e-sales-flat is a580ec47-fa81-43a8-98d8-f79d00b354d1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:31:26Z PPU: model size in memory before the refresh: 356.6 MB
2026-11-20T11:31:29Z PPU: trace started (full)
2026-11-20T11:31:30Z PPU: refresh started, request 7c594f7d-4fa7-44af-93a7-65c1d8766bf6
2026-11-20T11:31:40Z PPU: refresh failed (Failed) other
2026-11-20T11:32:10Z PPU: trace captured 234 events: ProgressReportEnd 211, ExecutionMetrics 10, CommandEnd 8, Error 5
```
