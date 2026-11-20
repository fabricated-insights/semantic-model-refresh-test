# Harness run 20261120T114752Z-v99i-f55a

- Task: refresh
- Variant: v99i-buffer-stg-sales
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 16e58caf-3880-445b-aaa6-327c8e0d8957
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 14,373 MB, Power Query 14,289 MB, duration 1 min, CPU 216 s, rows 10,559,477, model n/a (no size)
- Refresh request ebd27517-6ab0-4c87-963b-6f40d32d4a64, 2026-11-20T11:50:55.727 to 2026-11-20T11:51:56.46, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99i-buffer-stg-sales on PPU data-1m-v1: refreshed, peak 25,773 MB (2026-11-20T05:14:09Z).
  - Peak change: -11,400 MB (-44.2%). **FLAG: peak changed by more than 1%**
  - **FLAG: result changed from refreshed to failed**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 14,373 MB vs 666 MB (+13,707 MB), Power Query 14,289 MB vs 591 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 541 MB. The refresh may use the SKU maximum minus this: 101,859 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,525 MB: OVER (569%); F16 4,579 MB: OVER (314%); F32 9,699 MB: OVER (148%); F64 25,059 MB: fits (57%); PPU 101,859 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                                     Product Date Grid.Product Date Grid            VertiPaq         13.9    13.8        0
                                     Product Date Grid.Product Date Grid             Process         10.6     9.7        0
                                     Product Date Grid.Product Date Grid      TabularRefresh         10.6     9.7        0
                                     Product Date Grid.Product Date Grid            ReadData          9.7     9.6 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          9.7     2.5        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          7.0     2.4        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          6.8     2.3   104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          2.5     0.0        0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          2.5     0.1        0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          2.4     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.4     0.7        0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.2     0.2        0
```

**Screenshot: the refresh error of v99i-buffer-stg-sales on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99i-buffer-stg-sales-refresh-error.png**

## Log

```
2026-11-20T11:50:14Z run 20261120T114752Z-v99i-f55a: variant=v99i-buffer-stg-sales data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T11:50:21Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:50:30Z PPU: v99i-buffer-stg-sales is c22581d6-175d-489e-b120-eb36a486ebd1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:50:52Z PPU: model size in memory before the refresh: 540.6 MB
2026-11-20T11:50:55Z PPU: trace started (full)
2026-11-20T11:50:55Z PPU: refresh started, request ebd27517-6ab0-4c87-963b-6f40d32d4a64
2026-11-20T11:52:06Z PPU: refresh failed (Failed) other
2026-11-20T11:52:37Z PPU: trace captured 352 events: ProgressReportEnd 329, ExecutionMetrics 10, CommandEnd 8, Error 5
```
