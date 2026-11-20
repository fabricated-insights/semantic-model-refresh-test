# Harness run 20261120T164945Z-v99b-f55a

- Task: refresh
- Variant: v99b-one-sales-copy
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: c05dd58c-b304-42cf-b2fa-8ba37aafe1af
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 14,741 MB, Power Query 14,689 MB, duration 1 min, CPU 241 s, rows 216,067, model n/a (no size)
- Refresh request ac279c85-8767-474b-8a85-529d3b3c7fd6, 2026-11-20T16:51:03.077 to 2026-11-20T16:52:14.413, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99b-one-sales-copy on PPU data-1m-v1: failed, peak 14,566 MB (2026-11-20T10:55:48Z).
  - Peak change: +175 MB (+1.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 14,741 MB vs 604 MB (+14,137 MB), Power Query 14,689 MB vs 529 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 522 MB. The refresh may use the SKU maximum minus this: 101,878 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,544 MB: OVER (579%); F16 4,598 MB: OVER (321%); F32 9,718 MB: OVER (152%); F64 25,078 MB: fits (59%); PPU 101,878 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         14.7     1.6      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          7.7     0.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          6.9     1.6      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          6.8     1.5 104990
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          2.8     0.1      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          2.7     0.1      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          2.6     0.0      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          2.5     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.1     0.6      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          0.8     0.5      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          0.8     0.5 100450
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          0.7     0.1      0
```

**Screenshot: the refresh error of v99b-one-sales-copy on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99b-one-sales-copy-refresh-error.png**

## Log

```
2026-11-20T16:50:26Z run 20261120T164945Z-v99b-f55a: variant=v99b-one-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T16:50:35Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T16:50:44Z PPU: v99b-one-sales-copy is 03d0c1da-34b0-4aba-85d6-ed2d23257e66, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T16:50:59Z PPU: model size in memory before the refresh: 521.5 MB
2026-11-20T16:51:02Z PPU: trace started (full)
2026-11-20T16:51:03Z PPU: refresh started, request ac279c85-8767-474b-8a85-529d3b3c7fd6
2026-11-20T16:52:43Z PPU: refresh failed (Failed) other
2026-11-20T16:53:14Z PPU: trace captured 196 events: ProgressReportEnd 173, ExecutionMetrics 10, CommandEnd 8, Error 5
```
