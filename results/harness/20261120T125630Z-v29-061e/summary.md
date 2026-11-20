# Harness run 20261120T125630Z-v29-061e

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 490b0a28-4994-4ba8-a776-0a132bbe2716
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 5,967 MB, Power Query 5,922 MB, duration 1 min, CPU 116 s, rows 2,561,140, model 69 MB (Backup step in SemanticModelLogs)
- Refresh request 8070509f-6e87-4c90-9ad4-47f9956c14d1, 2026-11-20T12:59:23.937 to 2026-11-20T13:00:31.627, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v29-keys-as-text on F64 data-1m-v1: refreshed, peak 665 MB (2026-11-20T07:37:17Z).
  - Peak change: +5,302 MB (+797.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 5,967 MB vs 667 MB (+5,300 MB), Power Query 5,922 MB vs 592 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 94 MB. The refresh may use the SKU maximum minus this: 25,506 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,972 MB: OVER (201%); F16 5,026 MB: OVER (119%); F32 10,146 MB: fits (59%); F64 25,506 MB: fits (23%); PPU 102,306 MB: fits (6%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    8a2beb05-98b9-4e44-92de-799777abce23 TabularSequencePoint         60.2     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         56.9    28.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         54.6    28.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         52.9    27.9 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.2    11.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.3     2.0       0
                                                                                       Commit          5.0     0.0       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          3.6     0.1       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          3.5     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.3     1.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.3     0.7       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          3.3     0.0       0
```

## Log

```
2026-11-20T12:58:47Z run 20261120T125630Z-v29-061e: variant=v29-keys-as-text data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T12:58:54Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:58:59Z F64: v29-keys-as-text is 8a2beb05-98b9-4e44-92de-799777abce23, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:59:23Z F64: model size in memory before the refresh: 93.8 MB
2026-11-20T12:59:24Z F64: refresh started, request 8070509f-6e87-4c90-9ad4-47f9956c14d1
2026-11-20T13:00:34Z F64: refresh refreshed (Completed) 
2026-11-20T13:00:34Z F64: monitoring database Monitoring KQL database
2026-11-20T13:02:10Z F64: ExecutionMetrics event found
2026-11-20T13:02:12Z F64: model size in memory right after the refresh: 141.9 MB
```
