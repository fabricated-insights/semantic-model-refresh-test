# Harness run 20261119T224755Z-v23-f55a

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 9b9e7804-9616-4456-b8f3-d1e3c9c04720
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,406 MB, Power Query 884 MB, duration 1 min, CPU 166 s, rows 16,549,502, model 182 MB (Backup step in XMLA trace)
- Refresh request 60404b32-01c1-4138-b6d1-872964aeeafd, 2026-11-19T22:50:42.867 to 2026-11-19T22:52:23.627, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v23-dax-calc-tables on PPU data-1m-v1: refreshed, peak 1,405 MB (2026-11-16T23:06:24Z).
  - Peak change: +1 MB (+0.1%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 1,406 MB vs 551 MB (+855 MB), Power Query 884 MB vs 298 MB, model 182 MB vs 73 MB.
- Model size in memory when the full refresh started: 1,296 MB. The refresh may use the SKU maximum minus this: 101,104 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 1,770 MB: fits (79%); F16 3,824 MB: fits (37%); F32 8,944 MB: fits (16%); F64 24,304 MB: fits (6%); PPU 101,104 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            316478cf-dbf2-484e-9234-3f1cb86faffd TabularSequencePoint         81.7     0.4       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         64.2    22.1       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         63.0    22.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         62.6    21.9 2349091
                           Sales Copy.Sales Copy       TabularRefresh         15.8    13.1       0
                                            <NA>               Commit         15.4     0.0    <NA>
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         14.2    14.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         14.0    12.9       0
             Product Date Grid.Product Date Grid             VertiPaq         11.7    11.7       0
                           Sales Copy.Sales Copy              Process         11.3    11.1       0
                           Sales Copy.Sales Copy             ReadData         11.0    10.9 2349091
             Product Date Grid.Product Date Grid       TabularRefresh          9.1     8.4       0
```

## Log

```
2026-11-19T22:49:58Z run 20261119T224755Z-v23-f55a: variant=v23-dax-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T22:50:04Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:50:24Z PPU: v23-dax-calc-tables is 316478cf-dbf2-484e-9234-3f1cb86faffd, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:50:39Z PPU: model size in memory before the refresh: 1295.8 MB
2026-11-19T22:50:42Z PPU: trace started (full)
2026-11-19T22:50:43Z PPU: refresh started, request 60404b32-01c1-4138-b6d1-872964aeeafd
2026-11-19T22:52:53Z PPU: refresh refreshed (Completed) 
2026-11-19T22:53:24Z PPU: trace captured 464 events: ProgressReportEnd 419, ExecutionMetrics 34, CommandEnd 11
2026-11-19T22:53:24Z PPU: model size in memory right after the refresh: 183.9 MB
```
