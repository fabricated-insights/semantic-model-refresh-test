# Harness run 20261120T071150Z-v26-061e

- Task: refresh
- Variant: v26-bad-dax
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 609ae2b5-3cab-4fc1-bc8d-1c9ff1405d6d
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 645 MB, Power Query 470 MB, duration 1 min, CPU 58 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 0c6875e3-606d-494f-9d63-0482a189cb31, 2026-11-20T07:14:35.433 to 2026-11-20T07:15:19.287, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v26-bad-dax on F64 data-1m-v1: refreshed, peak 1,016 MB (2026-11-19T23:18:07Z).
  - Peak change: -371 MB (-36.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 645 MB vs 716 MB (-71 MB), Power Query 470 MB vs 527 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (22%); F16 5,054 MB: fits (13%); F32 10,174 MB: fits (6%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  59ff6c07-aebe-46b6-b8b5-9ad2216819f2 TabularSequencePoint         38.3     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         37.8    11.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         36.4    11.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         36.2    11.2 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.1     4.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.0     4.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.7     1.0       0
                                                                     Commit          2.5     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.5     1.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.5     0.9  104990
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.3     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          1.1     0.0       0
```

## Log

```
2026-11-20T07:14:03Z run 20261120T071150Z-v26-061e: variant=v26-bad-dax data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T07:14:11Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:14:14Z F64: v26-bad-dax is 59ff6c07-aebe-46b6-b8b5-9ad2216819f2, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:14:35Z F64: model size in memory before the refresh: 66.2 MB
2026-11-20T07:14:35Z F64: refresh started, request 0c6875e3-606d-494f-9d63-0482a189cb31
2026-11-20T07:15:21Z F64: refresh refreshed (Completed) 
2026-11-20T07:15:21Z F64: monitoring database Monitoring KQL database
2026-11-20T07:16:56Z F64: ExecutionMetrics event found
2026-11-20T07:16:58Z F64: model size in memory right after the refresh: 92.7 MB
```
