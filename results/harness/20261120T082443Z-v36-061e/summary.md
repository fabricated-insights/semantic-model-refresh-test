# Harness run 20261120T082443Z-v36-061e

- Task: refresh
- Variant: v36-calc-summary-month-grain
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1cfa6698-3c35-42b1-88cd-0d9582ff2a9b
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 14,682 MB, Power Query 1,333 MB, duration 7 min, CPU 808 s, rows 78,870,826, model 1,406 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 50a9e66e-e8a2-40f8-bbcd-5fa34197b90e, 2026-11-20T08:27:45.213 to 2026-11-20T08:35:30.48, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v36-calc-summary-month-grain on F64 data-10m-v1: refreshed, peak 14,684 MB (2026-11-20T00:25:33Z).
  - Peak change: -2 MB (-0.0%).
- Against v00-baseline on F64 data-10m-v1 (2026-11-13T08:43:01Z): peak 14,682 MB vs 1,650 MB (+13,032 MB), Power Query 1,333 MB vs 1,192 MB, model 1,406 MB vs 778 MB.
- Model size in memory when the full refresh started: 1,321 MB. The refresh may use the SKU maximum minus this: 24,279 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 1,745 MB: OVER (841%); F16 3,799 MB: OVER (386%); F32 8,919 MB: OVER (165%); F64 24,279 MB: fits (60%); PPU 101,079 MB: fits (15%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  9ab77bda-e29b-4924-9f6e-10b460e7f7c4 TabularSequencePoint        438.2     0.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        337.1   107.6        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        333.3   107.6        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        331.5   107.6 23719935
                                 Sales Copy.Sales Copy       TabularRefresh         92.3    70.5        0
                                 Sales Copy.Sales Copy              Process         63.5    56.6        0
                           Sales Summary.Sales Summary       TabularRefresh         61.3    40.6        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         59.8    68.3        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         58.7    58.6        0
                                 Sales Copy.Sales Copy             ReadData         56.6    56.6 23719935
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         25.0    12.9        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         23.2    12.9        0
```

## Log

```
2026-11-20T08:26:57Z run 20261120T082443Z-v36-061e: variant=v36-calc-summary-month-grain data_tag=data-10m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T08:27:10Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:27:25Z F64: v36-calc-summary-month-grain is 9ab77bda-e29b-4924-9f6e-10b460e7f7c4, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T08:27:45Z F64: model size in memory before the refresh: 1320.6 MB
2026-11-20T08:27:45Z F64: refresh started, request 50a9e66e-e8a2-40f8-bbcd-5fa34197b90e
2026-11-20T08:35:57Z F64: refresh refreshed (Completed) 
2026-11-20T08:35:57Z F64: monitoring database Monitoring KQL database
2026-11-20T08:36:46Z F64: ExecutionMetrics event found
2026-11-20T08:38:59Z F64: model size in memory right after the refresh: 1406.2 MB
```
