# Harness run 20261120T135627Z-v36-061e

- Task: refresh
- Variant: v36-calc-summary-month-grain
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 67e822d3-41ce-4f55-a21c-6616f332312b
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 14,683 MB, Power Query 1,827 MB, duration 8 min, CPU 839 s, rows 78,870,826, model 1,405 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request bbbc817d-e36b-4ab8-97b3-57cbd724ef7a, 2026-11-20T13:59:52.83 to 2026-11-20T14:08:01.163, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v36-calc-summary-month-grain on F64 data-10m-v1: refreshed, peak 14,682 MB (2026-11-20T08:38:56Z).
  - Peak change: +1 MB (+0.0%).
- Against v00-baseline on F64 data-10m-v1 (2026-11-13T08:43:01Z): peak 14,683 MB vs 1,650 MB (+13,033 MB), Power Query 1,827 MB vs 1,192 MB, model 1,405 MB vs 778 MB.
- Model size in memory when the full refresh started: 1,406 MB. The refresh may use the SKU maximum minus this: 24,194 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 1,660 MB: OVER (885%); F16 3,714 MB: OVER (395%); F32 8,834 MB: OVER (166%); F64 24,194 MB: fits (61%); PPU 100,994 MB: fits (15%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  9ab77bda-e29b-4924-9f6e-10b460e7f7c4 TabularSequencePoint        456.9     0.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        351.7   111.1        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        348.1   111.1        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        346.1   111.1 23719935
                                 Sales Copy.Sales Copy       TabularRefresh         95.8    72.2        0
                                 Sales Copy.Sales Copy              Process         65.8    58.0        0
                           Sales Summary.Sales Summary       TabularRefresh         64.2    43.0        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         63.1    71.7        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         61.9    61.6        0
                                 Sales Copy.Sales Copy             ReadData         58.3    58.0 23719935
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         26.0    13.6        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         24.3    13.6        0
```

## Log

```
2026-11-20T13:59:14Z run 20261120T135627Z-v36-061e: variant=v36-calc-summary-month-grain data_tag=data-10m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T13:59:25Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:59:27Z F64: v36-calc-summary-month-grain is 9ab77bda-e29b-4924-9f6e-10b460e7f7c4, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T13:59:52Z F64: model size in memory before the refresh: 1406.2 MB
2026-11-20T13:59:53Z F64: refresh started, request bbbc817d-e36b-4ab8-97b3-57cbd724ef7a
2026-11-20T14:08:04Z F64: refresh refreshed (Completed) 
2026-11-20T14:08:04Z F64: monitoring database Monitoring KQL database
2026-11-20T14:08:54Z F64: ExecutionMetrics event found
2026-11-20T14:11:06Z F64: model size in memory right after the refresh: 1404.6 MB
```
