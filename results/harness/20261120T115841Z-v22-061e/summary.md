# Harness run 20261120T115841Z-v22-061e

- Task: refresh
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: c3dd8f0a-4c3f-4d45-964b-5c7bdb6fca3d
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 685 MB, Power Query 404 MB, duration 1 min, CPU 122 s, rows 21,353,868, model 101 MB (Backup step in SemanticModelLogs)
- Refresh request 064efd31-bbbd-451e-b9b8-123f1aec6cfc, 2026-11-20T12:01:40.657 to 2026-11-20T12:03:00.96, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v22-dax-calc-columns on F64 data-1m-v1: refreshed, peak 755 MB (2026-11-20T06:39:36Z).
  - Peak change: -70 MB (-9.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 685 MB vs 667 MB (+18 MB), Power Query 404 MB vs 592 MB, model 101 MB vs 73 MB.
- Model size in memory when the full refresh started: 98 MB. The refresh may use the SKU maximum minus this: 25,502 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,968 MB: fits (23%); F16 5,022 MB: fits (14%); F32 10,142 MB: fits (7%); F64 25,502 MB: fits (3%); PPU 102,302 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  683e80a5-7d57-493c-a708-3a0b8ce5350c TabularSequencePoint         68.6     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         61.0    20.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         58.2    20.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         57.8    20.4 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.2    11.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.9     8.8       0
                                Sales.Sales Line Label       TabularRefresh          5.6     5.4       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.8     1.7       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.8     1.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.6     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.6     1.6  104990
                                   Sales.Customer Name       TabularRefresh          2.5     2.1       0
```

## Log

```
2026-11-20T12:01:05Z run 20261120T115841Z-v22-061e: variant=v22-dax-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T12:01:15Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:01:18Z F64: v22-dax-calc-columns is 683e80a5-7d57-493c-a708-3a0b8ce5350c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:01:40Z F64: model size in memory before the refresh: 97.8 MB
2026-11-20T12:01:40Z F64: refresh started, request 064efd31-bbbd-451e-b9b8-123f1aec6cfc
2026-11-20T12:03:21Z F64: refresh refreshed (Completed) 
2026-11-20T12:03:21Z F64: monitoring database Monitoring KQL database
2026-11-20T12:04:57Z F64: ExecutionMetrics event found
2026-11-20T12:04:59Z F64: model size in memory right after the refresh: 132.6 MB
```
