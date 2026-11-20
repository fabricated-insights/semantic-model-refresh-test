# Harness run 20261120T132436Z-v33-061e

- Task: refresh
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: b4a5daa4-0834-4eed-8f84-7d4815a59bb1
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 754 MB, Power Query 679 MB, duration 1 min, CPU 106 s, rows 2,791,244, model 74 MB (Backup step in SemanticModelLogs)
- Refresh request d5f83aff-1fc1-4af4-901c-c610fb149943, 2026-11-20T13:27:19.477 to 2026-11-20T13:28:30.473, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v33-auto-date-time on F64 data-1m-v1: refreshed, peak 613 MB (2026-11-20T07:57:30Z).
  - Peak change: +141 MB (+23.0%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 754 MB vs 667 MB (+87 MB), Power Query 679 MB vs 592 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 25,530 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (25%); F16 5,050 MB: fits (15%); F32 10,170 MB: fits (7%); F64 25,530 MB: fits (3%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    79c2f30d-ee15-45f7-92a8-73654d03e1a1 TabularSequencePoint         62.8     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         62.1    20.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         58.6    20.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         57.5    20.0 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.7    12.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.5    11.5       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh         10.4     0.6       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          9.4     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.9     2.0       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          4.7     0.1       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          4.4     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          3.6     0.0       0
```

## Log

```
2026-11-20T13:26:41Z run 20261120T132436Z-v33-061e: variant=v33-auto-date-time data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T13:26:49Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:26:53Z F64: v33-auto-date-time is 79c2f30d-ee15-45f7-92a8-73654d03e1a1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:27:19Z F64: model size in memory before the refresh: 69.7 MB
2026-11-20T13:27:19Z F64: refresh started, request d5f83aff-1fc1-4af4-901c-c610fb149943
2026-11-20T13:29:00Z F64: refresh refreshed (Completed) 
2026-11-20T13:29:00Z F64: monitoring database Monitoring KQL database
2026-11-20T13:30:36Z F64: ExecutionMetrics event found
2026-11-20T13:30:38Z F64: model size in memory right after the refresh: 96.2 MB
```
