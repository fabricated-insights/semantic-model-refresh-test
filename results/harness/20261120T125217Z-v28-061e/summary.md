# Harness run 20261120T125217Z-v28-061e

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 20420d72-8e4e-4e61-a4e9-fcf34c3779ef
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 760 MB, Power Query 475 MB, duration 1 min, CPU 58 s, rows 2,561,140, model 69 MB (Backup step in SemanticModelLogs)
- Refresh request 91d42d0a-2205-4681-9552-d37167732a80, 2026-11-20T12:53:36.95 to 2026-11-20T12:54:11.907, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v28-types-all-text on F64 data-1m-v1: refreshed, peak 630 MB (2026-11-20T07:29:46Z).
  - Peak change: +130 MB (+20.6%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 760 MB vs 667 MB (+93 MB), Power Query 475 MB vs 592 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 96 MB. The refresh may use the SKU maximum minus this: 25,504 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,970 MB: fits (26%); F16 5,024 MB: fits (15%); F32 10,144 MB: fits (7%); F64 25,504 MB: fits (3%); PPU 102,304 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    bc793114-53e1-4476-8e50-c4b0c5b15603 TabularSequencePoint         30.7     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         28.9    16.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         27.9    16.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         27.7    16.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.7     4.7       0
                                                                                       Commit          2.3     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.1     0.9       0
                                                      Sales.Order Number       TabularRefresh          1.7     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.4     0.9  104990
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          1.4     0.1       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     0.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.3     0.4       0
```

## Log

```
2026-11-20T12:53:09Z run 20261120T125217Z-v28-061e: variant=v28-types-all-text data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T12:53:17Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:53:21Z F64: v28-types-all-text is bc793114-53e1-4476-8e50-c4b0c5b15603, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:53:36Z F64: model size in memory before the refresh: 95.8 MB
2026-11-20T12:53:37Z F64: refresh started, request 91d42d0a-2205-4681-9552-d37167732a80
2026-11-20T12:54:22Z F64: refresh refreshed (Completed) 
2026-11-20T12:54:22Z F64: monitoring database Monitoring KQL database
2026-11-20T12:55:58Z F64: ExecutionMetrics event found
2026-11-20T12:56:00Z F64: model size in memory right after the refresh: 171.5 MB
```
