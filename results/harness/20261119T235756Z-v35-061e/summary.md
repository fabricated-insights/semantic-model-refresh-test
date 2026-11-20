# Harness run 20261119T235756Z-v35-061e

- Task: refresh
- Variant: v35-calc-tables-four-copies
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 7c886f24-3978-43fa-ba1b-37d553fe4265
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 13,064 MB, Power Query 1,708 MB, duration 10 min, CPU 1,078 s, rows 147,082,700, model 2,799 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request d7de1815-3c8b-4714-86d7-74a3e381570f, 2026-11-19T23:59:15.39 to 2026-11-20T00:10:29.93, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v35-calc-tables-four-copies on F64 data-10m-v1: refreshed, peak 13,063 MB (2026-11-13T12:49:17Z).
  - Peak change: +1 MB (+0.0%).
- Against v00-baseline on F64 data-10m-v1 (2026-11-13T08:43:01Z): peak 13,064 MB vs 1,650 MB (+11,414 MB), Power Query 1,708 MB vs 1,192 MB, model 2,799 MB vs 778 MB.
- Model size in memory when the full refresh started: 2,745 MB. The refresh may use the SKU maximum minus this: 22,855 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 321 MB: OVER (4072%); F16 2,375 MB: OVER (550%); F32 7,495 MB: OVER (174%); F64 22,855 MB: fits (57%); PPU 99,655 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec     Rows
            d4c8e929-5a3c-4171-a267-8dc68a857e76 TabularSequencePoint        626.1     0.9        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        354.1   110.8        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        348.2   110.7        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        346.1   110.7 23719935
                           Sales Copy.Sales Copy       TabularRefresh        258.5   237.0        0
                           Sales Copy.Sales Copy              Process        226.2   221.9        0
                           Sales Copy.Sales Copy             ReadData        222.2   221.8 94879740
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         68.4    77.0        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         67.3    67.1        0
                     Sales Summary.Sales Summary       TabularRefresh         58.4    39.1        0
                           Sales Copy.Sales Copy    AnalyzeEncodeData         43.9    85.2        0
                           Sales Copy.Sales Copy             VertiPaq         39.0    39.0        0
```

## Log

```
2026-11-19T23:58:28Z run 20261119T235756Z-v35-061e: variant=v35-calc-tables-four-copies data_tag=data-10m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T23:58:35Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:59:02Z F64: v35-calc-tables-four-copies is d4c8e929-5a3c-4171-a267-8dc68a857e76, DataTag reads back data-10m-v1, SourceType parquet
2026-11-19T23:59:15Z F64: model size in memory before the refresh: 2745.2 MB
2026-11-19T23:59:15Z F64: refresh started, request d7de1815-3c8b-4714-86d7-74a3e381570f
2026-11-20T00:10:57Z F64: refresh refreshed (Completed) 
2026-11-20T00:10:57Z F64: monitoring database Monitoring KQL database
2026-11-20T00:10:59Z F64: ExecutionMetrics event found
2026-11-20T00:13:11Z F64: model size in memory right after the refresh: 2798.8 MB
```
