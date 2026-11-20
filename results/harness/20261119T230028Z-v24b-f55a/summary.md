# Harness run 20261119T230028Z-v24b-f55a

- Task: refresh
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3d1c08e6-014d-4aa3-8d05-f1808986c489
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 794 MB, Power Query 596 MB, duration 1 min, CPU 125 s, rows 3,541,806, model 103 MB (Backup step in XMLA trace)
- Refresh request 88e8dac7-50ad-4c1e-8260-56fcba0606d9, 2026-11-19T23:04:32.333 to 2026-11-19T23:05:45.107, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v24b-second-fact-bidirectional on PPU data-1m-v1: refreshed, peak 1,432 MB (2026-11-17T06:13:28Z).
  - Peak change: -638 MB (-44.6%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 794 MB vs 551 MB (+243 MB), Power Query 596 MB vs 298 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 82 MB. The refresh may use the SKU maximum minus this: 102,318 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,984 MB: fits (27%); F16 5,038 MB: fits (16%); F32 10,158 MB: fits (8%); F64 25,518 MB: fits (3%); PPU 102,318 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  2b9c7b82-fae8-4534-8106-25e802c59a13 TabularSequencePoint         60.5     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         59.8    20.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         58.4    20.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         57.8    20.3 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh         16.6     6.2       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process         15.4     6.1       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData         12.9     6.0  980666
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.9    12.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.8    10.7       0
                                                  <NA>               Commit          6.3     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.3     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.1     1.8       0
```

## Log

```
2026-11-19T23:03:52Z run 20261119T230028Z-v24b-f55a: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T23:04:00Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:04:06Z PPU: v24b-second-fact-bidirectional is 2b9c7b82-fae8-4534-8106-25e802c59a13, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:04:28Z PPU: model size in memory before the refresh: 82.4 MB
2026-11-19T23:04:32Z PPU: trace started (full)
2026-11-19T23:04:34Z PPU: refresh started, request 88e8dac7-50ad-4c1e-8260-56fcba0606d9
2026-11-19T23:06:14Z PPU: refresh refreshed (Completed) 
2026-11-19T23:06:45Z PPU: trace captured 305 events: ProgressReportEnd 260, ExecutionMetrics 34, CommandEnd 11
2026-11-19T23:06:46Z PPU: model size in memory right after the refresh: 110.0 MB
```
