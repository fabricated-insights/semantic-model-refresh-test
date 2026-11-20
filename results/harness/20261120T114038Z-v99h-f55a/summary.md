# Harness run 20261120T114038Z-v99h-f55a

- Task: refresh
- Variant: v99h-staging-buffers
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: fa625626-17e2-40f9-a472-358216e797c3
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 14,759 MB, Power Query 14,675 MB, duration 2 min, CPU 360 s, rows 10,559,477, model n/a (no size)
- Refresh request 9fff9de6-addb-4bc7-b7d3-ce7e9f65a89b, 2026-11-20T11:44:01.767 to 2026-11-20T11:46:16.343, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99h-staging-buffers on PPU data-1m-v1: refreshed, peak 25,832 MB (2026-11-20T04:28:44Z).
  - Peak change: -11,073 MB (-42.9%). **FLAG: peak changed by more than 1%**
  - **FLAG: result changed from refreshed to failed**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 14,759 MB vs 666 MB (+14,093 MB), Power Query 14,675 MB vs 591 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 543 MB. The refresh may use the SKU maximum minus this: 101,857 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,523 MB: OVER (585%); F16 4,577 MB: OVER (322%); F32 9,697 MB: OVER (152%); F64 25,057 MB: fits (59%); PPU 101,857 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                                                       Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         38.1     3.2        0
                                                       Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process         19.8     3.1        0
                                                       Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData         19.6     3.0   104990
                                                       Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql         17.6     0.0        0
                                                                          Product Date Grid.Product Date Grid             Process         17.4    12.4        0
                                                                          Product Date Grid.Product Date Grid      TabularRefresh         17.4    12.4        0
                                                                          Product Date Grid.Product Date Grid            VertiPaq         16.3    12.5        0
                                                                          Product Date Grid.Product Date Grid            ReadData         16.1    12.3 10113306
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh         12.2     0.2        0
                                     Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh         11.8     1.0        0
                                                             Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh         11.5     0.1        0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f             Process         11.4     0.0        0
```

**Screenshot: the refresh error of v99h-staging-buffers on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99h-staging-buffers-refresh-error.png**

## Log

```
2026-11-20T11:43:01Z run 20261120T114038Z-v99h-f55a: variant=v99h-staging-buffers data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T11:43:08Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:43:17Z PPU: v99h-staging-buffers is fceac6f8-d619-41bc-83ea-24304ed40142, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:43:56Z PPU: model size in memory before the refresh: 542.7 MB
2026-11-20T11:44:01Z PPU: trace started (full)
2026-11-20T11:44:04Z PPU: refresh started, request 9fff9de6-addb-4bc7-b7d3-ce7e9f65a89b
2026-11-20T11:46:44Z PPU: refresh failed (Failed) other
2026-11-20T11:47:15Z PPU: trace captured 352 events: ProgressReportEnd 329, ExecutionMetrics 10, CommandEnd 8, Error 5
```
