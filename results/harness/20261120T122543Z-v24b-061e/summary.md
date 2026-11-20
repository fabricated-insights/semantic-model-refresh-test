# Harness run 20261120T122543Z-v24b-061e

- Task: refresh
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: c5748d2b-0556-499a-9d20-2e7ad1d4c9ba
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 739 MB, Power Query 645 MB, duration 1 min, CPU 110 s, rows 3,541,806, model 103 MB (Backup step in SemanticModelLogs)
- Refresh request 893bfec3-26eb-4ecc-94a9-98ff3c4a9ce5, 2026-11-20T12:28:46.2 to 2026-11-20T12:29:48.02, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v24b-second-fact-bidirectional on F64 data-1m-v1: refreshed, peak 727 MB (2026-11-20T07:04:03Z).
  - Peak change: +12 MB (+1.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 739 MB vs 667 MB (+72 MB), Power Query 645 MB vs 592 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 82 MB. The refresh may use the SKU maximum minus this: 25,518 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,984 MB: fits (25%); F16 5,038 MB: fits (15%); F32 10,158 MB: fits (7%); F64 25,518 MB: fits (3%); PPU 102,318 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    a21050a7-7531-4f04-a061-b795aa01fdf7 TabularSequencePoint         53.7     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         53.1    17.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         50.0    17.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         49.7    17.4 2349091
                      Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh         14.9     5.4       0
                      Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process         12.3     5.4       0
                      Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData         10.5     5.3  980666
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.5     9.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.3     8.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.2     1.8       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.2     0.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          3.0     0.0       0
```

## Log

```
2026-11-20T12:28:09Z run 20261120T122543Z-v24b-061e: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T12:28:16Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:28:21Z F64: v24b-second-fact-bidirectional is a21050a7-7531-4f04-a061-b795aa01fdf7, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:28:46Z F64: model size in memory before the refresh: 82.4 MB
2026-11-20T12:28:46Z F64: refresh started, request 893bfec3-26eb-4ecc-94a9-98ff3c4a9ce5
2026-11-20T12:29:56Z F64: refresh refreshed (Completed) 
2026-11-20T12:29:57Z F64: monitoring database Monitoring KQL database
2026-11-20T12:30:46Z F64: ExecutionMetrics event found
2026-11-20T12:30:48Z F64: model size in memory right after the refresh: 110.0 MB
```
