# Harness run 20261120T093824Z-v35-f55a

- Task: refresh
- Variant: v35-calc-tables-four-copies
- Data tag: data-10m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 695fc001-7d91-4fb1-926d-e44268a4284b
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 13,320 MB, Power Query 3,359 MB, duration 20 min, CPU 2,052 s, rows 147,082,700, model 3,286 MB (Backup step in XMLA trace)
- Refresh request d243eee4-7d9c-4814-ad1f-fd7c7c4e1a0b, 2026-11-20T09:42:06.783 to 2026-11-20T10:03:17.093, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v35-calc-tables-four-copies on PPU data-10m-v1: refreshed, peak 13,316 MB (2026-11-20T00:16:16Z).
  - Peak change: +4 MB (+0.0%).
- Against v00-baseline on PPU data-10m-v1 (2026-11-18T11:14:13Z): peak 13,320 MB vs 1,834 MB (+11,486 MB), Power Query 3,359 MB vs 1,713 MB, model 3,286 MB vs 778 MB.
- Model size in memory when the full refresh started: 2,734 MB. The refresh may use the SKU maximum minus this: 99,666 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 332 MB: OVER (4006%); F16 2,386 MB: OVER (558%); F32 7,506 MB: OVER (177%); F64 22,866 MB: fits (58%); PPU 99,666 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec     Rows
            90c2816c-fbb9-4514-ac64-d4da369fe384 TabularSequencePoint       1195.7     0.2        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        700.1   223.7        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        693.3   223.6        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        689.7   223.6 23719935
                           Sales Copy.Sales Copy       TabularRefresh        473.2   430.4        0
                           Sales Copy.Sales Copy              Process        413.8   405.2        0
                           Sales Copy.Sales Copy             ReadData        408.8   405.1 94879740
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData        162.4   173.3        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq        160.2   157.3        0
                     Sales Summary.Sales Summary       TabularRefresh        111.4    73.3        0
                                            <NA>               Commit         72.2     0.0     <NA>
                           Sales Copy.Sales Copy    AnalyzeEncodeData         67.2   128.0        0
```

## Log

```
2026-11-20T09:40:49Z run 20261120T093824Z-v35-f55a: variant=v35-calc-tables-four-copies data_tag=data-10m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T09:40:57Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T09:41:36Z PPU: v35-calc-tables-four-copies is 90c2816c-fbb9-4514-ac64-d4da369fe384, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T09:42:03Z PPU: model size in memory before the refresh: 2733.5 MB
2026-11-20T09:42:06Z PPU: trace started (full)
2026-11-20T09:42:06Z PPU: refresh started, request d243eee4-7d9c-4814-ad1f-fd7c7c4e1a0b
2026-11-20T10:03:21Z PPU: refresh refreshed (Completed) 
2026-11-20T10:03:53Z PPU: trace captured 2929 events: ProgressReportEnd 2896, ExecutionMetrics 23, CommandEnd 10
2026-11-20T10:03:54Z PPU: model size in memory right after the refresh: 2834.5 MB
```
