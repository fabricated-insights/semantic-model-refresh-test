# Harness run 20261120T065931Z-v24b-061e

- Task: refresh
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: eced9e67-dcfc-4e07-b4c1-c84d12b9f8c1
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 727 MB, Power Query 522 MB, duration 1 min, CPU 125 s, rows 3,541,806, model 103 MB (Backup step in SemanticModelLogs)
- Refresh request f2ecf873-eb83-40c1-bcaa-54fb2f0c950c, 2026-11-20T07:00:41.84 to 2026-11-20T07:01:55.72, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v24b-second-fact-bidirectional on F64 data-1m-v1: refreshed, peak 661 MB (2026-11-19T23:07:13Z).
  - Peak change: +66 MB (+10.0%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 727 MB vs 716 MB (+11 MB), Power Query 522 MB vs 527 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 82 MB. The refresh may use the SKU maximum minus this: 25,518 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,984 MB: fits (24%); F16 5,038 MB: fits (14%); F32 10,158 MB: fits (7%); F64 25,518 MB: fits (3%); PPU 102,318 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  a21050a7-7531-4f04-a061-b795aa01fdf7 TabularSequencePoint         62.1     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         59.3    18.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         58.4    18.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         57.9    18.7 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh         16.2     5.7       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process         13.9     5.7       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData         11.7     5.6  980666
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.3    11.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.1    10.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.2     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.1     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.9     1.9  104990
```

## Log

```
2026-11-20T07:00:10Z run 20261120T065931Z-v24b-061e: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T07:00:19Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:00:23Z F64: v24b-second-fact-bidirectional is a21050a7-7531-4f04-a061-b795aa01fdf7, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:00:41Z F64: model size in memory before the refresh: 82.4 MB
2026-11-20T07:00:42Z F64: refresh started, request f2ecf873-eb83-40c1-bcaa-54fb2f0c950c
2026-11-20T07:02:27Z F64: refresh refreshed (Completed) 
2026-11-20T07:02:27Z F64: monitoring database Monitoring KQL database
2026-11-20T07:04:02Z F64: ExecutionMetrics event found
2026-11-20T07:04:04Z F64: model size in memory right after the refresh: 110.0 MB
```
