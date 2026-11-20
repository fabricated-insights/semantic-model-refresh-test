# Harness run 20261120T133841Z-v35-061e

- Task: refresh
- Variant: v35-calc-tables-four-copies
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6bd60cac-6ef1-4e23-b946-86ce5ef5e24a
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 13,141 MB, Power Query 1,606 MB, duration 10 min, CPU 1,032 s, rows 147,082,700, model 2,814 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request 71039805-6df5-4533-a9f8-8570323e0c29, 2026-11-20T13:41:28.12 to 2026-11-20T13:52:30.21, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v35-calc-tables-four-copies on F64 data-10m-v1: refreshed, peak 13,063 MB (2026-11-20T08:23:54Z).
  - Peak change: +78 MB (+0.6%).
- Against v00-baseline on F64 data-10m-v1 (2026-11-13T08:43:01Z): peak 13,141 MB vs 1,650 MB (+11,491 MB), Power Query 1,606 MB vs 1,192 MB, model 2,814 MB vs 778 MB.
- Model size in memory when the full refresh started: 2,805 MB. The refresh may use the SKU maximum minus this: 22,795 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 261 MB: OVER (5027%); F16 2,315 MB: OVER (568%); F32 7,435 MB: OVER (177%); F64 22,795 MB: fits (58%); PPU 99,595 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec     Rows
            d4c8e929-5a3c-4171-a267-8dc68a857e76 TabularSequencePoint        604.1     0.9        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        350.4   110.0        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        345.0   110.0        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        343.9   110.0 23719935
                           Sales Copy.Sales Copy       TabularRefresh        241.1   223.5        0
                           Sales Copy.Sales Copy              Process        214.5   210.4        0
                           Sales Copy.Sales Copy             ReadData        210.7   210.3 94879740
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         57.0    65.9        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         55.8    55.8        0
                     Sales Summary.Sales Summary       TabularRefresh         49.8    33.1        0
                           Sales Copy.Sales Copy    AnalyzeEncodeData         44.3    86.2        0
                           Sales Copy.Sales Copy             VertiPaq         39.4    39.3        0
```

## Log

```
2026-11-20T13:40:55Z run 20261120T133841Z-v35-061e: variant=v35-calc-tables-four-copies data_tag=data-10m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T13:41:04Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:41:06Z F64: v35-calc-tables-four-copies is d4c8e929-5a3c-4171-a267-8dc68a857e76, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T13:41:28Z F64: model size in memory before the refresh: 2804.6 MB
2026-11-20T13:41:28Z F64: refresh started, request 71039805-6df5-4533-a9f8-8570323e0c29
2026-11-20T13:52:40Z F64: refresh refreshed (Completed) 
2026-11-20T13:52:40Z F64: monitoring database Monitoring KQL database
2026-11-20T13:53:29Z F64: ExecutionMetrics event found
2026-11-20T13:55:41Z F64: model size in memory right after the refresh: 2814.2 MB
```
