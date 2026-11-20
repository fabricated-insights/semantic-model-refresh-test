# Harness run 20261120T105615Z-v99c-f55a

- Task: refresh
- Variant: v99c-crossjoin-only
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 0ea85457-0ed5-4a50-a376-435e4b1f7626
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 14,380 MB, Power Query 14,146 MB, duration 1 min, CPU 232 s, rows 10,329,373, model n/a (no size)
- Refresh request dd8e9e48-e97b-4991-9e32-01b99212ad49, 2026-11-20T10:59:59.16 to 2026-11-20T11:01:02.89, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99c-crossjoin-only on PPU data-1m-v1: refreshed, peak 26,157 MB (2026-11-20T02:24:05Z).
  - Peak change: -11,777 MB (-45.0%). **FLAG: peak changed by more than 1%**
  - **FLAG: result changed from refreshed to failed**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 14,380 MB vs 666 MB (+13,714 MB), Power Query 14,146 MB vs 591 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 380 MB. The refresh may use the SKU maximum minus this: 102,020 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,686 MB: OVER (535%); F16 4,740 MB: OVER (303%); F32 9,860 MB: OVER (146%); F64 25,220 MB: fits (57%); PPU 102,020 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         20.0     4.0        0
                                     Product Date Grid.Product Date Grid            VertiPaq         13.7    13.7        0
                                     Product Date Grid.Product Date Grid             Process         11.2    10.3        0
                                     Product Date Grid.Product Date Grid      TabularRefresh         11.2    10.3        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql         10.6     0.0        0
                                     Product Date Grid.Product Date Grid            ReadData         10.3    10.2 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          9.2     3.9        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          9.0     3.8   104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          4.1     1.0        0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          3.2     0.2        0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          2.8     0.0        0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          2.8     0.1        0
```

**Screenshot: the refresh error of v99c-crossjoin-only on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99c-crossjoin-only-refresh-error.png**

## Log

```
2026-11-20T10:59:16Z run 20261120T105615Z-v99c-f55a: variant=v99c-crossjoin-only data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T10:59:22Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T10:59:29Z PPU: v99c-crossjoin-only is 364f4109-e09b-4cda-a773-d642978613b4, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T10:59:55Z PPU: model size in memory before the refresh: 380.4 MB
2026-11-20T10:59:59Z PPU: trace started (full)
2026-11-20T10:59:59Z PPU: refresh started, request dd8e9e48-e97b-4991-9e32-01b99212ad49
2026-11-20T11:01:09Z PPU: refresh failed (Failed) other
2026-11-20T11:01:40Z PPU: trace captured 241 events: ProgressReportEnd 218, ExecutionMetrics 10, CommandEnd 8, Error 5
```
