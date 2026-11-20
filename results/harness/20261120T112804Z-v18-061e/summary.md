# Harness run 20261120T112804Z-v18-061e

- Task: refresh
- Variant: v18-pq-10m-summary
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 37d72b1e-89ba-4816-8b7c-7ead5efadeb4
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,524 MB, Power Query 1,388 MB, duration 1 min, CPU 195 s, rows 2,561,730, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 2d5a4b4d-aaa7-433f-8a2f-64d319440a94, 2026-11-20T11:31:21.267 to 2026-11-20T11:32:52.923, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v18-pq-10m-summary on F64 data-1m-v1: refreshed, peak 1,796 MB (2026-11-20T05:56:15Z).
  - Peak change: -272 MB (-15.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 1,524 MB vs 667 MB (+857 MB), Power Query 1,388 MB vs 592 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (51%); F16 5,054 MB: fits (30%); F32 10,174 MB: fits (15%); F64 25,534 MB: fits (6%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  488c2f22-ab75-4ac9-87fa-79b129d25c49 TabularSequencePoint         84.9     0.1       0
                 Store Year Summary.Store Year Summary       TabularRefresh         84.7     0.1       0
                 Store Year Summary.Store Year Summary           ExecuteSql         84.5     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         65.9    20.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         63.1    20.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         61.5    20.7 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         13.1    14.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         12.9    12.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.5     1.6       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     1.6       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.9     1.5  104990
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          2.8     0.0       0
```

## Log

```
2026-11-20T11:30:44Z run 20261120T112804Z-v18-061e: variant=v18-pq-10m-summary data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T11:30:52Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:30:56Z F64: v18-pq-10m-summary is 488c2f22-ab75-4ac9-87fa-79b129d25c49, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:31:21Z F64: model size in memory before the refresh: 66.2 MB
2026-11-20T11:31:21Z F64: refresh started, request 2d5a4b4d-aaa7-433f-8a2f-64d319440a94
2026-11-20T11:33:02Z F64: refresh refreshed (Completed) 
2026-11-20T11:33:02Z F64: monitoring database Monitoring KQL database
2026-11-20T11:33:52Z F64: ExecutionMetrics event found
2026-11-20T11:33:54Z F64: model size in memory right after the refresh: 92.7 MB
```
