# Harness run 20261120T055709Z-v19-061e

- Task: refresh
- Variant: v19-pq-heavy-10m
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: aa113e64-703b-4c33-b98c-d925750cec11
- Refresh parallelism requested: 6

## F64

- Result: **failed** (M evaluation memory limit)
- Peak 23,336 MB, Power Query 23,219 MB, duration 18 min, CPU 4,250 s, rows 2,563,134, model n/a (no size)
- Refresh request 8a2d41e5-8375-4607-841a-91c53b455804, 2026-11-20T05:59:56.723 to 2026-11-20T06:18:02.883, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v19-pq-heavy-10m on F64 data-1m-v1: failed, peak 22,208 MB (2026-11-19T22:21:18Z).
  - Peak change: +1,128 MB (+5.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 23,336 MB vs 716 MB (+22,620 MB), Power Query 23,219 MB vs 527 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (761%); F16 5,120 MB: OVER (456%); F32 10,240 MB: OVER (228%); F64 25,600 MB: fits (91%); PPU 102,400 MB: fits (23%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
The M evaluation exceeded the memory limit. To address the issue consider optimizing the M expressions, reducing the concurrency of operations that are memory intensive or upgrading to increase the available memory. Container exited unexpectedly with code 0x0000DEAD. PID: 16112.
Used features: (none).;Container exited unexpectedly with code 0x0000DEAD. PID: 16112.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 16112.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 16112..
```

Steps running or failed when it stopped:

```
                                    Object      OperationDetailName                        Began Ended EndStatus
      5ac4ec23-e684-402f-a53d-9a6e18c4724f     TabularSequencePoint 2026-11-20T05:59:59.6901734Z  None          
         PQ Delivery Days.PQ Delivery Days           TabularRefresh 2026-11-20T05:59:59.7451231Z  None          
         PQ Delivery Days.PQ Delivery Days               ExecuteSql 2026-11-20T05:59:59.8702847Z  None          
           PQ Customer RFM.PQ Customer RFM           TabularRefresh 2026-11-20T06:00:07.5593193Z  None          
           PQ Customer RFM.PQ Customer RFM               ExecuteSql 2026-11-20T06:00:07.5783748Z  None          
Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare  2026-11-20T06:00:49.545324Z  None          
Model.0b5f92d3-53dd-41de-9f8f-6776ebfdcb67 RelationshipBuildPrepare 2026-11-20T06:00:49.7793315Z  None          
Model.f92796a2-a826-4e07-899a-ff3c6eceb911 RelationshipBuildPrepare 2026-11-20T06:00:49.7847823Z  None          
Model.7af29c93-a4a1-4082-83d2-9f57ab371736 RelationshipBuildPrepare 2026-11-20T06:00:49.8020641Z  None          
Model.6b5e0dab-b62f-4ded-8a7b-f2e12bd9c6b5 RelationshipBuildPrepare 2026-11-20T06:00:49.8200238Z  None          
Model.6029b9f6-210b-42fb-a96a-2a8bc3fd4d4b RelationshipBuildPrepare 2026-11-20T06:00:49.8329634Z  None          
```

Slowest steps:

```
                                          Object OperationDetailName  DurationSec  CpuSec    Rows
                 PQ Basket Pairs.PQ Basket Pairs      TabularRefresh       1046.2     0.0       0
                 PQ Basket Pairs.PQ Basket Pairs          ExecuteSql       1046.1     0.0       0
       PQ Customer Segments.PQ Customer Segments          ExecuteSql        721.3     0.0       0
       PQ Customer Segments.PQ Customer Segments      TabularRefresh        721.3     0.0       0
 PQ Top Products by Year.PQ Top Products by Year      TabularRefresh         81.2     0.0       0
 PQ Top Products by Year.PQ Top Products by Year          ExecuteSql         81.2     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      TabularRefresh         48.8    10.7       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             Process         47.5    10.7       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba            ReadData         47.3    10.6 2349091
  Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          7.8     0.1       0
  Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          7.6     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba   AnalyzeEncodeData          4.6     5.2       0
```

**Screenshot: the refresh error of v19-pq-heavy-10m on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v19-pq-heavy-10m-m-evaluation-memory.png**

## Log

```
2026-11-20T05:59:26Z run 20261120T055709Z-v19-061e: variant=v19-pq-heavy-10m data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T05:59:33Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T05:59:36Z F64: v19-pq-heavy-10m is 5ac4ec23-e684-402f-a53d-9a6e18c4724f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T05:59:56Z F64: model size in memory before the refresh: 0.1 MB
2026-11-20T05:59:56Z F64: refresh started, request 8a2d41e5-8375-4607-841a-91c53b455804
2026-11-20T06:18:10Z F64: refresh failed (Failed) M evaluation memory limit
2026-11-20T06:18:10Z F64: monitoring database Monitoring KQL database
2026-11-20T06:19:46Z F64: ExecutionMetrics event found
```
