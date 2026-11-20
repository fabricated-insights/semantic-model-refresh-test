# Harness run 20261120T165343Z-v99c-f55a

- Task: refresh
- Variant: v99c-crossjoin-only
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 069c7d99-dda4-42be-9611-7f79c6dd221d
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (other)
- Peak 14,323 MB, Power Query 14,244 MB, duration 1 min, CPU 183 s, rows 10,329,373, model n/a (no size)
- Refresh request 28aeff9d-6641-4e3a-814b-d34295d7c063, 2026-11-20T16:54:51.75 to 2026-11-20T16:55:43.44, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99c-crossjoin-only on PPU data-1m-v1: failed, peak 14,380 MB (2026-11-20T11:01:41Z).
  - Peak change: -57 MB (-0.4%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 14,323 MB vs 604 MB (+13,719 MB), Power Query 14,244 MB vs 529 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 380 MB. The refresh may use the SKU maximum minus this: 102,020 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,686 MB: OVER (533%); F16 4,740 MB: OVER (302%); F32 9,860 MB: OVER (145%); F64 25,220 MB: fits (57%); PPU 102,020 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         13.5     1.4        0
                                     Product Date Grid.Product Date Grid            VertiPaq         10.1    10.1        0
                                     Product Date Grid.Product Date Grid             Process          8.3     7.7        0
                                     Product Date Grid.Product Date Grid      TabularRefresh          8.3     7.7        0
                                     Product Date Grid.Product Date Grid            ReadData          7.6     7.6 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          7.6     1.3        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          7.4     1.2   104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          5.9     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.6     0.6        0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.0     0.2        0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          0.9     0.0        0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          0.8     0.0        0
```

**Screenshot: the refresh error of v99c-crossjoin-only on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v99c-crossjoin-only-refresh-error.png**

## Log

```
2026-11-20T16:54:17Z run 20261120T165343Z-v99c-f55a: variant=v99c-crossjoin-only data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T16:54:25Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T16:54:31Z PPU: v99c-crossjoin-only is 364f4109-e09b-4cda-a773-d642978613b4, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T16:54:48Z PPU: model size in memory before the refresh: 380.4 MB
2026-11-20T16:54:51Z PPU: trace started (full)
2026-11-20T16:54:51Z PPU: refresh started, request 28aeff9d-6641-4e3a-814b-d34295d7c063
2026-11-20T16:56:02Z PPU: refresh failed (Failed) other
2026-11-20T16:56:33Z PPU: trace captured 241 events: ProgressReportEnd 218, ExecutionMetrics 10, CommandEnd 8, Error 5
```
