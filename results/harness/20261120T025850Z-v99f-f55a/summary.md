# Harness run 20261120T025850Z-v99f-f55a

- Task: refresh
- Variant: v99f-calc-tables
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: def93a56-c467-48ba-b4ea-1828b36db6f3
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 22,841 MB, Power Query 22,719 MB, duration 25 min, CPU 4,795 s, rows 36,073,405, model 361 MB (Backup step in XMLA trace)
- Refresh request c7f3f6cb-92e8-41be-860d-0b6c74aa4fe9, 2026-11-20T03:00:18.717 to 2026-11-20T03:25:19.193, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99f-calc-tables on PPU data-1m-v1: refreshed, peak 22,870 MB (2026-11-17T13:07:17Z).
  - Peak change: -29 MB (-0.1%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 22,841 MB vs 551 MB (+22,290 MB), Power Query 22,719 MB vs 298 MB, model 361 MB vs 73 MB.
- Model size in memory when the full refresh started: 386 MB. The refresh may use the SKU maximum minus this: 102,014 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,680 MB: OVER (852%); F16 4,734 MB: OVER (482%); F32 9,854 MB: OVER (232%); F64 25,214 MB: fits (91%); PPU 102,014 MB: fits (22%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            78a00a5c-5123-48ef-a449-f334f1e5852f TabularSequencePoint       1478.7     0.3       0
                           Sales Flat.Sales Flat       TabularRefresh       1355.1    63.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1249.7    22.1       0
                           Sales Flat.Sales Flat           ExecuteSql        883.1     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        632.7     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        616.9    22.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        616.6    22.0 2349091
                   Customer Stats.Customer Stats       TabularRefresh        506.5     2.8       0
                           Sales Flat.Sales Flat              Process        471.9    63.5       0
                           Sales Flat.Sales Flat             ReadData        471.3    63.4 2349091
                   Customer Stats.Customer Stats           ExecuteSql        266.5     0.0       0
                   Customer Stats.Customer Stats              Process        239.8     2.8       0
```

## Log

```
2026-11-20T02:59:42Z run 20261120T025850Z-v99f-f55a: variant=v99f-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T02:59:54Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T03:00:01Z PPU: v99f-calc-tables is 78a00a5c-5123-48ef-a449-f334f1e5852f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T03:00:15Z PPU: model size in memory before the refresh: 385.7 MB
2026-11-20T03:00:18Z PPU: trace started (full)
2026-11-20T03:00:18Z PPU: refresh started, request c7f3f6cb-92e8-41be-860d-0b6c74aa4fe9
2026-11-20T03:25:33Z PPU: refresh refreshed (Completed) 
2026-11-20T03:26:03Z PPU: trace captured 713 events: ProgressReportEnd 666, ExecutionMetrics 36, CommandEnd 11
2026-11-20T03:26:05Z PPU: model size in memory right after the refresh: 491.7 MB
```
