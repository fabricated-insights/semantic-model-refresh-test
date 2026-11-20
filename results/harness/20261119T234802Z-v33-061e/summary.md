# Harness run 20261119T234802Z-v33-061e

- Task: refresh
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a97a343a-de4d-404e-a549-63317d46c0ce
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 548 MB, Power Query 271 MB, duration 1 min, CPU 57 s, rows 2,791,244, model 74 MB (Backup step in SemanticModelLogs)
- Refresh request 63793fba-1f55-4f41-8de4-e6c70ae08bf3, 2026-11-19T23:51:00.39 to 2026-11-19T23:51:47.157, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v33-auto-date-time on F64 data-1m-v1: refreshed, peak 554 MB (2026-11-13T20:38:08Z).
  - Peak change: -6 MB (-1.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 548 MB vs 615 MB (-67 MB), Power Query 271 MB vs 335 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 25,530 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (18%); F16 5,050 MB: fits (11%); F32 10,170 MB: fits (5%); F64 25,530 MB: fits (2%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    79c2f30d-ee15-45f7-92a8-73654d03e1a1 TabularSequencePoint         42.1     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         41.6    10.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         33.8    10.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         33.6    10.6 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          7.8     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.2     6.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.1     5.1       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.9     0.8       0
                                                                                       Commit          2.8     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          2.5     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.0     0.3       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          1.5     0.0       0
```

## Log

```
2026-11-19T23:50:28Z run 20261119T234802Z-v33-061e: variant=v33-auto-date-time data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T23:50:36Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:50:39Z F64: v33-auto-date-time is 79c2f30d-ee15-45f7-92a8-73654d03e1a1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:51:00Z F64: model size in memory before the refresh: 69.7 MB
2026-11-19T23:51:00Z F64: refresh started, request 63793fba-1f55-4f41-8de4-e6c70ae08bf3
2026-11-19T23:52:11Z F64: refresh refreshed (Completed) 
2026-11-19T23:52:11Z F64: monitoring database Monitoring KQL database
2026-11-19T23:53:46Z F64: ExecutionMetrics event found
2026-11-19T23:53:48Z F64: model size in memory right after the refresh: 96.2 MB
```
