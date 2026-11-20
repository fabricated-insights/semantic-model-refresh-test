# Harness run 20261120T173837Z-v99g-f55a

- Task: refresh
- Variant: v99g-sales-copy
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 68d784ce-2206-455e-9e79-bbcaac947113
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 663 MB, Power Query 640 MB, duration 0 min, CPU 13 s, rows 361,971, model n/a (no size)
- Refresh request b454a389-4489-4085-b9f3-523587c7dae6, 2026-11-20T17:39:46.857 to 2026-11-20T17:39:52.373, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99g-sales-copy on PPU data-1m-v1: failed, peak 718 MB (2026-11-20T11:40:20Z).
  - Peak change: -55 MB (-7.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 663 MB vs 604 MB (+59 MB), Power Query 640 MB vs 529 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 543 MB. The refresh may use the SKU maximum minus this: 101,857 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,523 MB: fits (26%); F16 4,577 MB: fits (14%); F32 9,697 MB: fits (7%); F64 25,057 MB: fits (3%); PPU 101,857 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          2.1     0.7      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.2     0.2      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          1.1     0.6      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          1.0     0.6 100450
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          1.0     0.1      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          0.9     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          0.9     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          0.8     0.0      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          0.5     0.1      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          0.4     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b            ReadData          0.3     0.0   4018
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b             Process          0.3     0.1      0
```

**Screenshot: the refresh error of v99g-sales-copy on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99g-sales-copy-refresh-error.png**

## Log

```
2026-11-20T17:39:11Z run 20261120T173837Z-v99g-f55a: variant=v99g-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T17:39:18Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T17:39:27Z PPU: v99g-sales-copy is 0fc043ea-05ca-437e-b339-49dc7a786423, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T17:39:43Z PPU: model size in memory before the refresh: 542.7 MB
2026-11-20T17:39:46Z PPU: trace started (full)
2026-11-20T17:39:46Z PPU: refresh started, request b454a389-4489-4085-b9f3-523587c7dae6
2026-11-20T17:39:57Z PPU: refresh failed (Failed) other
2026-11-20T17:40:27Z PPU: trace captured 229 events: ProgressReportEnd 206, ExecutionMetrics 10, CommandEnd 8, Error 5
```
