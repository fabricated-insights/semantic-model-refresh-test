# Harness run 20261120T083929Z-v99-061e

- Task: refresh
- Variant: v99-kitchen-sink
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 2eca5d2d-5d34-4f86-9b96-487edf9d942e
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 14,702 MB, Power Query 14,623 MB, duration 1 min, CPU 121 s, rows 10,329,373, model n/a (no size)
- Refresh request 6a3760cd-26b1-4eb2-bffb-7985989b54f6, 2026-11-20T08:40:34.717 to 2026-11-20T08:41:12.18, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99-kitchen-sink on F64 data-1m-v1: failed, peak 25,589 MB (2026-11-20T00:38:28Z).
  - Peak change: -10,887 MB (-42.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 14,702 MB vs 716 MB (+13,986 MB), Power Query 14,623 MB vs 527 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (480%); F16 5,120 MB: OVER (287%); F32 10,240 MB: OVER (144%); F64 25,600 MB: fits (57%); PPU 102,400 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          9.2     1.0        0
                                     Product Date Grid.Product Date Grid            VertiPaq          6.4     6.3        0
                                     Product Date Grid.Product Date Grid      TabularRefresh          5.4     5.0        0
                                     Product Date Grid.Product Date Grid             Process          5.3     5.0        0
                                     Product Date Grid.Product Date Grid            ReadData          5.0     4.9 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          4.7     0.0        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          4.4     1.0        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          4.3     0.9   104990
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          2.3     0.0        0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          2.1     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.2     0.3        0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.0     0.0        0
```

**Screenshot: the refresh error of v99-kitchen-sink on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99-kitchen-sink-refresh-error.png**

## Log

```
2026-11-20T08:40:03Z run 20261120T083929Z-v99-061e: variant=v99-kitchen-sink data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T08:40:18Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:40:21Z F64: v99-kitchen-sink is 768aac35-6135-47bf-bbb0-c54b0aa43296, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:40:34Z F64: model size in memory before the refresh: 0.1 MB
2026-11-20T08:40:34Z F64: refresh started, request 6a3760cd-26b1-4eb2-bffb-7985989b54f6
2026-11-20T08:41:20Z F64: refresh failed (Failed) other
2026-11-20T08:41:20Z F64: monitoring database Monitoring KQL database
2026-11-20T08:42:56Z F64: ExecutionMetrics event found
```
