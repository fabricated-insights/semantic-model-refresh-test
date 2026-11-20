# Harness run 20261120T155803Z-v19-e764

- Task: refresh
- Variant: v19-pq-heavy-10m
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: d3616086-b43f-4e69-98a3-40f30796e87e
- Refresh parallelism requested: 6

## F64-NE

- Result: **failed** (M evaluation memory limit)
- Peak 1,961 MB, Power Query 1,880 MB, duration 1 min, CPU 201 s, rows 1,709,236, model n/a (no size)
- Refresh request 50eeb098-5343-4df0-acba-75bce45a57b8, 2026-11-20T15:59:26.88 to 2026-11-20T16:00:35.633, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v19-pq-heavy-10m on F64-NE data-1m-v1: failed, peak 2,262 MB (2026-11-20T14:14:52Z).
  - Peak change: -301 MB (-13.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T14:22:30Z): peak 1,961 MB vs 949 MB (+1,012 MB), Power Query 1,880 MB vs 904 MB, model n/a vs 72 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (64%); F16 5,120 MB: fits (38%); F32 10,240 MB: fits (19%); F64 25,600 MB: fits (8%); PPU 102,400 MB: fits (2%); F2-csv 3,066 MB: fits (64%); F2-sql 3,066 MB: fits (64%); F64-NE 25,600 MB: fits (8%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
The M evaluation exceeded the memory limit. To address the issue consider optimizing the M expressions, reducing the concurrency of operations that are memory intensive or upgrading to increase the available memory. Container exited unexpectedly with code 0x0000DEAD. PID: 19476.
Used features: (none).;Container exited unexpectedly with code 0x0000DEAD. PID: 19476.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 19476.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 19476..
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
```

Steps running or failed when it stopped:

```
                                          Object      OperationDetailName                        Began Ended EndStatus
            6fdedc77-c7d5-464b-87f4-07d0759e8c76     TabularSequencePoint  2026-11-20T15:59:28.938076Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T15:59:29.0373984Z  None          
               PQ Delivery Days.PQ Delivery Days           TabularRefresh 2026-11-20T15:59:29.0556778Z  None          
                 PQ Customer RFM.PQ Customer RFM           TabularRefresh 2026-11-20T15:59:29.1028653Z  None          
                 PQ Customer RFM.PQ Customer RFM               ExecuteSql 2026-11-20T15:59:29.8563901Z  None          
               PQ Delivery Days.PQ Delivery Days               ExecuteSql 2026-11-20T15:59:29.8682124Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba                  Process 2026-11-20T15:59:35.7138626Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba                 ReadData 2026-11-20T15:59:35.7156999Z  None          
       PQ Customer Segments.PQ Customer Segments           TabularRefresh 2026-11-20T15:59:43.3957734Z  None          
       PQ Customer Segments.PQ Customer Segments               ExecuteSql 2026-11-20T15:59:43.4616547Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T15:59:48.9540242Z  None          
```

Slowest steps:

```
                                                Object OperationDetailName  DurationSec  CpuSec  Rows
       PQ Top Products by Year.PQ Top Products by Year      TabularRefresh         14.4     0.1     0
       PQ Top Products by Year.PQ Top Products by Year          ExecuteSql         13.2     0.0     0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh         10.3     0.1     0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh         10.1     0.1     0
                       PQ Basket Pairs.PQ Basket Pairs      TabularRefresh          7.3     0.1     0
                       PQ Basket Pairs.PQ Basket Pairs          ExecuteSql          7.2     0.0     0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          7.1     1.6     0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          5.9     0.0     0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba          ExecuteSql          5.8     0.0     0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          5.8     0.0     0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          4.2     0.1     0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          3.9     0.0     0
```

**Screenshot: the refresh error of v19-pq-heavy-10m on F64-NE in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-ne-v19-pq-heavy-10m-m-evaluation-memory.png**

## Log

```
2026-11-20T15:58:48Z run 20261120T155803Z-v19-e764: variant=v19-pq-heavy-10m data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T15:58:59Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T15:59:09Z F64-NE: v19-pq-heavy-10m is 6fdedc77-c7d5-464b-87f4-07d0759e8c76, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T15:59:11Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T15:59:26Z F64-NE: model size in memory before the refresh: 0.1 MB
2026-11-20T15:59:27Z F64-NE: refresh started, request 50eeb098-5343-4df0-acba-75bce45a57b8
2026-11-20T16:00:37Z F64-NE: refresh failed (Failed) M evaluation memory limit
2026-11-20T16:00:37Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T16:02:12Z F64-NE: ExecutionMetrics event found
```
