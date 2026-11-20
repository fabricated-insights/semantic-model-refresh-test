# Harness run 20261120T151357Z-v99h-061e

- Task: refresh
- Variant: v99h-staging-buffers
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e7ab3aa2-151c-4a8d-9ae3-d7c2857dcade
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 13,985 MB, Power Query 13,901 MB, duration 1 min, CPU 129 s, rows 10,559,477, model n/a (no size)
- Refresh request f6c78707-5238-48b9-9c16-ec68111fc579, 2026-11-20T15:17:09.417 to 2026-11-20T15:17:47.703, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99h-staging-buffers on F64 data-1m-v1: failed, peak 14,286 MB (2026-11-20T09:59:58Z).
  - Peak change: -301 MB (-2.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 13,985 MB vs 667 MB (+13,318 MB), Power Query 13,901 MB vs 592 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (456%); F16 5,120 MB: OVER (273%); F32 10,240 MB: OVER (137%); F64 25,600 MB: fits (55%); PPU 102,400 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
            6754d363-b82c-451a-a473-4f6d0b92e672     TabularSequencePoint 2026-11-20T15:17:12.2557067Z  None          
                   Customer Stats.Customer Stats           TabularRefresh 2026-11-20T15:17:12.3589697Z  None          
                           Sales Flat.Sales Flat           TabularRefresh 2026-11-20T15:17:12.3737122Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T15:17:12.3744765Z  None          
                   Customer Stats.Customer Stats               ExecuteSql  2026-11-20T15:17:12.487934Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql  2026-11-20T15:17:12.490783Z  None          
                           Sales Flat.Sales Flat               ExecuteSql 2026-11-20T15:17:12.4971278Z  None          
      Model.15d460ac-5121-4fa3-9240-b70400d77763 RelationshipBuildPrepare 2026-11-20T15:17:14.0561197Z  None          
      Model.55fa90e1-00c5-4666-8bc8-dde516c69228 RelationshipBuildPrepare 2026-11-20T15:17:14.0589457Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T15:17:14.0616828Z  None          
      Model.7a71d08b-0c26-46a2-b754-69b8e39a97f9 RelationshipBuildPrepare 2026-11-20T15:17:21.3374348Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec     Rows
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          8.6     1.2        0
                                     Product Date Grid.Product Date Grid            VertiPaq          6.2     6.2        0
                                     Product Date Grid.Product Date Grid             Process          5.1     4.7        0
                                     Product Date Grid.Product Date Grid      TabularRefresh          5.1     4.7        0
                                     Product Date Grid.Product Date Grid            ReadData          4.6     4.6 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          4.6     1.1        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          4.5     1.1   104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          3.9     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.6     0.3        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          1.1     0.0        0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          0.9     0.1        0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          0.7     0.0        0
```

**Screenshot: the refresh error of v99h-staging-buffers on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99h-staging-buffers-refresh-error.png**

## Log

```
2026-11-20T15:16:36Z run 20261120T151357Z-v99h-061e: variant=v99h-staging-buffers data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T15:16:43Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T15:16:46Z F64: v99h-staging-buffers is 6754d363-b82c-451a-a473-4f6d0b92e672, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T15:17:09Z F64: model size in memory before the refresh: 0.4 MB
2026-11-20T15:17:09Z F64: refresh started, request f6c78707-5238-48b9-9c16-ec68111fc579
2026-11-20T15:17:54Z F64: refresh failed (Failed) other
2026-11-20T15:17:55Z F64: monitoring database Monitoring KQL database
2026-11-20T15:20:32Z F64: ExecutionMetrics event found
```
