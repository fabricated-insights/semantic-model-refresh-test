# Harness run 20261120T152249Z-v35-f55a

- Task: refresh
- Variant: v35-calc-tables-four-copies
- Data tag: data-10m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1e6d13c7-9ffc-4332-83bf-64088eac6d1f
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 13,141 MB, Power Query 1,771 MB, duration 22 min, CPU 2,122 s, rows 147,082,700, model 3,267 MB (Backup step in XMLA trace)
- Refresh request ef2a95a8-766f-4012-acdd-6c9df2cc25fd, 2026-11-20T15:26:11.177 to 2026-11-20T15:49:04.967, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v35-calc-tables-four-copies on PPU data-10m-v1: refreshed, peak 13,320 MB (2026-11-20T10:03:53Z).
  - Peak change: -179 MB (-1.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-10m-v1 (2026-11-18T11:14:13Z): peak 13,141 MB vs 1,834 MB (+11,307 MB), Power Query 1,771 MB vs 1,713 MB, model 3,267 MB vs 778 MB.
- Model size in memory when the full refresh started: 2,751 MB. The refresh may use the SKU maximum minus this: 99,649 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 315 MB: OVER (4166%); F16 2,369 MB: OVER (555%); F32 7,489 MB: OVER (175%); F64 22,849 MB: fits (58%); PPU 99,649 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec     Rows
            90c2816c-fbb9-4514-ac64-d4da369fe384 TabularSequencePoint       1291.1     2.6        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        689.0   217.9        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        670.1   217.8        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        665.6   217.8 23719935
                           Sales Copy.Sales Copy       TabularRefresh        574.9   510.3        0
                           Sales Copy.Sales Copy              Process        498.7   481.1        0
                           Sales Copy.Sales Copy             ReadData        487.2   481.0 94879740
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData        141.9   153.9        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq        139.9   139.3        0
                     Sales Summary.Sales Summary       TabularRefresh        133.2    83.4        0
                           Sales Copy.Sales Copy    AnalyzeEncodeData         77.9   135.4        0
                                            <NA>               Commit         73.7     0.0     <NA>
```

## Log

```
2026-11-20T15:25:03Z run 20261120T152249Z-v35-f55a: variant=v35-calc-tables-four-copies data_tag=data-10m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T15:25:08Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T15:25:42Z PPU: v35-calc-tables-four-copies is 90c2816c-fbb9-4514-ac64-d4da369fe384, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T15:26:05Z PPU: model size in memory before the refresh: 2750.6 MB
2026-11-20T15:26:11Z PPU: trace started (full)
2026-11-20T15:26:12Z PPU: refresh started, request ef2a95a8-766f-4012-acdd-6c9df2cc25fd
2026-11-20T15:49:26Z PPU: refresh refreshed (Completed) 
2026-11-20T15:49:58Z PPU: trace captured 2917 events: ProgressReportEnd 2896, ExecutionMetrics 11, CommandEnd 10
2026-11-20T15:49:59Z PPU: model size in memory right after the refresh: 2816.1 MB
```
