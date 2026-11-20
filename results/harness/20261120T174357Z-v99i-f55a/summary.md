# Harness run 20261120T174357Z-v99i-f55a

- Task: refresh
- Variant: v99i-buffer-stg-sales
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6cb2cb0a-e48c-4b07-9d39-be3ee88ec2f2
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 14,251 MB, Power Query 14,166 MB, duration 1 min, CPU 200 s, rows 10,559,477, model n/a (no size)
- Refresh request 837339b6-e8bd-4ac4-b3a8-eb0f0e0cc9e1, 2026-11-20T17:45:04.053 to 2026-11-20T17:46:01.78, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99i-buffer-stg-sales on PPU data-1m-v1: failed, peak 14,373 MB (2026-11-20T11:52:37Z).
  - Peak change: -122 MB (-0.8%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 14,251 MB vs 604 MB (+13,647 MB), Power Query 14,166 MB vs 529 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 541 MB. The refresh may use the SKU maximum minus this: 101,859 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,525 MB: OVER (564%); F16 4,579 MB: OVER (311%); F32 9,699 MB: OVER (147%); F64 25,059 MB: fits (57%); PPU 101,859 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                                     Product Date Grid.Product Date Grid            VertiPaq         12.7    12.6        0
                                     Product Date Grid.Product Date Grid             Process         10.5     9.7        0
                                     Product Date Grid.Product Date Grid      TabularRefresh         10.5     9.7        0
                                     Product Date Grid.Product Date Grid            ReadData          9.7     9.7 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          8.5     2.4        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          6.9     2.3        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          6.7     2.2   104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          1.5     0.0        0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.5     0.1        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.3     0.7        0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.2     0.1        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          1.0     0.7        0
```

**Screenshot: the refresh error of v99i-buffer-stg-sales on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99i-buffer-stg-sales-refresh-error.png**

## Log

```
2026-11-20T17:44:30Z run 20261120T174357Z-v99i-f55a: variant=v99i-buffer-stg-sales data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T17:44:35Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T17:44:44Z PPU: v99i-buffer-stg-sales is c22581d6-175d-489e-b120-eb36a486ebd1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T17:45:00Z PPU: model size in memory before the refresh: 540.6 MB
2026-11-20T17:45:03Z PPU: trace started (full)
2026-11-20T17:45:04Z PPU: refresh started, request 837339b6-e8bd-4ac4-b3a8-eb0f0e0cc9e1
2026-11-20T17:46:14Z PPU: refresh failed (Failed) other
2026-11-20T17:46:45Z PPU: trace captured 352 events: ProgressReportEnd 329, ExecutionMetrics 10, CommandEnd 8, Error 5
```
