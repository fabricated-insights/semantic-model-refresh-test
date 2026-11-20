# Harness run 20261120T142914Z-v99b-061e

- Task: refresh
- Variant: v99b-one-sales-copy
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: bc09f9aa-18af-43e4-a6fc-4481ea6baea1
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 13,884 MB, Power Query 13,832 MB, duration 0 min, CPU 90 s, rows 216,067, model n/a (no size)
- Refresh request 6306ad06-7aa8-4752-b8dd-44e8b23776eb, 2026-11-20T14:32:03.457 to 2026-11-20T14:32:32.367, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99b-one-sales-copy on F64 data-1m-v1: failed, peak 15,075 MB (2026-11-20T09:11:03Z).
  - Peak change: -1,191 MB (-7.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 13,884 MB vs 667 MB (+13,217 MB), Power Query 13,832 MB vs 592 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (453%); F16 5,120 MB: OVER (271%); F32 10,240 MB: OVER (136%); F64 25,600 MB: fits (54%); PPU 102,400 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
            1fe6d06d-415b-469f-9bfa-d9105a1aa0a2     TabularSequencePoint  2026-11-20T14:32:04.637093Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T14:32:04.7557569Z  None          
                           Sales Flat.Sales Flat           TabularRefresh  2026-11-20T14:32:04.756196Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T14:32:04.8958701Z  None          
                           Sales Flat.Sales Flat               ExecuteSql 2026-11-20T14:32:04.9032544Z  None          
                   Customer Stats.Customer Stats           TabularRefresh 2026-11-20T14:32:05.8154291Z  None          
                   Customer Stats.Customer Stats               ExecuteSql 2026-11-20T14:32:05.8437813Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T14:32:06.4311968Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          8.0     1.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          3.9     0.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          3.9     1.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          3.8     0.9 104990
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.5     0.1      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          1.1     0.0      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.1     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          0.9     0.0      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          0.8     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          0.8     0.3      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          0.7     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          0.5     0.3      0
```

**Screenshot: the refresh error of v99b-one-sales-copy on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99b-one-sales-copy-refresh-error.png**

## Log

```
2026-11-20T14:31:28Z run 20261120T142914Z-v99b-061e: variant=v99b-one-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T14:31:40Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:31:42Z F64: v99b-one-sales-copy is 1fe6d06d-415b-469f-9bfa-d9105a1aa0a2, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:32:03Z F64: model size in memory before the refresh: 0.1 MB
2026-11-20T14:32:03Z F64: refresh started, request 6306ad06-7aa8-4752-b8dd-44e8b23776eb
2026-11-20T14:32:48Z F64: refresh failed (Failed) other
2026-11-20T14:32:49Z F64: monitoring database Monitoring KQL database
2026-11-20T14:34:24Z F64: ExecutionMetrics event found
```
