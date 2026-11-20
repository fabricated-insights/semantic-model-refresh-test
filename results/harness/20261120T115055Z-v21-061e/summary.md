# Harness run 20261120T115055Z-v21-061e

- Task: refresh
- Variant: v21-pq-group-by
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ed75012f-4297-493c-82da-2a00588597e2
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 3,444 MB, Power Query 3,249 MB, duration 1 min, CPU 174 s, rows 3,032,622, model 85 MB (Backup step in SemanticModelLogs)
- Refresh request 8e3dbc38-b991-44e3-b0de-cc78569f850a, 2026-11-20T11:53:50.81 to 2026-11-20T11:55:13.887, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v21-pq-group-by on F64 data-1m-v1: refreshed, peak 3,992 MB (2026-11-20T06:35:53Z).
  - Peak change: -548 MB (-13.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 3,444 MB vs 667 MB (+2,777 MB), Power Query 3,249 MB vs 592 MB, model 85 MB vs 73 MB.
- Model size in memory when the full refresh started: 92 MB. The refresh may use the SKU maximum minus this: 25,508 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,974 MB: OVER (116%); F16 5,028 MB: fits (68%); F32 10,148 MB: fits (34%); F64 25,508 MB: fits (14%); PPU 102,308 MB: fits (3%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    215d5bec-5f3c-4bbe-9ebf-b0ca5a0d0e72 TabularSequencePoint         75.1     0.1       0
                                           Customer Stats.Customer Stats       TabularRefresh         73.7     2.2       0
                                           Customer Stats.Customer Stats           ExecuteSql         63.9     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         60.2    19.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         57.5    19.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         56.9    18.9 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.9    11.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.7    10.4       0
                                           Customer Stats.Customer Stats              Process          9.7     2.2       0
                                           Customer Stats.Customer Stats             ReadData          9.1     1.8  471482
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.7     2.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.3     0.6       0
```

## Log

```
2026-11-20T11:53:11Z run 20261120T115055Z-v21-061e: variant=v21-pq-group-by data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T11:53:25Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:53:29Z F64: v21-pq-group-by is 215d5bec-5f3c-4bbe-9ebf-b0ca5a0d0e72, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:53:50Z F64: model size in memory before the refresh: 92.1 MB
2026-11-20T11:53:50Z F64: refresh started, request 8e3dbc38-b991-44e3-b0de-cc78569f850a
2026-11-20T11:55:31Z F64: refresh refreshed (Completed) 
2026-11-20T11:55:31Z F64: monitoring database Monitoring KQL database
2026-11-20T11:58:09Z F64: ExecutionMetrics event found
2026-11-20T11:58:11Z F64: model size in memory right after the refresh: 118.6 MB
```
