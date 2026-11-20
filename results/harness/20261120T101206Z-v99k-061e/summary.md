# Harness run 20261120T101206Z-v99k-061e

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 031ca4a1-cfe5-4115-80d0-b6568c8ae9a6
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 12,864 MB, Power Query 12,742 MB, duration 8 min, CPU 829 s, rows 22,085,043, model 185 MB (Backup step in SemanticModelLogs)
- Refresh request 296778e1-cce6-445f-992e-3e6bc84d7183, 2026-11-20T10:14:58.663 to 2026-11-20T10:23:10.96, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99k-no-buffers on F64 data-1m-v1: refreshed, peak 13,034 MB (2026-11-20T04:33:52Z).
  - Peak change: -170 MB (-1.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 12,864 MB vs 716 MB (+12,148 MB), Power Query 12,742 MB vs 527 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 25,402 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (449%); F16 4,922 MB: OVER (261%); F32 10,042 MB: OVER (128%); F64 25,402 MB: fits (51%); PPU 102,202 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    15619243-80f2-4103-abfe-ed7d0d628749 TabularSequencePoint        477.7     0.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        465.4    23.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        236.2    23.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        236.0    23.5 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        228.8     0.0       0
                                           Customer Stats.Customer Stats       TabularRefresh        227.0     2.5       0
                                           Customer Stats.Customer Stats           ExecuteSql        175.4     0.0       0
                                           Customer Stats.Customer Stats              Process         51.2     2.4       0
                                           Customer Stats.Customer Stats             ReadData         50.6     2.0  471482
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          8.3     0.5       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          7.2     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.6     1.8       0
```

## Log

```
2026-11-20T10:14:21Z run 20261120T101206Z-v99k-061e: variant=v99k-no-buffers data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T10:14:30Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T10:14:36Z F64: v99k-no-buffers is 15619243-80f2-4103-abfe-ed7d0d628749, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T10:14:58Z F64: model size in memory before the refresh: 197.8 MB
2026-11-20T10:14:58Z F64: refresh started, request 296778e1-cce6-445f-992e-3e6bc84d7183
2026-11-20T10:23:40Z F64: refresh refreshed (Completed) 
2026-11-20T10:23:40Z F64: monitoring database Monitoring KQL database
2026-11-20T10:25:16Z F64: ExecutionMetrics event found
2026-11-20T10:25:19Z F64: model size in memory right after the refresh: 232.6 MB
```
