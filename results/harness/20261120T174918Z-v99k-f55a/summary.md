# Harness run 20261120T174918Z-v99k-f55a

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 9f5bdf64-7602-4e06-b3e4-384c25bcaa65
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 13,049 MB, Power Query 12,931 MB, duration 8 min, CPU 831 s, rows 22,085,043, model 185 MB (Backup step in XMLA trace)
- Refresh request d29eb4c1-1846-4fb0-b704-3307db440699, 2026-11-20T17:50:22.95 to 2026-11-20T17:59:03.86, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99k-no-buffers on PPU data-1m-v1: refreshed, peak 13,152 MB (2026-11-20T12:24:25Z).
  - Peak change: -103 MB (-0.8%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 13,049 MB vs 604 MB (+12,445 MB), Power Query 12,931 MB vs 529 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 102,202 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (455%); F16 4,922 MB: OVER (265%); F32 10,042 MB: OVER (130%); F64 25,402 MB: fits (51%); PPU 102,202 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  036d4881-e715-4a7c-9782-be79275ef5ac TabularSequencePoint        506.0     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        493.3    23.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        250.9    23.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        250.6    23.8 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        242.4     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        217.7     2.6       0
                         Customer Stats.Customer Stats           ExecuteSql        140.5     0.0       0
                         Customer Stats.Customer Stats              Process         77.1     2.5       0
                         Customer Stats.Customer Stats             ReadData         76.4     2.0  471482
                                                  <NA>               Commit         12.4     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.6     1.8       0
                                Sales.Sales Line Label       TabularRefresh          5.8     5.6       0
```

## Log

```
2026-11-20T17:49:51Z run 20261120T174918Z-v99k-f55a: variant=v99k-no-buffers data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T17:49:57Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T17:50:02Z PPU: v99k-no-buffers is 036d4881-e715-4a7c-9782-be79275ef5ac, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T17:50:19Z PPU: model size in memory before the refresh: 197.8 MB
2026-11-20T17:50:22Z PPU: trace started (full)
2026-11-20T17:50:23Z PPU: refresh started, request d29eb4c1-1846-4fb0-b704-3307db440699
2026-11-20T17:59:04Z PPU: refresh refreshed (Completed) 
2026-11-20T17:59:35Z PPU: trace captured 462 events: ProgressReportEnd 442, ExecutionMetrics 10, CommandEnd 10
2026-11-20T17:59:36Z PPU: model size in memory right after the refresh: 232.6 MB
```
