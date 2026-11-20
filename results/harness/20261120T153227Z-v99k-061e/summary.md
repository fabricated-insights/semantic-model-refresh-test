# Harness run 20261120T153227Z-v99k-061e

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 8037004c-6464-431a-bef1-cec700eeb619
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 13,141 MB, Power Query 13,036 MB, duration 14 min, CPU 1,453 s, rows 22,085,043, model 185 MB (Backup step in SemanticModelLogs)
- Refresh request 079c06ab-a44f-4057-9c08-d4de1612f58c, 2026-11-20T15:35:26.627 to 2026-11-20T15:49:40.27, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99k-no-buffers on F64 data-1m-v1: refreshed, peak 12,864 MB (2026-11-20T10:25:17Z).
  - Peak change: +277 MB (+2.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 13,141 MB vs 667 MB (+12,474 MB), Power Query 13,036 MB vs 592 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 25,402 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (458%); F16 4,922 MB: OVER (267%); F32 10,042 MB: OVER (131%); F64 25,402 MB: fits (52%); PPU 102,202 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  15619243-80f2-4103-abfe-ed7d0d628749 TabularSequencePoint        839.0     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        826.7    22.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        574.1    22.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        573.8    22.7 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        252.5     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        228.4     2.4       0
                         Customer Stats.Customer Stats           ExecuteSql        150.5     0.0       0
                         Customer Stats.Customer Stats              Process         77.8     2.3       0
                         Customer Stats.Customer Stats             ReadData         77.2     1.9  471482
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.9     9.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.6     6.5       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.5     1.6       0
```

## Log

```
2026-11-20T15:34:49Z run 20261120T153227Z-v99k-061e: variant=v99k-no-buffers data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T15:34:58Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T15:35:02Z F64: v99k-no-buffers is 15619243-80f2-4103-abfe-ed7d0d628749, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T15:35:26Z F64: model size in memory before the refresh: 197.8 MB
2026-11-20T15:35:26Z F64: refresh started, request 079c06ab-a44f-4057-9c08-d4de1612f58c
2026-11-20T15:50:09Z F64: refresh refreshed (Completed) 
2026-11-20T15:50:09Z F64: monitoring database Monitoring KQL database
2026-11-20T15:50:59Z F64: ExecutionMetrics event found
2026-11-20T15:51:34Z F64: model size in memory right after the refresh: 232.6 MB
```
