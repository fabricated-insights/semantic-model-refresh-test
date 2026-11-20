# Harness run 20261119T215931Z-v19-f55a

- Task: refresh
- Variant: v19-pq-heavy-10m
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 63548562-747f-48d4-b5a1-c578e0521758
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (M evaluation memory limit)
- Peak 21,276 MB, Power Query 21,155 MB, duration 17 min, CPU 4,018 s, rows 2,563,134, model 0 MB (Backup step in XMLA trace)
- Refresh request 5b0cc51c-e62d-4d5c-884a-975eb562112b, 2026-11-19T22:00:44.1 to 2026-11-19T22:17:50.003, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v19-pq-heavy-10m on PPU data-1m-v1: failed, peak 24,123 MB (2026-11-18T06:46:38Z).
  - Peak change: -2,847 MB (-11.8%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 21,276 MB vs 551 MB (+20,725 MB), Power Query 21,155 MB vs 298 MB, model 0 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (694%); F16 5,120 MB: OVER (416%); F32 10,240 MB: OVER (208%); F64 25,600 MB: fits (83%); PPU 102,400 MB: fits (21%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
The M evaluation exceeded the memory limit. To address the issue consider optimizing the M expressions, reducing the concurrency of operations that are memory intensive or upgrading to increase the available memory. Container exited unexpectedly with code 0x0000DEAD. PID: 19756.
Used features: (none).;Container exited unexpectedly with code 0x0000DEAD. PID: 19756.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 19756.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 19756..
```

Slowest steps:

```
                                          Object OperationDetailName  DurationSec  CpuSec    Rows
               PQ Delivery Days.PQ Delivery Days      TabularRefresh        896.4     0.1       0
               PQ Delivery Days.PQ Delivery Days          ExecuteSql        896.2     0.0       0
                 PQ Basket Pairs.PQ Basket Pairs      TabularRefresh        870.8     0.1       0
                 PQ Basket Pairs.PQ Basket Pairs          ExecuteSql        870.7     0.0       0
       PQ Customer Segments.PQ Customer Segments      TabularRefresh        452.9     0.1       0
       PQ Customer Segments.PQ Customer Segments          ExecuteSql        452.8     0.0       0
 PQ Top Products by Year.PQ Top Products by Year      TabularRefresh        154.5     0.1       0
 PQ Top Products by Year.PQ Top Products by Year          ExecuteSql        154.3     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      TabularRefresh         85.7    19.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             Process         85.1    19.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba            ReadData         84.6    19.7 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba   AnalyzeEncodeData         12.2    13.5       0
```

**Screenshot: the refresh error of v19-pq-heavy-10m on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v19-pq-heavy-10m-m-evaluation-memory.png**

## Log

```
2026-11-19T22:00:15Z run 20261119T215931Z-v19-f55a: variant=v19-pq-heavy-10m data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T22:00:21Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:00:24Z PPU: v19-pq-heavy-10m is 393784af-1418-40f1-a51d-7c01c12a2326, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:00:40Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-19T22:00:43Z PPU: trace started (full)
2026-11-19T22:00:44Z PPU: refresh started, request 5b0cc51c-e62d-4d5c-884a-975eb562112b
2026-11-19T22:17:57Z PPU: refresh failed (Failed) M evaluation memory limit
2026-11-19T22:18:27Z PPU: trace captured 360 events: ProgressReportEnd 306, ExecutionMetrics 38, CommandEnd 11, Error 5
```
