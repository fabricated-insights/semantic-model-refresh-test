# Harness run 20261120T141829Z-v99a-061e

- Task: refresh
- Variant: v99a-no-big-calc-tables
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a151947c-4f79-4db9-a2a4-94c332e86ecb
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 16,034 MB, Power Query 15,957 MB, duration 5 min, CPU 450 s, rows 22,085,043, model 185 MB (Backup step in SemanticModelLogs)
- Refresh request 628c5de6-e499-4be5-82ed-f489277e3c76, 2026-11-20T14:21:18.567 to 2026-11-20T14:26:16.417, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99a-no-big-calc-tables on F64 data-1m-v1: refreshed, peak 16,022 MB (2026-11-20T09:03:25Z).
  - Peak change: +12 MB (+0.1%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 16,034 MB vs 667 MB (+15,367 MB), Power Query 15,957 MB vs 592 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 25,402 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (559%); F16 4,922 MB: OVER (326%); F32 10,042 MB: OVER (160%); F64 25,402 MB: fits (63%); PPU 102,202 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  96009ba6-0e71-4d15-b224-fac22fc40bc5 TabularSequencePoint        289.3     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        280.3    13.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        144.7    13.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        144.6    13.1 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        135.4     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        118.4     1.4       0
                         Customer Stats.Customer Stats           ExecuteSql         85.0     0.0       0
                         Customer Stats.Customer Stats              Process         33.2     1.4       0
                         Customer Stats.Customer Stats             ReadData         32.9     1.2  471482
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.7     1.0       0
                                Sales.Sales Line Label       TabularRefresh          3.3     3.2       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.8     1.0       0
```

## Log

```
2026-11-20T14:20:44Z run 20261120T141829Z-v99a-061e: variant=v99a-no-big-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T14:20:52Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:20:56Z F64: v99a-no-big-calc-tables is 96009ba6-0e71-4d15-b224-fac22fc40bc5, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:21:18Z F64: model size in memory before the refresh: 197.8 MB
2026-11-20T14:21:18Z F64: refresh started, request 628c5de6-e499-4be5-82ed-f489277e3c76
2026-11-20T14:26:29Z F64: refresh refreshed (Completed) 
2026-11-20T14:26:29Z F64: monitoring database Monitoring KQL database
2026-11-20T14:28:05Z F64: ExecutionMetrics event found
2026-11-20T14:28:24Z F64: model size in memory right after the refresh: 232.6 MB
```
