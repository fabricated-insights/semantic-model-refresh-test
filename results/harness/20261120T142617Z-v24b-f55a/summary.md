# Harness run 20261120T142617Z-v24b-f55a

- Task: refresh
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ace67439-45ad-4418-8d45-6206f2f520ec
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 805 MB, Power Query 713 MB, duration 1 min, CPU 133 s, rows 3,541,806, model 103 MB (Backup step in XMLA trace)
- Refresh request f933a050-9cd9-44f4-8d1b-a84f0e607bab, 2026-11-20T14:29:05.25 to 2026-11-20T14:30:21.14, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v24b-second-fact-bidirectional on PPU data-1m-v1: refreshed, peak 866 MB (2026-11-20T08:39:03Z).
  - Peak change: -61 MB (-7.0%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 805 MB vs 604 MB (+201 MB), Power Query 713 MB vs 529 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 82 MB. The refresh may use the SKU maximum minus this: 102,318 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,984 MB: fits (27%); F16 5,038 MB: fits (16%); F32 10,158 MB: fits (8%); F64 25,518 MB: fits (3%); PPU 102,318 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    2b9c7b82-fae8-4534-8106-25e802c59a13 TabularSequencePoint         65.6     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         64.8    19.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         61.5    19.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         61.2    19.5 2349091
                      Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh         17.7     5.6       0
                      Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process         15.0     5.6       0
                      Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData         12.7     5.5  980666
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.5    11.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.3    10.3       0
                                                                    <NA>               Commit          6.2     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.8     1.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.4     0.6       0
```

## Log

```
2026-11-20T14:28:30Z run 20261120T142617Z-v24b-f55a: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T14:28:36Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:28:40Z PPU: v24b-second-fact-bidirectional is 2b9c7b82-fae8-4534-8106-25e802c59a13, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:29:01Z PPU: model size in memory before the refresh: 82.4 MB
2026-11-20T14:29:05Z PPU: trace started (full)
2026-11-20T14:29:05Z PPU: refresh started, request f933a050-9cd9-44f4-8d1b-a84f0e607bab
2026-11-20T14:30:45Z PPU: refresh refreshed (Completed) 
2026-11-20T14:31:16Z PPU: trace captured 279 events: ProgressReportEnd 259, ExecutionMetrics 10, CommandEnd 10
2026-11-20T14:31:17Z PPU: model size in memory right after the refresh: 110.0 MB
```
