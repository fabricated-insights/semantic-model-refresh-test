# Harness run 20261119T220331Z-v19-061e

- Task: refresh
- Variant: v19-pq-heavy-10m
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 17363fcc-d478-4e2d-aa78-750eaaadc97e
- Refresh parallelism requested: 6

## F64

- Result: **failed** (M evaluation memory limit)
- Peak 22,208 MB, Power Query 22,088 MB, duration 15 min, CPU 3,504 s, rows 2,563,134, model n/a (no size)
- Refresh request 3875fb2f-749c-496d-b25e-6e2d15cdbc97, 2026-11-19T22:04:28.05 to 2026-11-19T22:19:38.297, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v19-pq-heavy-10m on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 22,208 MB vs 615 MB (+21,593 MB), Power Query 22,088 MB vs 335 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (724%); F16 5,120 MB: OVER (434%); F32 10,240 MB: OVER (217%); F64 25,600 MB: fits (87%); PPU 102,400 MB: fits (22%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
The M evaluation exceeded the memory limit. To address the issue consider optimizing the M expressions, reducing the concurrency of operations that are memory intensive or upgrading to increase the available memory. Container exited unexpectedly with code 0x0000DEAD. PID: 23360.
Used features: (none).;Container exited unexpectedly with code 0x0000DEAD. PID: 23360.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 23360.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 23360..
```

Steps running or failed when it stopped:

```
                                    Object           OperationDetailName                        Began Ended EndStatus
      5ac4ec23-e684-402f-a53d-9a6e18c4724f          TabularSequencePoint 2026-11-19T22:04:30.4606891Z  None          
           PQ Customer RFM.PQ Customer RFM                TabularRefresh 2026-11-19T22:04:30.5542306Z  None          
           PQ Customer RFM.PQ Customer RFM                    ExecuteSql 2026-11-19T22:04:30.6932164Z  None          
Model.7af29c93-a4a1-4082-83d2-9f57ab371736      RelationshipBuildPrepare 2026-11-19T22:05:55.9684579Z  None          
Model.6029b9f6-210b-42fb-a96a-2a8bc3fd4d4b      RelationshipBuildPrepare 2026-11-19T22:05:56.0179378Z  None          
Model.6b5e0dab-b62f-4ded-8a7b-f2e12bd9c6b5      RelationshipBuildPrepare  2026-11-19T22:05:56.035746Z  None          
Model.0b5f92d3-53dd-41de-9f8f-6776ebfdcb67      RelationshipBuildPrepare 2026-11-19T22:05:56.0808382Z  None          
Model.f92796a2-a826-4e07-899a-ff3c6eceb911      RelationshipBuildPrepare 2026-11-19T22:05:56.0930735Z  None          
Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f      RelationshipBuildPrepare 2026-11-19T22:05:56.1053701Z  None          
                                                                Rollback 2026-11-19T22:19:38.1550014Z  None          
                                                                  Commit   2026-11-19T22:19:38.55778Z  None          
      5ac4ec23-e684-402f-a53d-9a6e18c4724f                 TabularCommit 2026-11-19T22:19:38.5582277Z  None          
      5ac4ec23-e684-402f-a53d-9a6e18c4724f MetadataTraversalDuringBackup 2026-11-19T22:19:38.8014105Z  None          
      5ac4ec23-e684-402f-a53d-9a6e18c4724f                        Backup 2026-11-19T22:19:38.8097555Z  None          
```

Slowest steps:

```
                                          Object OperationDetailName  DurationSec  CpuSec    Rows
                 PQ Basket Pairs.PQ Basket Pairs      TabularRefresh        770.9     0.1       0
                 PQ Basket Pairs.PQ Basket Pairs          ExecuteSql        770.8     0.0       0
               PQ Delivery Days.PQ Delivery Days      TabularRefresh        752.9     0.1       0
               PQ Delivery Days.PQ Delivery Days          ExecuteSql        752.7     0.0       0
       PQ Customer Segments.PQ Customer Segments          ExecuteSql        374.4     0.0       0
       PQ Customer Segments.PQ Customer Segments      TabularRefresh        374.4     0.1       0
 PQ Top Products by Year.PQ Top Products by Year      TabularRefresh        135.8     0.0       0
 PQ Top Products by Year.PQ Top Products by Year          ExecuteSql        135.7     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      TabularRefresh         82.9    20.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             Process         80.5    20.1       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba            ReadData         80.1    20.0 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba   AnalyzeEncodeData         12.1    13.2       0
```

**Screenshot: the refresh error of v19-pq-heavy-10m on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v19-pq-heavy-10m-m-evaluation-memory.png**

## Log

```
2026-11-19T22:04:04Z run 20261119T220331Z-v19-061e: variant=v19-pq-heavy-10m data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T22:04:13Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:04:14Z F64: v19-pq-heavy-10m is 5ac4ec23-e684-402f-a53d-9a6e18c4724f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:04:27Z F64: model size in memory before the refresh: 0.1 MB
2026-11-19T22:04:28Z F64: refresh started, request 3875fb2f-749c-496d-b25e-6e2d15cdbc97
2026-11-19T22:19:40Z F64: refresh failed (Failed) M evaluation memory limit
2026-11-19T22:19:40Z F64: monitoring database Monitoring KQL database
2026-11-19T22:21:16Z F64: ExecutionMetrics event found
```
