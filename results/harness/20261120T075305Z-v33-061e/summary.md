# Harness run 20261120T075305Z-v33-061e

- Task: refresh
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 593e2418-daa4-49a2-b9ab-ea0641088ace
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 613 MB, Power Query 455 MB, duration 1 min, CPU 129 s, rows 2,791,244, model 74 MB (Backup step in SemanticModelLogs)
- Refresh request 820390e3-8913-4775-8ad2-4000b3145cc5, 2026-11-20T07:54:09.443 to 2026-11-20T07:55:35.887, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v33-auto-date-time on F64 data-1m-v1: refreshed, peak 548 MB (2026-11-19T23:53:47Z).
  - Peak change: +65 MB (+11.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 613 MB vs 716 MB (-103 MB), Power Query 455 MB vs 527 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 25,530 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (20%); F16 5,050 MB: fits (12%); F32 10,170 MB: fits (6%); F64 25,530 MB: fits (2%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    79c2f30d-ee15-45f7-92a8-73654d03e1a1 TabularSequencePoint         78.7     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         77.8    21.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         73.4    21.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         72.9    21.7 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         12.0    13.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.8    11.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.2     1.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          4.5     0.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          4.3     0.0       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          3.9     0.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.7     1.9       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          3.5     0.0       0
```

## Log

```
2026-11-20T07:53:40Z run 20261120T075305Z-v33-061e: variant=v33-auto-date-time data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T07:53:49Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:53:53Z F64: v33-auto-date-time is 79c2f30d-ee15-45f7-92a8-73654d03e1a1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:54:09Z F64: model size in memory before the refresh: 69.7 MB
2026-11-20T07:54:09Z F64: refresh started, request 820390e3-8913-4775-8ad2-4000b3145cc5
2026-11-20T07:55:50Z F64: refresh refreshed (Completed) 
2026-11-20T07:55:50Z F64: monitoring database Monitoring KQL database
2026-11-20T07:56:39Z F64: ExecutionMetrics event found
2026-11-20T07:57:30Z F64: model size in memory right after the refresh: 96.2 MB
```
