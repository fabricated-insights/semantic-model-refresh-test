# Harness run 20261120T073034Z-v29-061e

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a86d7954-5cd7-460c-9fa0-636b250e2ece
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 665 MB, Power Query 398 MB, duration 1 min, CPU 56 s, rows 2,561,140, model 69 MB (Backup step in SemanticModelLogs)
- Refresh request f1186b11-537b-4ce8-b632-f522f8410dda, 2026-11-20T07:33:53.36 to 2026-11-20T07:34:28.543, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v29-keys-as-text on F64 data-1m-v1: refreshed, peak 766 MB (2026-11-19T23:33:35Z).
  - Peak change: -101 MB (-13.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 665 MB vs 716 MB (-51 MB), Power Query 398 MB vs 527 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 94 MB. The refresh may use the SKU maximum minus this: 25,506 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,972 MB: fits (22%); F16 5,026 MB: fits (13%); F32 10,146 MB: fits (7%); F64 25,506 MB: fits (3%); PPU 102,306 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    8a2beb05-98b9-4e44-92de-799777abce23 TabularSequencePoint         31.5     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         29.6    13.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         28.5    13.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         28.3    13.4 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.7     4.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.2     1.0       0
                                                                                       Commit          2.2     0.0       0
                                                      Sales.Order Number       TabularRefresh          1.7     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     1.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.3     1.0  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.1     0.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.0     0.0       0
```

## Log

```
2026-11-20T07:33:14Z run 20261120T073034Z-v29-061e: variant=v29-keys-as-text data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T07:33:24Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:33:27Z F64: v29-keys-as-text is 8a2beb05-98b9-4e44-92de-799777abce23, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:33:53Z F64: model size in memory before the refresh: 93.8 MB
2026-11-20T07:33:53Z F64: refresh started, request f1186b11-537b-4ce8-b632-f522f8410dda
2026-11-20T07:34:38Z F64: refresh refreshed (Completed) 
2026-11-20T07:34:39Z F64: monitoring database Monitoring KQL database
2026-11-20T07:37:16Z F64: ExecutionMetrics event found
2026-11-20T07:37:18Z F64: model size in memory right after the refresh: 141.9 MB
```
