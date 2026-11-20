# Harness run 20261120T012738Z-v99b-f55a

- Task: refresh
- Variant: v99b-one-sales-copy
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: d0a08fe6-8751-4dbd-bbd7-dd9dc6a54da8
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 26,194 MB, Power Query 26,033 MB, duration 16 min, CPU 3,214 s, rows 28,053,515, model 517 MB (Backup step in XMLA trace)
- Refresh request 2603a6a5-800c-48d0-8019-9f973dfc50ea, 2026-11-20T01:28:49.86 to 2026-11-20T01:44:43.83, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99b-one-sales-copy on PPU data-1m-v1: refreshed, peak 25,684 MB (2026-11-17T18:13:07Z).
  - Peak change: +510 MB (+2.0%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 26,194 MB vs 551 MB (+25,643 MB), Power Query 26,033 MB vs 298 MB, model 517 MB vs 73 MB.
- Model size in memory when the full refresh started: 522 MB. The refresh may use the SKU maximum minus this: 101,878 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,544 MB: OVER (1029%); F16 4,598 MB: OVER (570%); F32 9,718 MB: OVER (270%); F64 25,078 MB: OVER (104%); PPU 101,878 MB: fits (26%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            03d0c1da-34b0-4aba-85d6-ed2d23257e66 TabularSequencePoint        940.4     0.4       0
                           Sales Flat.Sales Flat       TabularRefresh        898.8    72.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        893.5    24.4       0
                           Sales Flat.Sales Flat           ExecuteSql        656.2     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        489.0     2.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        447.0    24.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        446.7    24.3 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        446.4     0.0       0
                   Customer Stats.Customer Stats           ExecuteSql        301.7     0.0       0
                           Sales Flat.Sales Flat              Process        242.5    72.0       0
                           Sales Flat.Sales Flat             ReadData        242.0    71.9 2349091
                   Customer Stats.Customer Stats              Process        187.2     2.3       0
```

## Log

```
2026-11-20T01:28:11Z run 20261120T012738Z-v99b-f55a: variant=v99b-one-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T01:28:21Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T01:28:30Z PPU: v99b-one-sales-copy is 03d0c1da-34b0-4aba-85d6-ed2d23257e66, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T01:28:46Z PPU: model size in memory before the refresh: 521.5 MB
2026-11-20T01:28:49Z PPU: trace started (full)
2026-11-20T01:28:50Z PPU: refresh started, request 2603a6a5-800c-48d0-8019-9f973dfc50ea
2026-11-20T01:45:02Z PPU: refresh refreshed (Completed) 
2026-11-20T01:45:33Z PPU: trace captured 660 events: ProgressReportEnd 615, ExecutionMetrics 34, CommandEnd 11
2026-11-20T01:45:35Z PPU: model size in memory right after the refresh: 640.6 MB
```
