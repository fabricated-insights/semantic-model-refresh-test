# Harness run 20261120T072147Z-v19-f55a

- Task: refresh
- Variant: v19-pq-heavy-10m
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 406a7da7-99dc-4711-89e0-6c3cacf19d3a
- Refresh parallelism requested: 6

## PPU

- Result: **failed** (M evaluation memory limit)
- Peak 23,900 MB, Power Query 23,779 MB, duration 26 min, CPU 6,145 s, rows 2,563,134, model n/a (no size)
- Refresh request 6117e6f5-75da-45e6-9804-ea80195aa3cd, 2026-11-20T07:24:31.093 to 2026-11-20T07:50:40.177, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v19-pq-heavy-10m on PPU data-1m-v1: failed, peak 21,276 MB (2026-11-19T22:18:27Z).
  - Peak change: +2,624 MB (+12.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 23,900 MB vs 666 MB (+23,234 MB), Power Query 23,779 MB vs 591 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 102,400 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (780%); F16 5,120 MB: OVER (467%); F32 10,240 MB: OVER (233%); F64 25,600 MB: fits (93%); PPU 102,400 MB: fits (23%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
The M evaluation exceeded the memory limit. To address the issue consider optimizing the M expressions, reducing the concurrency of operations that are memory intensive or upgrading to increase the available memory. Container exited unexpectedly with code 0x0000DEAD. PID: 13076.
Used features: (none).;Container exited unexpectedly with code 0x0000DEAD. PID: 13076.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 13076.
Used features: (none).
Container exited unexpectedly with code 0x0000DEAD. PID: 13076..
```

Slowest steps:

```
                                          Object OperationDetailName  DurationSec  CpuSec    Rows
               PQ Delivery Days.PQ Delivery Days      TabularRefresh       1378.8     0.1       0
               PQ Delivery Days.PQ Delivery Days          ExecuteSql       1378.7     0.0       0
                 PQ Basket Pairs.PQ Basket Pairs      TabularRefresh       1193.6     0.1       0
                 PQ Basket Pairs.PQ Basket Pairs          ExecuteSql       1193.5     0.0       0
       PQ Customer Segments.PQ Customer Segments      TabularRefresh        787.7     0.1       0
       PQ Customer Segments.PQ Customer Segments          ExecuteSql        787.5     0.0       0
 PQ Top Products by Year.PQ Top Products by Year      TabularRefresh        153.8     0.1       0
 PQ Top Products by Year.PQ Top Products by Year          ExecuteSql        153.7     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      TabularRefresh         92.6    24.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             Process         91.4    24.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba            ReadData         90.8    24.6 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba   AnalyzeEncodeData         12.7    13.9       0
```

**Screenshot: the refresh error of v19-pq-heavy-10m on PPU in the service (semantic model > Refresh history > error details), saved as docs/screenshots/ppu-v19-pq-heavy-10m-m-evaluation-memory.png**

## Log

```
2026-11-20T07:23:53Z run 20261120T072147Z-v19-f55a: variant=v19-pq-heavy-10m data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T07:24:03Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:24:06Z PPU: v19-pq-heavy-10m is 393784af-1418-40f1-a51d-7c01c12a2326, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:24:27Z PPU: model size in memory before the refresh: 0.1 MB
2026-11-20T07:24:31Z PPU: trace started (full)
2026-11-20T07:24:31Z PPU: refresh started, request 6117e6f5-75da-45e6-9804-ea80195aa3cd
2026-11-20T07:50:45Z PPU: refresh failed (Failed) M evaluation memory limit
2026-11-20T07:51:16Z PPU: trace captured 335 events: ProgressReportEnd 299, ExecutionMetrics 23, CommandEnd 8, Error 5
```
