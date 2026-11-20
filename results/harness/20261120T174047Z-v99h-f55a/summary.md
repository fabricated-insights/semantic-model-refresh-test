# Harness run 20261120T174047Z-v99h-f55a

- Task: refresh
- Variant: v99h-staging-buffers
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 397b21d5-6592-4ca1-988d-40d6a6313d1a
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 14,272 MB, Power Query 14,188 MB, duration 1 min, CPU 223 s, rows 10,559,477, model n/a (no size)
- Refresh request c3537451-ba80-4b2c-9fb1-76107efe03ff, 2026-11-20T17:41:45.3 to 2026-11-20T17:42:46.757, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99h-staging-buffers on PPU data-1m-v1: failed, peak 14,759 MB (2026-11-20T11:47:15Z).
  - Peak change: -487 MB (-3.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 14,272 MB vs 604 MB (+13,668 MB), Power Query 14,188 MB vs 529 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 543 MB. The refresh may use the SKU maximum minus this: 101,857 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,523 MB: OVER (566%); F16 4,577 MB: OVER (312%); F32 9,697 MB: OVER (147%); F64 25,057 MB: fits (57%); PPU 101,857 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         16.8     1.5        0
                                     Product Date Grid.Product Date Grid            VertiPaq         10.2    10.2        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          8.6     0.0        0
                                     Product Date Grid.Product Date Grid             Process          8.2     7.5        0
                                     Product Date Grid.Product Date Grid      TabularRefresh          8.2     7.5        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          8.2     1.5        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          8.0     1.5   104990
                                     Product Date Grid.Product Date Grid            ReadData          7.5     7.5 10113306
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          2.3     0.1        0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          2.0     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.7     0.6        0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.0     0.1        0
```

**Screenshot: the refresh error of v99h-staging-buffers on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99h-staging-buffers-refresh-error.png**

## Log

```
2026-11-20T17:41:11Z run 20261120T174047Z-v99h-f55a: variant=v99h-staging-buffers data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T17:41:18Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T17:41:27Z PPU: v99h-staging-buffers is fceac6f8-d619-41bc-83ea-24304ed40142, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T17:41:41Z PPU: model size in memory before the refresh: 542.7 MB
2026-11-20T17:41:45Z PPU: trace started (full)
2026-11-20T17:41:45Z PPU: refresh started, request c3537451-ba80-4b2c-9fb1-76107efe03ff
2026-11-20T17:42:55Z PPU: refresh failed (Failed) other
2026-11-20T17:43:26Z PPU: trace captured 352 events: ProgressReportEnd 329, ExecutionMetrics 10, CommandEnd 8, Error 5
```
