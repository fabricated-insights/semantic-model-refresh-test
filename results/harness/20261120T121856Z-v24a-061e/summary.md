# Harness run 20261120T121856Z-v24a-061e

- Task: refresh
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 053b5624-255f-401f-af4b-0f59245dbc83
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 726 MB, Power Query 521 MB, duration 1 min, CPU 69 s, rows 3,541,806, model 103 MB (Backup step in SemanticModelLogs)
- Refresh request 2d42b158-3a01-4e87-b5ae-79033f1a67e5, 2026-11-20T12:21:49.123 to 2026-11-20T12:22:30.82, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v24a-second-fact on F64 data-1m-v1: refreshed, peak 664 MB (2026-11-20T06:58:46Z).
  - Peak change: +62 MB (+9.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 726 MB vs 667 MB (+59 MB), Power Query 521 MB vs 592 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 82 MB. The refresh may use the SKU maximum minus this: 25,518 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,984 MB: fits (24%); F16 5,038 MB: fits (14%); F32 10,158 MB: fits (7%); F64 25,518 MB: fits (3%); PPU 102,318 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  bf8ceaed-631f-4d6e-8156-09b5c5ce253a TabularSequencePoint         36.3     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         36.0    10.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.5    10.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.3    10.8 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh          8.8     3.0       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process          7.8     2.9       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData          6.7     2.9  980666
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.9     5.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.8     4.8       0
                                                                     Commit          3.2     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.5     0.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.5     0.9       0
```

## Log

```
2026-11-20T12:21:12Z run 20261120T121856Z-v24a-061e: variant=v24a-second-fact data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T12:21:22Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:21:26Z F64: v24a-second-fact is bf8ceaed-631f-4d6e-8156-09b5c5ce253a, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:21:49Z F64: model size in memory before the refresh: 82.4 MB
2026-11-20T12:21:49Z F64: refresh started, request 2d42b158-3a01-4e87-b5ae-79033f1a67e5
2026-11-20T12:22:34Z F64: refresh refreshed (Completed) 
2026-11-20T12:22:34Z F64: monitoring database Monitoring KQL database
2026-11-20T12:25:12Z F64: ExecutionMetrics event found
2026-11-20T12:25:13Z F64: model size in memory right after the refresh: 110.0 MB
```
