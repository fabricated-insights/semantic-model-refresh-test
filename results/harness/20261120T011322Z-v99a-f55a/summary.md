# Harness run 20261120T011322Z-v99a-f55a

- Task: refresh
- Variant: v99a-no-big-calc-tables
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 82a119da-1564-4611-a99d-b18233b336c9
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 16,117 MB, Power Query 16,008 MB, duration 11 min, CPU 1,142 s, rows 22,085,043, model 185 MB (Backup step in XMLA trace)
- Refresh request 94e36c0c-0a1d-43fd-907a-c13a37314c16, 2026-11-20T01:14:35.903 to 2026-11-20T01:25:50.787, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99a-no-big-calc-tables on PPU data-1m-v1: refreshed, peak 16,045 MB (2026-11-17T06:21:03Z).
  - Peak change: +72 MB (+0.4%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 16,117 MB vs 551 MB (+15,566 MB), Power Query 16,008 MB vs 298 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 102,202 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (562%); F16 4,922 MB: OVER (327%); F32 10,042 MB: OVER (160%); F64 25,402 MB: fits (63%); PPU 102,202 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  948a9aac-0241-4366-b5de-ce4224c7bc48 TabularSequencePoint        657.1     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        642.0    23.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        350.3    23.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        350.0    23.8 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        291.6     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        277.4     2.4       0
                         Customer Stats.Customer Stats           ExecuteSql        186.1     0.0       0
                         Customer Stats.Customer Stats              Process         91.3     2.3       0
                         Customer Stats.Customer Stats             ReadData         90.6     1.9  471482
                                                  <NA>               Commit         14.3     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.6     1.8       0
                                Sales.Sales Line Label       TabularRefresh          6.4     6.2       0
```

## Log

```
2026-11-20T01:14:00Z run 20261120T011322Z-v99a-f55a: variant=v99a-no-big-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T01:14:12Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T01:14:18Z PPU: v99a-no-big-calc-tables is 948a9aac-0241-4366-b5de-ce4224c7bc48, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T01:14:32Z PPU: model size in memory before the refresh: 197.8 MB
2026-11-20T01:14:35Z PPU: trace started (full)
2026-11-20T01:14:36Z PPU: refresh started, request 94e36c0c-0a1d-43fd-907a-c13a37314c16
2026-11-20T01:26:17Z PPU: refresh refreshed (Completed) 
2026-11-20T01:26:48Z PPU: trace captured 488 events: ProgressReportEnd 443, ExecutionMetrics 34, CommandEnd 11
2026-11-20T01:26:50Z PPU: model size in memory right after the refresh: 232.6 MB
```
