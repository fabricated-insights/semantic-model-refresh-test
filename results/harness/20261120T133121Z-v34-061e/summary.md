# Harness run 20261120T133121Z-v34-061e

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6da1365a-1789-4021-b5aa-260384be39c2
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 685 MB, Power Query 601 MB, duration 1 min, CPU 56 s, rows 2,847,496, model 74 MB (Backup step in SemanticModelLogs)
- Refresh request 97d239ec-ce52-4e2e-a12a-aa24a26fda9f, 2026-11-20T13:34:50.793 to 2026-11-20T13:35:30.687, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v34-auto-date-time-no-date-table on F64 data-1m-v1: refreshed, peak 556 MB (2026-11-20T08:04:25Z).
  - Peak change: +129 MB (+23.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 685 MB vs 667 MB (+18 MB), Power Query 601 MB vs 592 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 25,530 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (23%); F16 5,050 MB: fits (14%); F32 10,170 MB: fits (7%); F64 25,530 MB: fits (3%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    8876d3c4-cd50-45e6-b465-6758c70c6ca0 TabularSequencePoint         35.0     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         34.6    10.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         33.8    10.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         33.6    10.6 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.6     5.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.5     4.5       0
                                                                                       Commit          2.7     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.0     0.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     0.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.3     0.8  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.0     0.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          0.7     0.0       0
```

## Log

```
2026-11-20T13:34:14Z run 20261120T133121Z-v34-061e: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T13:34:23Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:34:26Z F64: v34-auto-date-time-no-date-table is 8876d3c4-cd50-45e6-b465-6758c70c6ca0, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:34:50Z F64: model size in memory before the refresh: 70.3 MB
2026-11-20T13:34:50Z F64: refresh started, request 97d239ec-ce52-4e2e-a12a-aa24a26fda9f
2026-11-20T13:35:36Z F64: refresh refreshed (Completed) 
2026-11-20T13:35:36Z F64: monitoring database Monitoring KQL database
2026-11-20T13:38:12Z F64: ExecutionMetrics event found
2026-11-20T13:38:14Z F64: model size in memory right after the refresh: 96.9 MB
```
