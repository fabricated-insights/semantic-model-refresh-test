# Harness run 20261120T124502Z-v27-061e

- Task: refresh
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: fa4418ba-c3f3-42be-a606-a8def2469b2e
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 726 MB, Power Query 500 MB, duration 1 min, CPU 106 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request de9b6a8e-f912-4237-8860-b93432515080, 2026-11-20T12:48:19.937 to 2026-11-20T12:49:29.89, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v27-high-cardinality-visuals on F64 data-1m-v1: refreshed, peak 550 MB (2026-11-20T07:23:30Z).
  - Peak change: +176 MB (+32.0%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 726 MB vs 667 MB (+59 MB), Power Query 500 MB vs 592 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (24%); F16 5,054 MB: fits (14%); F32 10,174 MB: fits (7%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    65980d29-ea56-4b4c-9a03-d5c7d50cb6db TabularSequencePoint         61.6     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         60.9    20.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         59.3    20.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         58.6    20.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.6    13.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.4    11.4       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.0     2.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     2.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.8     1.9  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.7     0.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.4     0.0       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          1.1     0.1       0
```

## Log

```
2026-11-20T12:47:43Z run 20261120T124502Z-v27-061e: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T12:47:51Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:47:54Z F64: v27-high-cardinality-visuals is 65980d29-ea56-4b4c-9a03-d5c7d50cb6db, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:48:19Z F64: model size in memory before the refresh: 66.2 MB
2026-11-20T12:48:20Z F64: refresh started, request de9b6a8e-f912-4237-8860-b93432515080
2026-11-20T12:49:30Z F64: refresh refreshed (Completed) 
2026-11-20T12:49:30Z F64: monitoring database Monitoring KQL database
2026-11-20T12:51:05Z F64: ExecutionMetrics event found
2026-11-20T12:51:40Z F64: model size in memory right after the refresh: 92.7 MB
```
