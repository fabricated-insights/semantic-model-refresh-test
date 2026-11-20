# Harness run 20261120T141933Z-v24a-f55a

- Task: refresh
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a2c313d9-ae92-4dfe-96bb-52be7fa8c0a8
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 816 MB, Power Query 711 MB, duration 1 min, CPU 136 s, rows 3,541,806, model 103 MB (Backup step in XMLA trace)
- Refresh request 8898745d-7da5-416e-9e46-5c2705860d51, 2026-11-20T14:22:42.913 to 2026-11-20T14:24:39.847, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v24a-second-fact on PPU data-1m-v1: refreshed, peak 796 MB (2026-11-20T08:33:17Z).
  - Peak change: +20 MB (+2.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 816 MB vs 604 MB (+212 MB), Power Query 711 MB vs 529 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 82 MB. The refresh may use the SKU maximum minus this: 102,318 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,984 MB: fits (27%); F16 5,038 MB: fits (16%); F32 10,158 MB: fits (8%); F64 25,518 MB: fits (3%); PPU 102,318 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  b0358b26-6f81-4c1b-a470-0f781c76b094 TabularSequencePoint         67.4     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         66.6    21.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         63.9    21.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         63.3    21.1 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh         17.0     6.1       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process         15.9     6.0       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData         13.0     6.0  980666
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.3    12.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.1    11.1       0
                                                  <NA>               Commit          7.8     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.4     1.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.1     1.8       0
```

## Log

```
2026-11-20T14:22:08Z run 20261120T141933Z-v24a-f55a: variant=v24a-second-fact data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T14:22:14Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:22:17Z PPU: v24a-second-fact is b0358b26-6f81-4c1b-a470-0f781c76b094, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:22:39Z PPU: model size in memory before the refresh: 82.4 MB
2026-11-20T14:22:42Z PPU: trace started (full)
2026-11-20T14:22:43Z PPU: refresh started, request 8898745d-7da5-416e-9e46-5c2705860d51
2026-11-20T14:24:53Z PPU: refresh refreshed (Completed) 
2026-11-20T14:25:24Z PPU: trace captured 279 events: ProgressReportEnd 259, ExecutionMetrics 10, CommandEnd 10
2026-11-20T14:25:25Z PPU: model size in memory right after the refresh: 110.0 MB
```
