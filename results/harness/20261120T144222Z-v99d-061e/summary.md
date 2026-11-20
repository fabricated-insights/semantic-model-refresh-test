# Harness run 20261120T144222Z-v99d-061e

- Task: refresh
- Variant: v99d-power-query
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: b56d6031-dda8-4262-a501-add6704a35b8
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 16,076 MB, Power Query 15,953 MB, duration 9 min, CPU 892 s, rows 22,085,043, model 185 MB (Backup step in SemanticModelLogs)
- Refresh request 5e1f36e4-a3d3-43bd-9a92-407094d34fff, 2026-11-20T14:43:22.59 to 2026-11-20T14:52:32.877, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99d-power-query on F64 data-1m-v1: refreshed, peak 16,075 MB (2026-11-20T09:40:48Z).
  - Peak change: +1 MB (+0.0%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 16,076 MB vs 667 MB (+15,409 MB), Power Query 15,953 MB vs 592 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 25,402 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (560%); F16 4,922 MB: OVER (327%); F32 10,042 MB: OVER (160%); F64 25,402 MB: fits (63%); PPU 102,202 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  0effade8-bfbb-4759-b64a-81c4f00d4b76 TabularSequencePoint        541.2     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        529.8    14.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        368.5    14.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        368.4    14.3 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        161.1     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        151.0     1.5       0
                         Customer Stats.Customer Stats           ExecuteSql        100.7     0.0       0
                         Customer Stats.Customer Stats              Process         50.2     1.4       0
                         Customer Stats.Customer Stats             ReadData         49.8     1.2  471482
                                Sales.Sales Line Label       TabularRefresh          3.3     3.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          3.1     4.4       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.1     1.1       0
```

## Log

```
2026-11-20T14:42:56Z run 20261120T144222Z-v99d-061e: variant=v99d-power-query data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T14:43:03Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:43:07Z F64: v99d-power-query is 0effade8-bfbb-4759-b64a-81c4f00d4b76, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:43:22Z F64: model size in memory before the refresh: 197.8 MB
2026-11-20T14:43:22Z F64: refresh started, request 5e1f36e4-a3d3-43bd-9a92-407094d34fff
2026-11-20T14:52:34Z F64: refresh refreshed (Completed) 
2026-11-20T14:52:34Z F64: monitoring database Monitoring KQL database
2026-11-20T14:54:10Z F64: ExecutionMetrics event found
2026-11-20T14:54:13Z F64: model size in memory right after the refresh: 232.6 MB
```
