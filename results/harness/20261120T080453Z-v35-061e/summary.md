# Harness run 20261120T080453Z-v35-061e

- Task: refresh
- Variant: v35-calc-tables-four-copies
- Data tag: data-10m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ef5875e0-4d49-46bd-805a-71bf50a7d22d
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 13,063 MB, Power Query 1,239 MB, duration 10 min, CPU 1,057 s, rows 147,082,700, model 2,805 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request f0602c7a-bcbc-4dc9-a25c-2eaf5b582fca, 2026-11-20T08:08:56.877 to 2026-11-20T08:20:07.827, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v35-calc-tables-four-copies on F64 data-10m-v1: refreshed, peak 13,064 MB (2026-11-20T00:13:08Z).
  - Peak change: -1 MB (-0.0%).
- Against v00-baseline on F64 data-10m-v1 (2026-11-13T08:43:01Z): peak 13,063 MB vs 1,650 MB (+11,413 MB), Power Query 1,239 MB vs 1,192 MB, model 2,805 MB vs 778 MB.
- Model size in memory when the full refresh started: 2,715 MB. The refresh may use the SKU maximum minus this: 22,885 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 351 MB: OVER (3721%); F16 2,405 MB: OVER (543%); F32 7,525 MB: OVER (174%); F64 22,885 MB: fits (57%); PPU 99,685 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec     Rows
            d4c8e929-5a3c-4171-a267-8dc68a857e76 TabularSequencePoint        618.7     0.9        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        367.6   110.9        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        361.8   110.9        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        360.8   110.9 23719935
                           Sales Copy.Sales Copy       TabularRefresh        238.6   221.6        0
                           Sales Copy.Sales Copy              Process        211.8   208.3        0
                           Sales Copy.Sales Copy             ReadData        208.5   208.2 94879740
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         64.4    73.3        0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         63.3    63.2        0
                     Sales Summary.Sales Summary       TabularRefresh         49.0    32.5        0
                           Sales Copy.Sales Copy    AnalyzeEncodeData         43.2    84.3        0
                           Sales Copy.Sales Copy             VertiPaq         38.0    38.0        0
```

## Log

```
2026-11-20T08:07:52Z run 20261120T080453Z-v35-061e: variant=v35-calc-tables-four-copies data_tag=data-10m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T08:08:01Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:08:28Z F64: v35-calc-tables-four-copies is d4c8e929-5a3c-4171-a267-8dc68a857e76, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T08:08:56Z F64: model size in memory before the refresh: 2714.9 MB
2026-11-20T08:08:57Z F64: refresh started, request f0602c7a-bcbc-4dc9-a25c-2eaf5b582fca
2026-11-20T08:20:09Z F64: refresh refreshed (Completed) 
2026-11-20T08:20:09Z F64: monitoring database Monitoring KQL database
2026-11-20T08:21:45Z F64: ExecutionMetrics event found
2026-11-20T08:23:57Z F64: model size in memory right after the refresh: 2804.6 MB
```
