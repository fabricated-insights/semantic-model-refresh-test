# Harness run 20261120T112046Z-v00-061e

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: c244a7b9-8bd0-438a-95fd-940e3e5f41dc
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 667 MB, Power Query 592 MB, duration 1 min, CPU 110 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request a3634c1c-0fc0-41c7-a8c0-994e517662e7, 2026-11-20T11:23:58.673 to 2026-11-20T11:25:13.917, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64 data-1m-v1: refreshed, peak 716 MB (2026-11-20T05:49:55Z).
  - Peak change: -49 MB (-6.8%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (22%); F16 5,054 MB: fits (13%); F32 10,174 MB: fits (7%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    aee1f825-0998-43ef-9b7c-fa80d819f127 TabularSequencePoint         65.5     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         64.8    20.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         61.4    20.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         60.3    20.4 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.9    13.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.7    11.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.7     1.9       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          4.1     0.1       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          3.8     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          3.3     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.0     0.5       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          2.9     0.0       0
```

## Log

```
2026-11-20T11:23:23Z run 20261120T112046Z-v00-061e: variant=v00-baseline data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T11:23:31Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:23:35Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:23:58Z F64: model size in memory before the refresh: 66.2 MB
2026-11-20T11:23:58Z F64: refresh started, request a3634c1c-0fc0-41c7-a8c0-994e517662e7
2026-11-20T11:25:39Z F64: refresh refreshed (Completed) 
2026-11-20T11:25:39Z F64: monitoring database Monitoring KQL database
2026-11-20T11:27:16Z F64: ExecutionMetrics event found
2026-11-20T11:27:18Z F64: model size in memory right after the refresh: 92.7 MB
```
