# Harness run 20261120T072420Z-v28-061e

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 44420cc3-0b75-4f7f-879a-ac8bbecc91a1
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 630 MB, Power Query 522 MB, duration 1 min, CPU 120 s, rows 2,561,140, model 69 MB (Backup step in SemanticModelLogs)
- Refresh request 80de20d6-75a8-4bf0-8ad0-65a7c71cf604, 2026-11-20T07:26:58.867 to 2026-11-20T07:28:06.453, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v28-types-all-text on F64 data-1m-v1: refreshed, peak 673 MB (2026-11-19T23:28:59Z).
  - Peak change: -43 MB (-6.4%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 630 MB vs 716 MB (-86 MB), Power Query 522 MB vs 527 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 96 MB. The refresh may use the SKU maximum minus this: 25,504 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,970 MB: fits (21%); F16 5,024 MB: fits (13%); F32 10,144 MB: fits (6%); F64 25,504 MB: fits (2%); PPU 102,304 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    bc793114-53e1-4476-8e50-c4b0c5b15603 TabularSequencePoint         60.3     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         56.9    32.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         54.1    32.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         51.4    32.1 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         12.9    12.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.8     1.8       0
                                                                                       Commit          4.8     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.7     0.7       0
                                                      Sales.Order Number       TabularRefresh          3.1     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          2.9     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.7     1.8       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.7     0.1       0
```

## Log

```
2026-11-20T07:26:24Z run 20261120T072420Z-v28-061e: variant=v28-types-all-text data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T07:26:34Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:26:38Z F64: v28-types-all-text is bc793114-53e1-4476-8e50-c4b0c5b15603, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:26:58Z F64: model size in memory before the refresh: 95.8 MB
2026-11-20T07:26:59Z F64: refresh started, request 80de20d6-75a8-4bf0-8ad0-65a7c71cf604
2026-11-20T07:28:09Z F64: refresh refreshed (Completed) 
2026-11-20T07:28:09Z F64: monitoring database Monitoring KQL database
2026-11-20T07:29:45Z F64: ExecutionMetrics event found
2026-11-20T07:29:47Z F64: model size in memory right after the refresh: 171.5 MB
```
