# Harness run 20261120T024606Z-v99e-f55a

- Task: refresh
- Variant: v99e-sales-flat
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 41e26dfa-4d4f-419b-97a4-e784904e3abc
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 23,036 MB, Power Query 22,935 MB, duration 10 min, CPU 1,631 s, rows 24,459,705, model 323 MB (Backup step in XMLA trace)
- Refresh request a1f6a1be-502d-44af-971c-23af9fe86d5b, 2026-11-20T02:47:24.543 to 2026-11-20T02:57:27.69, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99e-sales-flat on PPU data-1m-v1: refreshed, peak 23,382 MB (2026-11-17T10:32:49Z).
  - Peak change: -346 MB (-1.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 23,036 MB vs 551 MB (+22,485 MB), Power Query 22,935 MB vs 298 MB, model 323 MB vs 73 MB.
- Model size in memory when the full refresh started: 357 MB. The refresh may use the SKU maximum minus this: 102,043 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,709 MB: OVER (850%); F16 4,763 MB: OVER (484%); F32 9,883 MB: OVER (233%); F64 25,243 MB: fits (91%); PPU 102,043 MB: fits (23%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            a580ec47-fa81-43a8-98d8-f79d00b354d1 TabularSequencePoint        581.7     0.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        566.8    23.8       0
                           Sales Flat.Sales Flat       TabularRefresh        486.1    73.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        304.6     0.0       0
                           Sales Flat.Sales Flat           ExecuteSql        290.7     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        273.7     2.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        262.1    23.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        261.8    23.8 2349091
                   Customer Stats.Customer Stats           ExecuteSql        219.9     0.0       0
                           Sales Flat.Sales Flat              Process        195.3    73.0       0
                           Sales Flat.Sales Flat             ReadData        194.8    73.0 2349091
                   Customer Stats.Customer Stats              Process         53.6     2.2       0
```

## Log

```
2026-11-20T02:46:48Z run 20261120T024606Z-v99e-f55a: variant=v99e-sales-flat data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T02:46:59Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T02:47:05Z PPU: v99e-sales-flat is a580ec47-fa81-43a8-98d8-f79d00b354d1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T02:47:20Z PPU: model size in memory before the refresh: 356.6 MB
2026-11-20T02:47:24Z PPU: trace started (full)
2026-11-20T02:47:24Z PPU: refresh started, request a1f6a1be-502d-44af-971c-23af9fe86d5b
2026-11-20T02:57:36Z PPU: refresh refreshed (Completed) 
2026-11-20T02:58:07Z PPU: trace captured 650 events: ProgressReportEnd 605, ExecutionMetrics 34, CommandEnd 11
2026-11-20T02:58:08Z PPU: model size in memory right after the refresh: 459.7 MB
```
