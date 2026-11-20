# Harness run 20261120T141020Z-v19-e764

- Task: refresh
- Variant: v19-pq-heavy-10m
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 3991e313-a86e-4e6c-9a79-f747ccd83053
- Refresh parallelism requested: 6

## F64-NE

- Result: **failed** (M evaluation memory limit)
- Peak 2,262 MB, Power Query 2,258 MB, duration 1 min, CPU 253 s, rows 1,854,909, model n/a (no size)
- Refresh request 28105cbd-a045-42a4-8df2-5cdd5b0ab86c, 2026-11-20T14:11:33.67 to 2026-11-20T14:12:58.177, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v19-pq-heavy-10m on F64-NE data-1m-v1.
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T12:30:33Z): peak 2,262 MB vs 623 MB (+1,639 MB), Power Query 2,258 MB vs 583 MB, model n/a vs 72 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (74%); F16 5,120 MB: fits (44%); F32 10,240 MB: fits (22%); F64 25,600 MB: fits (9%); PPU 102,400 MB: fits (2%); F2-csv 3,066 MB: fits (74%); F2-sql 3,066 MB: fits (74%); F64-NE 25,600 MB: fits (9%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
The M evaluation exceeded the memory limit. To address the issue consider optimizing the M expressions, reducing the concurrency of operations that are memory intensive or upgrading to increase the available memory. Container exited unexpectedly with code 0x0000DEAD. PID: 28548.
Used features: Odbc.DataSource/Microsoft ODBC Driver for Google BigQuery/2.6.1.1003/BigQuery/2.;Container exited unexpectedly with code 0x0000DEAD. PID: 28548.
Used features: Odbc.DataSource/Microsoft ODBC Driver for Google BigQuery/2.6.1.1003/BigQuery/2.
Container exited unexpectedly with code 0x0000DEAD. PID: 28548.
Used features: Odbc.DataSource/Microsoft ODBC Driver for Google BigQuery/2.6.1.1003/BigQuery/2.
Container exited unexpectedly with code 0x0000DEAD. PID: 28548..
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
```

Steps running or failed when it stopped:

```
                                          Object           OperationDetailName                        Began Ended EndStatus
            6fdedc77-c7d5-464b-87f4-07d0759e8c76          TabularSequencePoint 2026-11-20T14:11:37.8958481Z  None          
               PQ Delivery Days.PQ Delivery Days                TabularRefresh 2026-11-20T14:11:38.0227066Z  None          
       PQ Customer Segments.PQ Customer Segments                TabularRefresh 2026-11-20T14:11:38.0374982Z  None          
                 PQ Customer RFM.PQ Customer RFM                TabularRefresh 2026-11-20T14:11:38.0688254Z  None          
                 PQ Customer RFM.PQ Customer RFM                    ExecuteSql 2026-11-20T14:11:38.7520296Z  None          
       PQ Customer Segments.PQ Customer Segments                    ExecuteSql 2026-11-20T14:11:38.7631226Z  None          
               PQ Delivery Days.PQ Delivery Days                    ExecuteSql 2026-11-20T14:11:38.7650652Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba                TabularRefresh 2026-11-20T14:11:48.8115853Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba                       Process 2026-11-20T14:11:53.3038941Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba                      ReadData 2026-11-20T14:11:53.3058917Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f      RelationshipBuildPrepare 2026-11-20T14:12:00.8554496Z  None          
                                                                      Rollback 2026-11-20T14:12:57.9976878Z  None          
                                                                        Commit 2026-11-20T14:12:58.4564514Z  None          
            6fdedc77-c7d5-464b-87f4-07d0759e8c76                 TabularCommit 2026-11-20T14:12:58.4566936Z  None          
            6fdedc77-c7d5-464b-87f4-07d0759e8c76 MetadataTraversalDuringBackup 2026-11-20T14:12:58.6889554Z  None          
            6fdedc77-c7d5-464b-87f4-07d0759e8c76                        Backup 2026-11-20T14:12:58.6962314Z  None          
```

Slowest steps:

```
                                                Object OperationDetailName  DurationSec  CpuSec   Rows
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         13.7     2.0      0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh         10.8     0.2      0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh         10.7     0.2      0
       PQ Top Products by Year.PQ Top Products by Year      TabularRefresh          8.4     0.1      0
       PQ Top Products by Year.PQ Top Products by Year          ExecuteSql          7.9     0.0      0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          6.6     1.9      0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          6.4     1.9 104990
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          6.4     0.0      0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          6.2     0.0      0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          6.0     0.0      0
                       PQ Basket Pairs.PQ Basket Pairs      TabularRefresh          5.6     0.0      0
                       PQ Basket Pairs.PQ Basket Pairs          ExecuteSql          5.5     0.0      0
```

**Screenshot: the refresh error of v19-pq-heavy-10m on F64-NE in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-ne-v19-pq-heavy-10m-m-evaluation-memory.png**

## Log

```
2026-11-20T14:11:00Z run 20261120T141020Z-v19-e764: variant=v19-pq-heavy-10m data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T14:11:10Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T14:11:13Z F64-NE: v19-pq-heavy-10m is 6fdedc77-c7d5-464b-87f4-07d0759e8c76, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T14:11:16Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T14:11:33Z F64-NE: model size in memory before the refresh: 0.1 MB
2026-11-20T14:11:33Z F64-NE: refresh started, request 28105cbd-a045-42a4-8df2-5cdd5b0ab86c
2026-11-20T14:13:14Z F64-NE: refresh failed (Failed) M evaluation memory limit
2026-11-20T14:13:14Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T14:14:49Z F64-NE: ExecutionMetrics event found
```
