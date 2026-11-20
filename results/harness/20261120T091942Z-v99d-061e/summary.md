# Harness run 20261120T091942Z-v99d-061e

- Task: refresh
- Variant: v99d-power-query
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 8311f4ce-14f7-45ed-848c-638432276c89
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 16,075 MB, Power Query 15,967 MB, duration 17 min, CPU 1,816 s, rows 22,085,043, model 185 MB (Backup step in SemanticModelLogs)
- Refresh request bd93ebc5-ec04-4b9a-98fa-8a5a3eb9e8a7, 2026-11-20T09:22:43.77 to 2026-11-20T09:39:36.26, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99d-power-query on F64 data-1m-v1: refreshed, peak 16,031 MB (2026-11-20T01:40:27Z).
  - Peak change: +44 MB (+0.3%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 16,075 MB vs 716 MB (+15,359 MB), Power Query 15,967 MB vs 527 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 25,402 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (560%); F16 4,922 MB: OVER (327%); F32 10,042 MB: OVER (160%); F64 25,402 MB: fits (63%); PPU 102,202 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  0effade8-bfbb-4759-b64a-81c4f00d4b76 TabularSequencePoint        997.8     0.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        981.8    23.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        631.2    23.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        631.0    23.6 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        350.4     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        268.1     2.3       0
                         Customer Stats.Customer Stats           ExecuteSql        184.2     0.0       0
                         Customer Stats.Customer Stats              Process         83.7     2.2       0
                         Customer Stats.Customer Stats             ReadData         83.1     1.8  471482
                                Sales.Sales Line Label       TabularRefresh          8.0     7.6       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.3     2.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.2     7.0       0
```

## Log

```
2026-11-20T09:22:08Z run 20261120T091942Z-v99d-061e: variant=v99d-power-query data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T09:22:16Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T09:22:21Z F64: v99d-power-query is 0effade8-bfbb-4759-b64a-81c4f00d4b76, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:22:43Z F64: model size in memory before the refresh: 197.8 MB
2026-11-20T09:22:43Z F64: refresh started, request bd93ebc5-ec04-4b9a-98fa-8a5a3eb9e8a7
2026-11-20T09:39:57Z F64: refresh refreshed (Completed) 
2026-11-20T09:39:57Z F64: monitoring database Monitoring KQL database
2026-11-20T09:40:47Z F64: ExecutionMetrics event found
2026-11-20T09:40:50Z F64: model size in memory right after the refresh: 232.6 MB
```
