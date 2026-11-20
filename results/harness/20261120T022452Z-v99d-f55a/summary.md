# Harness run 20261120T022452Z-v99d-f55a

- Task: refresh
- Variant: v99d-power-query
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f4139ca4-b8e3-49d4-bdc5-04229b57ca78
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 16,024 MB, Power Query 15,901 MB, duration 16 min, CPU 1,841 s, rows 22,085,043, model 185 MB (Backup step in XMLA trace)
- Refresh request 3f1594b8-99c7-4d6c-a514-dd2929bc8620, 2026-11-20T02:28:17.693 to 2026-11-20T02:44:58.427, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99d-power-query on PPU data-1m-v1: refreshed, peak 16,132 MB (2026-11-17T09:14:37Z).
  - Peak change: -108 MB (-0.7%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 16,024 MB vs 551 MB (+15,473 MB), Power Query 15,901 MB vs 298 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 102,202 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (559%); F16 4,922 MB: OVER (326%); F32 10,042 MB: OVER (160%); F64 25,402 MB: fits (63%); PPU 102,202 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  2fb3d992-aae5-40d4-ac2d-710eb2f49931 TabularSequencePoint        985.0     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        972.4    23.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        642.5    23.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        642.3    23.2 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        329.8     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        303.0     2.5       0
                         Customer Stats.Customer Stats           ExecuteSql        192.6     0.0       0
                         Customer Stats.Customer Stats              Process        110.3     2.5       0
                         Customer Stats.Customer Stats             ReadData        109.7     2.0  471482
                                                  <NA>               Commit         10.9     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.9     2.1       0
                                Sales.Sales Line Label       TabularRefresh          5.7     5.5       0
```

## Log

```
2026-11-20T02:27:36Z run 20261120T022452Z-v99d-f55a: variant=v99d-power-query data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T02:27:47Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T02:27:51Z PPU: v99d-power-query is 2fb3d992-aae5-40d4-ac2d-710eb2f49931, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T02:28:13Z PPU: model size in memory before the refresh: 197.8 MB
2026-11-20T02:28:17Z PPU: trace started (full)
2026-11-20T02:28:17Z PPU: refresh started, request 3f1594b8-99c7-4d6c-a514-dd2929bc8620
2026-11-20T02:45:00Z PPU: refresh refreshed (Completed) 
2026-11-20T02:45:31Z PPU: trace captured 488 events: ProgressReportEnd 443, ExecutionMetrics 34, CommandEnd 11
2026-11-20T02:45:33Z PPU: model size in memory right after the refresh: 232.6 MB
```
