# Harness run 20261120T081614Z-v23-f55a

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3708cc3e-5602-4ef7-b146-e4a504e48bbb
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,405 MB, Power Query 589 MB, duration 2 min, CPU 210 s, rows 16,549,502, model 182 MB (Backup step in XMLA trace)
- Refresh request 029deb29-1d70-4624-bb1e-3bbcd5268898, 2026-11-20T08:19:34.457 to 2026-11-20T08:21:50.163, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v23-dax-calc-tables on PPU data-1m-v1: refreshed, peak 1,406 MB (2026-11-19T22:53:24Z).
  - Peak change: -1 MB (-0.1%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 1,405 MB vs 666 MB (+739 MB), Power Query 589 MB vs 591 MB, model 182 MB vs 73 MB.
- Model size in memory when the full refresh started: 149 MB. The refresh may use the SKU maximum minus this: 102,251 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,917 MB: fits (48%); F16 4,971 MB: fits (28%); F32 10,091 MB: fits (14%); F64 25,451 MB: fits (6%); PPU 102,251 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            316478cf-dbf2-484e-9234-3f1cb86faffd TabularSequencePoint        110.6     0.4       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         87.3    27.7       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         84.6    27.6       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         83.7    27.5 2349091
                                            <NA>               Commit         21.5     0.0    <NA>
                           Sales Copy.Sales Copy       TabularRefresh         21.4    17.8       0
                           Sales Copy.Sales Copy              Process         15.3    15.0       0
                           Sales Copy.Sales Copy             ReadData         14.8    14.8 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         13.6    15.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         13.2    13.2       0
                     Sales Summary.Sales Summary       TabularRefresh         12.1     6.9       0
             Product Date Grid.Product Date Grid             VertiPaq         12.0    11.9       0
```

## Log

```
2026-11-20T08:18:52Z run 20261120T081614Z-v23-f55a: variant=v23-dax-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T08:18:59Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:19:04Z PPU: v23-dax-calc-tables is 316478cf-dbf2-484e-9234-3f1cb86faffd, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:19:30Z PPU: model size in memory before the refresh: 148.6 MB
2026-11-20T08:19:34Z PPU: trace started (full)
2026-11-20T08:19:34Z PPU: refresh started, request 029deb29-1d70-4624-bb1e-3bbcd5268898
2026-11-20T08:22:15Z PPU: refresh refreshed (Completed) 
2026-11-20T08:22:45Z PPU: trace captured 450 events: ProgressReportEnd 418, ExecutionMetrics 22, CommandEnd 10
2026-11-20T08:22:46Z PPU: model size in memory right after the refresh: 183.9 MB
```
