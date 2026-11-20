# Harness run 20261120T163242Z-v99q-061e

- Task: refresh
- Variant: v99q-customer-stats
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 74deb4ea-d17c-4dbb-af10-4a83afee3d2a
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 3,550 MB, Power Query 3,316 MB, duration 1 min, CPU 201 s, rows 22,055,454, model 114 MB (Backup step in SemanticModelLogs)
- Refresh request 1752455b-0caf-4af3-b5a9-e31139c1fd45, 2026-11-20T16:35:40.257 to 2026-11-20T16:37:10.93, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99q-customer-stats on F64 data-1m-v1: refreshed, peak 3,572 MB (2026-11-20T11:20:06Z).
  - Peak change: -22 MB (-0.6%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 3,550 MB vs 667 MB (+2,883 MB), Power Query 3,316 MB vs 592 MB, model 114 MB vs 73 MB.
- Model size in memory when the full refresh started: 127 MB. The refresh may use the SKU maximum minus this: 25,473 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,939 MB: OVER (121%); F16 4,993 MB: fits (71%); F32 10,113 MB: fits (35%); F64 25,473 MB: fits (14%); PPU 102,273 MB: fits (3%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  d23d017e-5e59-44df-9370-2adb1e080a45 TabularSequencePoint         79.9     0.2       0
                         Customer Stats.Customer Stats       TabularRefresh         78.1     2.3       0
                         Customer Stats.Customer Stats           ExecuteSql         67.4     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         61.6    21.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         59.0    21.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         58.6    20.9 2349091
                         Customer Stats.Customer Stats              Process         10.5     2.3       0
                         Customer Stats.Customer Stats             ReadData         10.0     1.9  471482
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.6     9.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.4     7.3       0
                                Sales.Sales Line Label       TabularRefresh          5.9     5.6       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.2     1.7       0
```

## Log

```
2026-11-20T16:35:02Z run 20261120T163242Z-v99q-061e: variant=v99q-customer-stats data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T16:35:10Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T16:35:14Z F64: v99q-customer-stats is d23d017e-5e59-44df-9370-2adb1e080a45, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T16:35:40Z F64: model size in memory before the refresh: 127.3 MB
2026-11-20T16:35:40Z F64: refresh started, request 1752455b-0caf-4af3-b5a9-e31139c1fd45
2026-11-20T16:37:20Z F64: refresh refreshed (Completed) 
2026-11-20T16:37:21Z F64: monitoring database Monitoring KQL database
2026-11-20T16:39:57Z F64: ExecutionMetrics event found
2026-11-20T16:40:00Z F64: model size in memory right after the refresh: 162.1 MB
```
