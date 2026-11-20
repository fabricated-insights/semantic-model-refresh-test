# Harness run 20261120T113625Z-v99g-f55a

- Task: refresh
- Variant: v99g-sales-copy
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 7dab3297-cb3a-45d8-b5bc-4c1c16f72754
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 718 MB, Power Query 674 MB, duration 0 min, CPU 14 s, rows 115,275, model n/a (no size)
- Refresh request 891c864f-3259-4f6d-a230-973a4717d820, 2026-11-20T11:39:24.753 to 2026-11-20T11:39:35.23, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99g-sales-copy on PPU data-1m-v1: refreshed, peak 22,945 MB (2026-11-20T03:50:52Z).
  - Peak change: -22,227 MB (-96.9%). **FLAG: peak changed by more than 1%**
  - **FLAG: result changed from refreshed to failed**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 718 MB vs 666 MB (+52 MB), Power Query 674 MB vs 591 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 543 MB. The refresh may use the SKU maximum minus this: 101,857 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,523 MB: fits (28%); F16 4,577 MB: fits (16%); F32 9,697 MB: fits (7%); F64 25,057 MB: fits (3%); PPU 101,857 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                                                                                                       Object OperationDetailName  DurationSec  CpuSec   Rows
                                                                                                         <NA>            Rollback          2.9     0.0   <NA>
                                                       Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          2.2     0.0      0
                                                             Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          2.1     0.1      0
                                                             Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          2.0     0.0      0
                                     Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.9     0.7      0
                                     Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          1.0     0.6      0
                                     Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          1.0     0.5 100450
                                     Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          0.7     0.0      0
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          0.5     0.0      0
                                                               Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          0.3     0.0      0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f      TabularRefresh          0.1     0.0      0
                                     Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be   AnalyzeEncodeData          0.0     0.0      0
```

**Screenshot: the refresh error of v99g-sales-copy on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99g-sales-copy-refresh-error.png**

## Log

```
2026-11-20T11:38:42Z run 20261120T113625Z-v99g-f55a: variant=v99g-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T11:38:49Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:38:58Z PPU: v99g-sales-copy is 0fc043ea-05ca-437e-b339-49dc7a786423, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:39:21Z PPU: model size in memory before the refresh: 542.7 MB
2026-11-20T11:39:24Z PPU: trace started (full)
2026-11-20T11:39:24Z PPU: refresh started, request 891c864f-3259-4f6d-a230-973a4717d820
2026-11-20T11:39:50Z PPU: refresh failed (Failed) other
2026-11-20T11:40:20Z PPU: trace captured 67 events: ProgressReportEnd 44, ExecutionMetrics 10, CommandEnd 8, Error 5
```
