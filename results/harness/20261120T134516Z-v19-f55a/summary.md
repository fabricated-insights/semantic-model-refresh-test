# Harness run 20261120T134516Z-v19-f55a

- Task: refresh
- Variant: v19-pq-heavy-10m
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a7b0958f-a459-4c5e-b71a-e1c64f7b9451
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 516 MB, Power Query 455 MB, duration 0 min, CPU 28 s, rows 252,345, model n/a (no size)
- Refresh request acdc12e4-33bf-428e-82be-f9daa02e3c51, 2026-11-20T13:48:10.01 to 2026-11-20T13:48:18.163, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v19-pq-heavy-10m on PPU data-1m-v1: failed, peak 23,900 MB (2026-11-20T07:51:16Z).
  - Peak change: -23,384 MB (-97.8%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 516 MB vs 604 MB (-88 MB), Power Query 455 MB vs 529 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (17%); F16 5,120 MB: fits (10%); F32 10,240 MB: fits (5%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.5     1.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.3     0.2      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.3     0.1      0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba          ExecuteSql          1.3     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          1.1     0.9      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          1.1     0.9 100450
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          1.0     0.0      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          1.0     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          1.0     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          0.9     0.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          0.3     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b            ReadData          0.2     0.1   4018
```

**Screenshot: the refresh error of v19-pq-heavy-10m on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v19-pq-heavy-10m-refresh-error.png**

## Log

```
2026-11-20T13:47:35Z run 20261120T134516Z-v19-f55a: variant=v19-pq-heavy-10m data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T13:47:41Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:47:43Z PPU: v19-pq-heavy-10m is 393784af-1418-40f1-a51d-7c01c12a2326, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:48:06Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-20T13:48:09Z PPU: trace started (full)
2026-11-20T13:48:10Z PPU: refresh started, request acdc12e4-33bf-428e-82be-f9daa02e3c51
2026-11-20T13:48:20Z PPU: refresh failed (Failed) other
2026-11-20T13:48:50Z PPU: trace captured 98 events: ProgressReportEnd 75, ExecutionMetrics 10, CommandEnd 8, Error 5
```
