# Harness run 20261119T235414Z-v34-061e

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 01f32279-2930-48a0-a626-07cbea94963d
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 550 MB, Power Query 270 MB, duration 1 min, CPU 56 s, rows 2,847,496, model 74 MB (Backup step in SemanticModelLogs)
- Refresh request a2ab3165-3222-41b1-8130-b8d195ce677f, 2026-11-19T23:55:14.193 to 2026-11-19T23:56:00.907, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v34-auto-date-time-no-date-table on F64 data-1m-v1: refreshed, peak 723 MB (2026-11-13T20:44:50Z).
  - Peak change: -173 MB (-23.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 550 MB vs 615 MB (-65 MB), Power Query 270 MB vs 335 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 25,530 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (18%); F16 5,050 MB: fits (11%); F32 10,170 MB: fits (5%); F64 25,530 MB: fits (2%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    8876d3c4-cd50-45e6-b465-6758c70c6ca0 TabularSequencePoint         41.8     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         41.3    10.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         33.3    10.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         33.0    10.4 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          7.9     0.0       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          7.7     0.0       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          7.6     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.7     5.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.6     4.6       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.1     0.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.0     0.7       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          2.6     0.0       0
```

## Log

```
2026-11-19T23:54:48Z run 20261119T235414Z-v34-061e: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T23:54:57Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:55:01Z F64: v34-auto-date-time-no-date-table is 8876d3c4-cd50-45e6-b465-6758c70c6ca0, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:55:14Z F64: model size in memory before the refresh: 70.3 MB
2026-11-19T23:55:14Z F64: refresh started, request a2ab3165-3222-41b1-8130-b8d195ce677f
2026-11-19T23:56:24Z F64: refresh refreshed (Completed) 
2026-11-19T23:56:24Z F64: monitoring database Monitoring KQL database
2026-11-19T23:56:42Z F64: ExecutionMetrics event found
2026-11-19T23:57:00Z F64: model size in memory right after the refresh: 96.9 MB
```
