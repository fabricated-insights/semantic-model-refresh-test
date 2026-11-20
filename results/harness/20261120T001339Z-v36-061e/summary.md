# Harness run 20261120T001339Z-v36-061e

- Task: refresh
- Variant: v36-calc-summary-month-grain
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: d288f5ce-caa0-43fe-b2b6-980e97545f78
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 14,684 MB, Power Query 1,995 MB, duration 7 min, CPU 809 s, rows 78,870,826, model 1,406 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request ba371712-0514-44a0-bee8-2ee59a397e53, 2026-11-20T00:14:55.487 to 2026-11-20T00:22:44.937, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v36-calc-summary-month-grain on F64 data-10m-v1: refreshed, peak 14,759 MB (2026-11-13T13:38:29Z).
  - Peak change: -75 MB (-0.5%).
- Against v00-baseline on F64 data-10m-v1 (2026-11-13T08:43:01Z): peak 14,684 MB vs 1,650 MB (+13,034 MB), Power Query 1,995 MB vs 1,192 MB, model 1,406 MB vs 778 MB.
- Model size in memory when the full refresh started: 1,322 MB. The refresh may use the SKU maximum minus this: 24,278 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 1,744 MB: OVER (842%); F16 3,798 MB: OVER (387%); F32 8,918 MB: OVER (165%); F64 24,278 MB: fits (60%); PPU 101,078 MB: fits (15%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  9ab77bda-e29b-4924-9f6e-10b460e7f7c4 TabularSequencePoint        442.0     0.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        343.7   110.2        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        340.0   110.2        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        338.8   110.2 23719935
                                 Sales Copy.Sales Copy       TabularRefresh         90.2    68.5        0
                                 Sales Copy.Sales Copy              Process         64.6    56.3        0
                           Sales Summary.Sales Summary       TabularRefresh         61.2    41.7        0
                                 Sales Copy.Sales Copy             ReadData         56.4    56.3 23719935
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         54.2    63.4        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         53.1    53.0        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         25.1    13.2        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         23.7    13.2        0
```

## Log

```
2026-11-20T00:14:15Z run 20261120T001339Z-v36-061e: variant=v36-calc-summary-month-grain data_tag=data-10m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T00:14:27Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T00:14:41Z F64: v36-calc-summary-month-grain is 9ab77bda-e29b-4924-9f6e-10b460e7f7c4, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T00:14:55Z F64: model size in memory before the refresh: 1321.9 MB
2026-11-20T00:14:55Z F64: refresh started, request ba371712-0514-44a0-bee8-2ee59a397e53
2026-11-20T00:23:07Z F64: refresh refreshed (Completed) 
2026-11-20T00:23:07Z F64: monitoring database Monitoring KQL database
2026-11-20T00:23:25Z F64: ExecutionMetrics event found
2026-11-20T00:25:35Z F64: model size in memory right after the refresh: 1405.5 MB
```
