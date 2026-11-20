# Harness run 20261119T235304Z-v35-f55a

- Task: refresh
- Variant: v35-calc-tables-four-copies
- Data tag: data-10m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 72f6dcd2-bd00-4b51-9cb8-cf89edbf9d9b
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 13,316 MB, Power Query 1,562 MB, duration 17 min, CPU 1,870 s, rows 147,082,700, model 3,269 MB (Backup step in XMLA trace)
- Refresh request 75afefe1-d627-472c-bf3c-1ccb38095dc4, 2026-11-19T23:56:31.387 to 2026-11-20T00:15:22.397, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v35-calc-tables-four-copies on PPU data-10m-v1: refreshed, peak 9,737 MB (2026-11-17T10:04:44Z).
  - Peak change: +3,579 MB (+36.8%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-10m-v1 (2026-11-18T11:14:13Z): peak 13,316 MB vs 1,834 MB (+11,482 MB), Power Query 1,562 MB vs 1,713 MB, model 3,269 MB vs 778 MB.
- Model size in memory when the full refresh started: 2,748 MB. The refresh may use the SKU maximum minus this: 99,652 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 318 MB: OVER (4186%); F16 2,372 MB: OVER (561%); F32 7,492 MB: OVER (178%); F64 22,852 MB: fits (58%); PPU 99,652 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec     Rows
            90c2816c-fbb9-4514-ac64-d4da369fe384 TabularSequencePoint       1048.6     2.1        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        564.6   189.9        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        558.2   189.8        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        554.7   189.8 23719935
                           Sales Copy.Sales Copy       TabularRefresh        459.8   421.2        0
                           Sales Copy.Sales Copy              Process        403.3   398.0        0
                           Sales Copy.Sales Copy             ReadData        399.6   397.8 94879740
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData        172.6   186.8        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq        170.7   170.5        0
                     Sales Summary.Sales Summary       TabularRefresh         98.3    63.7        0
                                            <NA>               Commit         78.5     0.0     <NA>
                           Sales Copy.Sales Copy    AnalyzeEncodeData         68.5   127.6        0
```

## Log

```
2026-11-19T23:55:22Z run 20261119T235304Z-v35-f55a: variant=v35-calc-tables-four-copies data_tag=data-10m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T23:55:30Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:56:06Z PPU: v35-calc-tables-four-copies is 90c2816c-fbb9-4514-ac64-d4da369fe384, DataTag reads back data-10m-v1, SourceType parquet
2026-11-19T23:56:27Z PPU: model size in memory before the refresh: 2747.9 MB
2026-11-19T23:56:31Z PPU: trace started (full)
2026-11-19T23:56:31Z PPU: refresh started, request 75afefe1-d627-472c-bf3c-1ccb38095dc4
2026-11-20T00:15:44Z PPU: refresh refreshed (Completed) 
2026-11-20T00:16:16Z PPU: trace captured 2942 events: ProgressReportEnd 2897, ExecutionMetrics 34, CommandEnd 11
2026-11-20T00:16:17Z PPU: model size in memory right after the refresh: 2817.4 MB
```
