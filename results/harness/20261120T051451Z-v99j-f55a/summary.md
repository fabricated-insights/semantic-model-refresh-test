# Harness run 20261120T051451Z-v99j-f55a

- Task: refresh
- Variant: v99j-buffer-stg-customer
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 035e2de0-5423-41d8-ad08-bf0802917326
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 23,111 MB, Power Query 22,975 MB, duration 17 min, CPU 2,850 s, rows 38,422,496, model 536 MB (Backup step in XMLA trace)
- Refresh request ff911c46-8c3f-450e-8ba7-14b38cfb0748, 2026-11-20T05:17:50.503 to 2026-11-20T05:34:54.22, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99j-buffer-stg-customer on PPU data-1m-v1: refreshed, peak 22,919 MB (2026-11-17T21:49:20Z).
  - Peak change: +192 MB (+0.8%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 23,111 MB vs 551 MB (+22,560 MB), Power Query 22,975 MB vs 298 MB, model 536 MB vs 73 MB.
- Model size in memory when the full refresh started: 541 MB. The refresh may use the SKU maximum minus this: 101,859 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,525 MB: OVER (915%); F16 4,579 MB: OVER (505%); F32 9,699 MB: OVER (238%); F64 25,059 MB: fits (92%); PPU 101,859 MB: fits (23%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            69bc2532-0803-4ff1-841a-d6893208f449 TabularSequencePoint       1007.9     0.9       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        916.7    25.0       0
                           Sales Flat.Sales Flat       TabularRefresh        741.8    81.1       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        471.5    24.9       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        471.3    24.9 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        445.0     0.0       0
                           Sales Flat.Sales Flat           ExecuteSql        442.4     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        406.8     2.4       0
                   Customer Stats.Customer Stats           ExecuteSql        317.5     0.0       0
                           Sales Flat.Sales Flat              Process        299.2    81.0       0
                           Sales Flat.Sales Flat             ReadData        298.3    80.9 2349091
                   Customer Stats.Customer Stats              Process         89.1     2.4       0
```

## Log

```
2026-11-20T05:17:05Z run 20261120T051451Z-v99j-f55a: variant=v99j-buffer-stg-customer data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T05:17:18Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T05:17:28Z PPU: v99j-buffer-stg-customer is 69bc2532-0803-4ff1-841a-d6893208f449, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T05:17:47Z PPU: model size in memory before the refresh: 540.6 MB
2026-11-20T05:17:50Z PPU: trace started (full)
2026-11-20T05:17:50Z PPU: refresh started, request ff911c46-8c3f-450e-8ba7-14b38cfb0748
2026-11-20T05:35:03Z PPU: refresh refreshed (Completed) 
2026-11-20T05:35:34Z PPU: trace captured 844 events: ProgressReportEnd 799, ExecutionMetrics 34, CommandEnd 11
2026-11-20T05:35:35Z PPU: model size in memory right after the refresh: 662.8 MB
```
