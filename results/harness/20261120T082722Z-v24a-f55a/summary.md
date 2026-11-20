# Harness run 20261120T082722Z-v24a-f55a

- Task: refresh
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e233f54d-2f38-49c2-806d-336d1a1afe4d
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 796 MB, Power Query 709 MB, duration 2 min, CPU 206 s, rows 3,541,806, model 103 MB (Backup step in XMLA trace)
- Refresh request 174a3db2-1194-4cbc-994f-c5524f16c091, 2026-11-20T08:30:05.747 to 2026-11-20T08:32:37.85, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v24a-second-fact on PPU data-1m-v1: refreshed, peak 947 MB (2026-11-19T23:00:00Z).
  - Peak change: -151 MB (-15.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 796 MB vs 666 MB (+130 MB), Power Query 709 MB vs 591 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 82 MB. The refresh may use the SKU maximum minus this: 102,318 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,984 MB: fits (27%); F16 5,038 MB: fits (16%); F32 10,158 MB: fits (8%); F64 25,518 MB: fits (3%); PPU 102,318 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  b0358b26-6f81-4c1b-a470-0f781c76b094 TabularSequencePoint        139.7     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        138.9    29.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        134.9    29.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        134.3    28.8 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh         30.7     8.1       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process         26.9     8.0       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData         23.0     7.9  980666
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         12.2    13.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         12.0    11.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         10.8     2.8       0
                                                  <NA>               Commit          9.5     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          7.3     2.7       0
```

## Log

```
2026-11-20T08:29:28Z run 20261120T082722Z-v24a-f55a: variant=v24a-second-fact data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T08:29:36Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:29:40Z PPU: v24a-second-fact is b0358b26-6f81-4c1b-a470-0f781c76b094, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:30:01Z PPU: model size in memory before the refresh: 82.4 MB
2026-11-20T08:30:05Z PPU: trace started (full)
2026-11-20T08:30:05Z PPU: refresh started, request 174a3db2-1194-4cbc-994f-c5524f16c091
2026-11-20T08:32:46Z PPU: refresh refreshed (Completed) 
2026-11-20T08:33:17Z PPU: trace captured 291 events: ProgressReportEnd 259, ExecutionMetrics 22, CommandEnd 10
2026-11-20T08:33:18Z PPU: model size in memory right after the refresh: 110.0 MB
```
