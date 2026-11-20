# Harness run 20261120T115334Z-v99j-f55a

- Task: refresh
- Variant: v99j-buffer-stg-customer
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: dd53ffcc-dd2d-4d73-88ec-e949ca225a0d
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 671 MB, Power Query 638 MB, duration 0 min, CPU 8 s, rows 83,957, model n/a (no size)
- Refresh request 811ab2b9-ae67-409e-b5ac-55af734fea15, 2026-11-20T11:54:33.903 to 2026-11-20T11:54:39.143, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99j-buffer-stg-customer on PPU data-1m-v1: refreshed, peak 23,111 MB (2026-11-20T05:35:34Z).
  - Peak change: -22,440 MB (-97.1%). **FLAG: peak changed by more than 1%**
  - **FLAG: result changed from refreshed to failed**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 671 MB vs 666 MB (+5 MB), Power Query 638 MB vs 591 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 543 MB. The refresh may use the SKU maximum minus this: 101,857 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,523 MB: fits (27%); F16 4,577 MB: fits (15%); F32 9,697 MB: fits (7%); F64 25,057 MB: fits (3%); PPU 101,857 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
```

Slowest steps:

```
                                                                                                       Object OperationDetailName  DurationSec  CpuSec  Rows
                                                             Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          0.9     0.0     0
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          0.8     0.1     0
                                                             Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          0.8     0.0     0
                                     Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          0.7     0.0     0
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          0.6     0.0     0
                                                               Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          0.2     0.0     0
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18            ReadData          0.1     0.0  2517
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18             Process          0.1     0.0     0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f            ReadData          0.0     0.0     1
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f     CompressSegment          0.0     0.0     0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f   AnalyzeEncodeData          0.0     0.0     0
                                                                                                         <NA>            Rollback          0.0     0.0  <NA>
```

**Screenshot: the refresh error of v99j-buffer-stg-customer on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99j-buffer-stg-customer-refresh-error.png**

## Log

```
2026-11-20T11:54:01Z run 20261120T115334Z-v99j-f55a: variant=v99j-buffer-stg-customer data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T11:54:07Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:54:15Z PPU: v99j-buffer-stg-customer is 69bc2532-0803-4ff1-841a-d6893208f449, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:54:30Z PPU: model size in memory before the refresh: 542.7 MB
2026-11-20T11:54:33Z PPU: trace started (full)
2026-11-20T11:54:34Z PPU: refresh started, request 811ab2b9-ae67-409e-b5ac-55af734fea15
2026-11-20T11:54:44Z PPU: refresh failed (Failed) other
2026-11-20T11:55:14Z PPU: trace captured 76 events: ProgressReportEnd 53, ExecutionMetrics 10, CommandEnd 8, Error 5
```
