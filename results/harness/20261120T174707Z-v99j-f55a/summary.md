# Harness run 20261120T174707Z-v99j-f55a

- Task: refresh
- Variant: v99j-buffer-stg-customer
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 234c530c-3c11-4492-b6da-1708d65b4075
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 193 MB, Power Query 159 MB, duration 0 min, CPU 13 s, rows 92,384, model n/a (no size)
- Refresh request 54452819-520f-44f2-9afe-401f2fb0b677, 2026-11-20T17:48:19.41 to 2026-11-20T17:48:26.51, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99j-buffer-stg-customer on PPU data-1m-v1: failed, peak 671 MB (2026-11-20T11:55:14Z).
  - Peak change: -478 MB (-71.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 193 MB vs 604 MB (-411 MB), Power Query 159 MB vs 529 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 543 MB. The refresh may use the SKU maximum minus this: 101,857 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,523 MB: fits (8%); F16 4,577 MB: fits (4%); F32 9,697 MB: fits (2%); F64 25,057 MB: fits (1%); PPU 101,857 MB: fits (0%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                                                                                                       Object OperationDetailName  DurationSec  CpuSec  Rows
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          2.5     0.1     0
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          2.2     0.0     0
                                                             Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          2.2     0.0     0
                                                             Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          2.2     0.0     0
                                     Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          2.1     0.0     0
                                                               Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          0.2     0.0     0
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18            ReadData          0.2     0.0  2517
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18             Process          0.2     0.0     0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f            ReadData          0.0     0.0     1
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f     CompressSegment          0.0     0.0     0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f   AnalyzeEncodeData          0.0     0.0     0
                                                                                                         <NA>            Rollback          0.0     0.0  <NA>
```

**Screenshot: the refresh error of v99j-buffer-stg-customer on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99j-buffer-stg-customer-refresh-error.png**

## Log

```
2026-11-20T17:47:44Z run 20261120T174707Z-v99j-f55a: variant=v99j-buffer-stg-customer data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T17:47:50Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T17:47:59Z PPU: v99j-buffer-stg-customer is 69bc2532-0803-4ff1-841a-d6893208f449, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T17:48:15Z PPU: model size in memory before the refresh: 542.7 MB
2026-11-20T17:48:19Z PPU: trace started (full)
2026-11-20T17:48:19Z PPU: refresh started, request 54452819-520f-44f2-9afe-401f2fb0b677
2026-11-20T17:48:29Z PPU: refresh failed (Failed) other
2026-11-20T17:49:00Z PPU: trace captured 76 events: ProgressReportEnd 53, ExecutionMetrics 10, CommandEnd 8, Error 5
```
