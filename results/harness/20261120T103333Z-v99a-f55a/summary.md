# Harness run 20261120T103333Z-v99a-f55a

- Task: refresh
- Variant: v99a-no-big-calc-tables
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 0cab9fbd-eabc-47ad-b152-a681de693de3
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 16,162 MB, Power Query 16,052 MB, duration 16 min, CPU 1,907 s, rows 22,085,043, model 185 MB (Backup step in XMLA trace)
- Refresh request 13cb2995-622f-45dd-8db7-a7b7be2ba234, 2026-11-20T10:35:13.863 to 2026-11-20T10:51:48.02, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99a-no-big-calc-tables on PPU data-1m-v1: refreshed, peak 16,117 MB (2026-11-20T01:26:48Z).
  - Peak change: +45 MB (+0.3%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 16,162 MB vs 666 MB (+15,496 MB), Power Query 16,052 MB vs 591 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 102,202 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (563%); F16 4,922 MB: OVER (328%); F32 10,042 MB: OVER (161%); F64 25,402 MB: fits (64%); PPU 102,202 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                              Object  OperationDetailName  DurationSec  CpuSec    Rows
                948a9aac-0241-4366-b5de-ce4224c7bc48 TabularSequencePoint        976.8     0.3       0
    Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        963.8    24.1       0
    Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        696.9     0.0       0
                       Customer Stats.Customer Stats       TabularRefresh        524.1     2.8       0
                       Customer Stats.Customer Stats           ExecuteSql        309.4     0.0       0
    Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        266.8    24.0       0
    Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        266.5    24.0 2349091
                       Customer Stats.Customer Stats              Process        214.5     2.6       0
                       Customer Stats.Customer Stats             ReadData        213.7     2.0  471482
                                                <NA>               Commit         12.9     0.0    <NA>
Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          8.0     0.2       0
Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          7.7     0.0       0
```

## Log

```
2026-11-20T10:34:43Z run 20261120T103333Z-v99a-f55a: variant=v99a-no-big-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T10:34:50Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T10:34:54Z PPU: v99a-no-big-calc-tables is 948a9aac-0241-4366-b5de-ce4224c7bc48, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T10:35:10Z PPU: model size in memory before the refresh: 197.8 MB
2026-11-20T10:35:13Z PPU: trace started (full)
2026-11-20T10:35:14Z PPU: refresh started, request 13cb2995-622f-45dd-8db7-a7b7be2ba234
2026-11-20T10:51:57Z PPU: refresh refreshed (Completed) 
2026-11-20T10:52:27Z PPU: trace captured 474 events: ProgressReportEnd 442, ExecutionMetrics 22, CommandEnd 10
2026-11-20T10:52:29Z PPU: model size in memory right after the refresh: 232.6 MB
```
