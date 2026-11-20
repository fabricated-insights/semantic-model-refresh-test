# Harness run 20261120T105250Z-v99b-f55a

- Task: refresh
- Variant: v99b-one-sales-copy
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3eee1c8a-f64c-45f2-b22f-567ea7f06c5c
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 14,566 MB, Power Query 14,515 MB, duration 1 min, CPU 178 s, rows 216,067, model n/a (no size)
- Refresh request b1a7954a-9ea0-42ae-a7f7-5b22bb09e84c, 2026-11-20T10:54:07.18 to 2026-11-20T10:55:04.593, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99b-one-sales-copy on PPU data-1m-v1: refreshed, peak 26,194 MB (2026-11-20T01:45:33Z).
  - Peak change: -11,628 MB (-44.4%). **FLAG: peak changed by more than 1%**
  - **FLAG: result changed from refreshed to failed**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 14,566 MB vs 666 MB (+13,900 MB), Power Query 14,515 MB vs 591 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 522 MB. The refresh may use the SKU maximum minus this: 101,878 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,544 MB: OVER (572%); F16 4,598 MB: OVER (317%); F32 9,718 MB: OVER (150%); F64 25,078 MB: fits (58%); PPU 101,878 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         14.5     1.8      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          7.9     1.7      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          7.7     1.6 104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          6.5     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          2.8     0.8      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          2.2     0.1      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          1.9     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          1.8     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.6     0.1      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          1.4     0.1      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          1.2     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          1.2     0.0      0
```

**Screenshot: the refresh error of v99b-one-sales-copy on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99b-one-sales-copy-refresh-error.png**

## Log

```
2026-11-20T10:53:28Z run 20261120T105250Z-v99b-f55a: variant=v99b-one-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T10:53:38Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T10:53:47Z PPU: v99b-one-sales-copy is 03d0c1da-34b0-4aba-85d6-ed2d23257e66, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T10:54:03Z PPU: model size in memory before the refresh: 521.5 MB
2026-11-20T10:54:07Z PPU: trace started (full)
2026-11-20T10:54:07Z PPU: refresh started, request b1a7954a-9ea0-42ae-a7f7-5b22bb09e84c
2026-11-20T10:55:17Z PPU: refresh failed (Failed) other
2026-11-20T10:55:48Z PPU: trace captured 196 events: ProgressReportEnd 173, ExecutionMetrics 10, CommandEnd 8, Error 5
```
