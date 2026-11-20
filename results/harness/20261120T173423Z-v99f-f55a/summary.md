# Harness run 20261120T173423Z-v99f-f55a

- Task: refresh
- Variant: v99f-calc-tables
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: b0f916b9-5922-4c3a-bf9d-1aa888f29ef9
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 73 MB, Power Query 51 MB, duration 0 min, CPU 13 s, rows 89,464, model n/a (no size)
- Refresh request 40ef3ac0-c285-442b-921f-eb000da07603, 2026-11-20T17:37:23.867 to 2026-11-20T17:37:40.7, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99f-calc-tables on PPU data-1m-v1: failed, peak 837 MB (2026-11-20T11:36:05Z).
  - Peak change: -764 MB (-91.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 73 MB vs 604 MB (-531 MB), Power Query 51 MB vs 529 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 386 MB. The refresh may use the SKU maximum minus this: 102,014 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,680 MB: fits (3%); F16 4,734 MB: fits (2%); F32 9,854 MB: fits (1%); F64 25,214 MB: fits (0%); PPU 102,014 MB: fits (0%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                                                                  Object OperationDetailName  DurationSec  CpuSec  Rows
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh         11.8     0.2     0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql         11.5     0.0     0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh         11.5     0.1     0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql         11.3     0.0     0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql         11.3     0.0     0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql         11.3     0.0     0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b            ReadData          0.4     0.1  4018
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b             Process          0.4     0.1     0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          0.3     0.0     0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b     CompressSegment          0.0     0.0     0
                                                                    <NA>            Rollback          0.0     0.0  <NA>
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b   AnalyzeEncodeData          0.0     0.0     0
```

**Screenshot: the refresh error of v99f-calc-tables on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99f-calc-tables-refresh-error.png**

## Log

```
2026-11-20T17:36:43Z run 20261120T173423Z-v99f-f55a: variant=v99f-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T17:36:49Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T17:36:56Z PPU: v99f-calc-tables is 78a00a5c-5123-48ef-a449-f334f1e5852f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T17:37:20Z PPU: model size in memory before the refresh: 385.7 MB
2026-11-20T17:37:23Z PPU: trace started (full)
2026-11-20T17:37:24Z PPU: refresh started, request 40ef3ac0-c285-442b-921f-eb000da07603
2026-11-20T17:37:49Z PPU: refresh failed (Failed) other
2026-11-20T17:38:19Z PPU: trace captured 80 events: ProgressReportEnd 57, ExecutionMetrics 10, CommandEnd 8, Error 5
```
