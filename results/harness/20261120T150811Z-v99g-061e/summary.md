# Harness run 20261120T150811Z-v99g-061e

- Task: refresh
- Variant: v99g-sales-copy
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 472794ca-db65-4bce-a19d-abeae7385192
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 236 MB, Power Query 192 MB, duration 0 min, CPU 14 s, rows 267,977, model n/a (no size)
- Refresh request 23fc6f20-9a6a-41dc-a1ac-590dbf973707, 2026-11-20T15:11:14.947 to 2026-11-20T15:11:20.723, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99g-sales-copy on F64 data-1m-v1: failed, peak 398 MB (2026-11-20T09:55:38Z).
  - Peak change: -162 MB (-40.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 236 MB vs 667 MB (-431 MB), Power Query 192 MB vs 592 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 663 MB. The refresh may use the SKU maximum minus this: 24,937 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,403 MB: fits (10%); F16 4,457 MB: fits (5%); F32 9,577 MB: fits (2%); F64 24,937 MB: fits (1%); PPU 101,737 MB: fits (0%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
```

Steps running or failed when it stopped:

```
                                                                                                 Object      OperationDetailName                        Began Ended EndStatus
                                                                   7019bbb5-e7cd-4985-bc14-7af18c43cc4e     TabularSequencePoint 2026-11-20T15:11:17.3609557Z  None          
                                                       Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T15:11:17.5666301Z  None          
                                                 Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           TabularRefresh 2026-11-20T15:11:17.5837008Z  None          
                                                                          Customer Stats.Customer Stats           TabularRefresh 2026-11-20T15:11:17.5976514Z  None          
                                                       Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T15:11:17.7493609Z  None          
                                                                          Customer Stats.Customer Stats               ExecuteSql 2026-11-20T15:11:17.7500533Z  None          
                                                                                  Sales Flat.Sales Flat           TabularRefresh 2026-11-20T15:11:19.3170637Z  None          
                                                                                  Sales Flat.Sales Flat               ExecuteSql 2026-11-20T15:11:19.3708442Z  None          
                                                 Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59                  Process 2026-11-20T15:11:19.5890088Z  None          
                                                 Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59                 ReadData 2026-11-20T15:11:19.5913398Z  None          
                                                             Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T15:11:20.3618318Z  None          
                                                                    Product Date Grid.Product Date Grid           TabularRefresh 2026-11-20T15:11:20.3937651Z  None          
                                                                    Product Date Grid.Product Date Grid                  Process 2026-11-20T15:11:20.3994583Z  None          
                                                                    Product Date Grid.Product Date Grid                 ReadData 2026-11-20T15:11:20.4010117Z  None          
LocalDateTable_46319c04-1847-47b2-8182-70e3e853ff2b.LocalDateTable_46319c04-1847-47b2-8182-70e3e853ff2b           TabularRefresh 2026-11-20T15:11:20.5214675Z  None          
LocalDateTable_46319c04-1847-47b2-8182-70e3e853ff2b.LocalDateTable_46319c04-1847-47b2-8182-70e3e853ff2b                  Process 2026-11-20T15:11:20.5228575Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          2.7     0.2      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          2.5     0.1      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          2.1     0.0      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          2.0     0.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          1.8     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.7     0.8      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          0.9     0.7 100450
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          0.9     0.7      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          0.6     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b             Process          0.4     0.1      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b            ReadData          0.4     0.1   4018
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          0.4     0.1      0
```

**Screenshot: the refresh error of v99g-sales-copy on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99g-sales-copy-refresh-error.png**

## Log

```
2026-11-20T15:10:44Z run 20261120T150811Z-v99g-061e: variant=v99g-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T15:10:52Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T15:10:54Z F64: v99g-sales-copy is 7019bbb5-e7cd-4985-bc14-7af18c43cc4e, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T15:11:14Z F64: model size in memory before the refresh: 662.8 MB
2026-11-20T15:11:15Z F64: refresh started, request 23fc6f20-9a6a-41dc-a1ac-590dbf973707
2026-11-20T15:11:25Z F64: refresh failed (Failed) other
2026-11-20T15:11:25Z F64: monitoring database Monitoring KQL database
2026-11-20T15:13:01Z F64: ExecutionMetrics event found
```
