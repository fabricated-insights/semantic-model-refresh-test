# Harness run 20261120T143529Z-v99c-061e

- Task: refresh
- Variant: v99c-crossjoin-only
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: d652c2e3-9eae-4451-8a99-97ecbac0e415
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 14,510 MB, Power Query 14,431 MB, duration 1 min, CPU 112 s, rows 10,329,373, model n/a (no size)
- Refresh request 418d0164-f857-4313-b1d6-643f1e6196ba, 2026-11-20T14:38:28.96 to 2026-11-20T14:39:01.747, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99c-crossjoin-only on F64 data-1m-v1: failed, peak 15,008 MB (2026-11-20T09:18:47Z).
  - Peak change: -498 MB (-3.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 14,510 MB vs 667 MB (+13,843 MB), Power Query 14,431 MB vs 592 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (473%); F16 5,120 MB: OVER (283%); F32 10,240 MB: OVER (142%); F64 25,600 MB: fits (57%); PPU 102,400 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
```

Steps running or failed when it stopped:

```
                                          Object      OperationDetailName                        Began Ended EndStatus
            daa7e567-713a-45fb-9a38-cd372ab42dd8     TabularSequencePoint 2026-11-20T14:38:30.0682474Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T14:38:30.1409446Z  None          
                           Sales Flat.Sales Flat           TabularRefresh 2026-11-20T14:38:30.1563335Z  None          
                   Customer Stats.Customer Stats           TabularRefresh 2026-11-20T14:38:30.1714979Z  None          
                   Customer Stats.Customer Stats               ExecuteSql 2026-11-20T14:38:30.2766268Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T14:38:30.2816332Z  None          
                           Sales Flat.Sales Flat               ExecuteSql 2026-11-20T14:38:30.2842867Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T14:38:31.6376891Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec     Rows
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          8.8     0.8        0
                                     Product Date Grid.Product Date Grid            VertiPaq          5.9     5.9        0
                                     Product Date Grid.Product Date Grid             Process          4.9     4.6        0
                                     Product Date Grid.Product Date Grid      TabularRefresh          4.9     4.6        0
                                     Product Date Grid.Product Date Grid            ReadData          4.5     4.5 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          4.4     0.8        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          4.3     0.0        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          4.3     0.8   104990
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          0.8     0.1        0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          0.7     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          0.7     0.3        0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          0.6     0.0        0
```

**Screenshot: the refresh error of v99c-crossjoin-only on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99c-crossjoin-only-refresh-error.png**

## Log

```
2026-11-20T14:37:53Z run 20261120T143529Z-v99c-061e: variant=v99c-crossjoin-only data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T14:38:03Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:38:06Z F64: v99c-crossjoin-only is daa7e567-713a-45fb-9a38-cd372ab42dd8, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:38:28Z F64: model size in memory before the refresh: 0.1 MB
2026-11-20T14:38:29Z F64: refresh started, request 418d0164-f857-4313-b1d6-643f1e6196ba
2026-11-20T14:39:14Z F64: refresh failed (Failed) other
2026-11-20T14:39:14Z F64: monitoring database Monitoring KQL database
2026-11-20T14:41:51Z F64: ExecutionMetrics event found
```
