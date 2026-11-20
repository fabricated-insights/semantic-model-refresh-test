# Harness run 20261120T113229Z-v99f-f55a

- Task: refresh
- Variant: v99f-calc-tables
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6069b0b8-925d-4881-a75e-ae373f8ed33d
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 837 MB, Power Query 797 MB, duration 0 min, CPU 10 s, rows 98,623, model n/a (no size)
- Refresh request 97121fe3-b40c-443b-adff-c307fcf4526b, 2026-11-20T11:35:25.17 to 2026-11-20T11:35:31.783, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99f-calc-tables on PPU data-1m-v1: refreshed, peak 22,841 MB (2026-11-20T03:26:03Z).
  - Peak change: -22,004 MB (-96.3%). **FLAG: peak changed by more than 1%**
  - **FLAG: result changed from refreshed to failed**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 837 MB vs 666 MB (+171 MB), Power Query 797 MB vs 591 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 386 MB. The refresh may use the SKU maximum minus this: 102,014 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,680 MB: fits (31%); F16 4,734 MB: fits (18%); F32 9,854 MB: fits (8%); F64 25,214 MB: fits (3%); PPU 102,014 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
```

Slowest steps:

```
                                                                                                       Object OperationDetailName  DurationSec  CpuSec  Rows
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.0     0.1     0
                                                       Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          0.9     0.0     0
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          0.8     0.0     0
                                     Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          0.8     0.0     0
                                                               Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          0.3     0.0     0
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18            ReadData          0.1     0.1  2517
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18             Process          0.1     0.1     0
                                                                                                         <NA>            Rollback          0.0     0.0  <NA>
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f   AnalyzeEncodeData          0.0     0.0     0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f      TabularRefresh          0.0     0.0     0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f            ReadData          0.0     0.0     1
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f             Process          0.0     0.0     0
```

**Screenshot: the refresh error of v99f-calc-tables on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99f-calc-tables-refresh-error.png**

## Log

```
2026-11-20T11:34:42Z run 20261120T113229Z-v99f-f55a: variant=v99f-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T11:34:49Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:34:56Z PPU: v99f-calc-tables is 78a00a5c-5123-48ef-a449-f334f1e5852f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:35:21Z PPU: model size in memory before the refresh: 385.7 MB
2026-11-20T11:35:25Z PPU: trace started (full)
2026-11-20T11:35:25Z PPU: refresh started, request 97121fe3-b40c-443b-adff-c307fcf4526b
2026-11-20T11:35:35Z PPU: refresh failed (Failed) other
2026-11-20T11:36:05Z PPU: trace captured 61 events: ProgressReportEnd 38, ExecutionMetrics 10, CommandEnd 8, Error 5
```
