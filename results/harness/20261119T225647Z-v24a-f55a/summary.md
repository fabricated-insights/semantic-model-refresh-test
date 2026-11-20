# Harness run 20261119T225647Z-v24a-f55a

- Task: refresh
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f0a07441-f670-402e-b3b5-3c00050c4f41
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 947 MB, Power Query 777 MB, duration 1 min, CPU 125 s, rows 3,541,806, model 103 MB (Backup step in XMLA trace)
- Refresh request 18faedfd-860a-45e8-8c84-adff6d3d90aa, 2026-11-19T22:57:49.6 to 2026-11-19T22:59:04.203, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v24a-second-fact on PPU data-1m-v1: refreshed, peak 857 MB (2026-11-17T06:06:34Z).
  - Peak change: +90 MB (+10.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 947 MB vs 551 MB (+396 MB), Power Query 777 MB vs 298 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 82 MB. The refresh may use the SKU maximum minus this: 102,318 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,984 MB: fits (32%); F16 5,038 MB: fits (19%); F32 10,158 MB: fits (9%); F64 25,518 MB: fits (4%); PPU 102,318 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  b0358b26-6f81-4c1b-a470-0f781c76b094 TabularSequencePoint         62.7     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         62.0    18.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         60.5    18.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         60.0    17.9 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh         17.0     6.2       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process         15.8     6.2       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData         12.9     6.1  980666
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         10.8     1.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.4    11.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.2    10.2       0
                                                  <NA>               Commit          7.7     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          7.6     0.0       0
```

## Log

```
2026-11-19T22:57:23Z run 20261119T225647Z-v24a-f55a: variant=v24a-second-fact data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T22:57:28Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:57:32Z PPU: v24a-second-fact is b0358b26-6f81-4c1b-a470-0f781c76b094, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:57:46Z PPU: model size in memory before the refresh: 82.4 MB
2026-11-19T22:57:49Z PPU: trace started (full)
2026-11-19T22:57:49Z PPU: refresh started, request 18faedfd-860a-45e8-8c84-adff6d3d90aa
2026-11-19T22:59:30Z PPU: refresh refreshed (Completed) 
2026-11-19T23:00:00Z PPU: trace captured 305 events: ProgressReportEnd 260, ExecutionMetrics 34, CommandEnd 11
2026-11-19T23:00:01Z PPU: model size in memory right after the refresh: 110.0 MB
```
