# Harness run 20261120T115529Z-v99k-f55a

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: aab5b80b-32ed-42fd-a7b6-23dcf497e9c3
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 13,152 MB, Power Query 13,054 MB, duration 27 min, CPU 2,928 s, rows 22,085,043, model 185 MB (Backup step in XMLA trace)
- Refresh request 4e5ae351-0ed2-4ac9-91e6-d87bff224af3, 2026-11-20T11:56:39.63 to 2026-11-20T12:23:31.847, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99k-no-buffers on PPU data-1m-v1: refreshed, peak 13,231 MB (2026-11-20T05:55:42Z).
  - Peak change: -79 MB (-0.6%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 13,152 MB vs 666 MB (+12,486 MB), Power Query 13,054 MB vs 591 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 102,202 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (459%); F16 4,922 MB: OVER (267%); F32 10,042 MB: OVER (131%); F64 25,402 MB: fits (52%); PPU 102,202 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            036d4881-e715-4a7c-9782-be79275ef5ac TabularSequencePoint       1596.0     0.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1585.7    30.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process       1176.2    30.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData       1175.9    30.3 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        409.4     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        351.4     2.9       0
                   Customer Stats.Customer Stats           ExecuteSql        205.0     0.0       0
                   Customer Stats.Customer Stats              Process        146.3     2.8       0
                   Customer Stats.Customer Stats             ReadData        145.6     2.4  471482
                                            <NA>               Commit         12.0     0.0    <NA>
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.3     8.7       0
                          Sales.Sales Line Label       TabularRefresh          6.1     5.8       0
```

## Log

```
2026-11-20T11:56:09Z run 20261120T115529Z-v99k-f55a: variant=v99k-no-buffers data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T11:56:16Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:56:20Z PPU: v99k-no-buffers is 036d4881-e715-4a7c-9782-be79275ef5ac, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:56:36Z PPU: model size in memory before the refresh: 197.8 MB
2026-11-20T11:56:39Z PPU: trace started (full)
2026-11-20T11:56:39Z PPU: refresh started, request 4e5ae351-0ed2-4ac9-91e6-d87bff224af3
2026-11-20T12:23:54Z PPU: refresh refreshed (Completed) 
2026-11-20T12:24:25Z PPU: trace captured 463 events: ProgressReportEnd 442, ExecutionMetrics 11, CommandEnd 10
2026-11-20T12:24:26Z PPU: model size in memory right after the refresh: 232.6 MB
```
