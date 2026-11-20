# Harness run 20261119T232331Z-v28-061e

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1703377c-dc24-41b2-8042-c083e71ba0f1
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 673 MB, Power Query 398 MB, duration 1 min, CPU 59 s, rows 2,561,140, model 69 MB (Backup step in SemanticModelLogs)
- Refresh request 91c63ba7-91ce-430f-a36d-a890c36a104d, 2026-11-19T23:26:37.657 to 2026-11-19T23:27:15.1, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v28-types-all-text on F64 data-1m-v1: refreshed, peak 777 MB (2026-11-11T20:45:58Z).
  - Peak change: -104 MB (-13.4%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 673 MB vs 615 MB (+58 MB), Power Query 398 MB vs 335 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 96 MB. The refresh may use the SKU maximum minus this: 25,504 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,970 MB: fits (23%); F16 5,024 MB: fits (13%); F32 10,144 MB: fits (7%); F64 25,504 MB: fits (3%); PPU 102,304 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    bc793114-53e1-4476-8e50-c4b0c5b15603 TabularSequencePoint         31.2     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         29.3    16.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         28.1    16.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         27.9    16.3 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.3     4.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.7     1.0       0
                                                                                       Commit          2.6     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.7     0.4       0
                                                      Sales.Order Number       TabularRefresh          1.7     0.0       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          1.6     0.1       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          1.5     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.4     1.0  104990
```

## Log

```
2026-11-19T23:26:05Z run 20261119T232331Z-v28-061e: variant=v28-types-all-text data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T23:26:13Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:26:16Z F64: v28-types-all-text is bc793114-53e1-4476-8e50-c4b0c5b15603, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:26:37Z F64: model size in memory before the refresh: 95.8 MB
2026-11-19T23:26:37Z F64: refresh started, request 91c63ba7-91ce-430f-a36d-a890c36a104d
2026-11-19T23:27:23Z F64: refresh refreshed (Completed) 
2026-11-19T23:27:23Z F64: monitoring database Monitoring KQL database
2026-11-19T23:28:58Z F64: ExecutionMetrics event found
2026-11-19T23:29:00Z F64: model size in memory right after the refresh: 171.5 MB
```
