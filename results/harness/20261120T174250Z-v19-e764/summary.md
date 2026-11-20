# Harness run 20261120T174250Z-v19-e764

- Task: refresh
- Variant: v19-pq-heavy-10m
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 6f0a725b-d62d-4281-93a9-e14d1aac3dcd
- Refresh parallelism requested: 6

## F64-NE

- Result: **failed** (M evaluation memory limit)
- Peak 1,143 MB, Power Query 1,009 MB, duration 1 min, CPU 202 s, rows 1,431,133, model n/a (no size)
- Refresh request 05c02abe-6353-497f-a6a9-dce45aeebd0a, 2026-11-20T17:43:50.147 to 2026-11-20T17:45:01.767, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v19-pq-heavy-10m on F64-NE data-1m-v1: failed, peak 1,961 MB (2026-11-20T16:02:15Z).
  - Peak change: -818 MB (-41.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T16:08:01Z): peak 1,143 MB vs 648 MB (+495 MB), Power Query 1,009 MB vs 616 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (37%); F16 5,120 MB: fits (22%); F32 10,240 MB: fits (11%); F64 25,600 MB: fits (4%); PPU 102,400 MB: fits (1%); F2-csv 3,066 MB: fits (37%); F2-sql 3,066 MB: fits (37%); F64-NE 25,600 MB: fits (4%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
The M evaluation exceeded the memory limit. To address the issue consider optimizing the M expressions, reducing the concurrency of operations that are memory intensive or upgrading to increase the available memory. Container exited unexpectedly with code 0x0000DEAD. PID: 18528.
Used features: (none).;Container exited unexpectedly with code 0x0000DEAD. PID: 18528.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 18528.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 18528..
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
```

Steps running or failed when it stopped:

```
                                          Object      OperationDetailName                        Began Ended EndStatus
            6fdedc77-c7d5-464b-87f4-07d0759e8c76     TabularSequencePoint 2026-11-20T17:43:56.3883412Z  None          
                 PQ Customer RFM.PQ Customer RFM           TabularRefresh  2026-11-20T17:43:56.512331Z  None          
       PQ Customer Segments.PQ Customer Segments           TabularRefresh 2026-11-20T17:43:56.5277052Z  None          
               PQ Delivery Days.PQ Delivery Days           TabularRefresh 2026-11-20T17:43:56.5428658Z  None          
       PQ Customer Segments.PQ Customer Segments               ExecuteSql 2026-11-20T17:43:57.0242979Z  None          
                 PQ Customer RFM.PQ Customer RFM               ExecuteSql 2026-11-20T17:43:57.0388197Z  None          
               PQ Delivery Days.PQ Delivery Days               ExecuteSql 2026-11-20T17:43:57.0417914Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T17:44:11.0988349Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba                  Process 2026-11-20T17:44:12.3250048Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba                 ReadData 2026-11-20T17:44:12.3272855Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T17:44:14.4965415Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
                         PQ Top Products by Year.PQ Top Products by Year      TabularRefresh         15.2     0.1      0
                                         PQ Basket Pairs.PQ Basket Pairs      TabularRefresh         14.5     0.1      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         14.4     1.7      0
                         PQ Top Products by Year.PQ Top Products by Year          ExecuteSql         14.4     0.0      0
                                         PQ Basket Pairs.PQ Basket Pairs          ExecuteSql         14.1     0.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          7.3     0.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          6.6     1.6      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          6.4     1.6 104990
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.7     0.1      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.4     0.6      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          1.4     0.0      0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba          ExecuteSql          1.2     0.0      0
```

**Screenshot: the refresh error of v19-pq-heavy-10m on F64-NE in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-ne-v19-pq-heavy-10m-m-evaluation-memory.png**

## Log

```
2026-11-20T17:43:24Z run 20261120T174250Z-v19-e764: variant=v19-pq-heavy-10m data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T17:43:32Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T17:43:33Z F64-NE: v19-pq-heavy-10m is 6fdedc77-c7d5-464b-87f4-07d0759e8c76, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T17:43:34Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T17:43:50Z F64-NE: model size in memory before the refresh: 0.1 MB
2026-11-20T17:43:51Z F64-NE: refresh started, request 05c02abe-6353-497f-a6a9-dce45aeebd0a
2026-11-20T17:45:31Z F64-NE: refresh failed (Failed) M evaluation memory limit
2026-11-20T17:45:32Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T17:47:07Z F64-NE: ExecutionMetrics event found
```
