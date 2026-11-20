# Harness run 20261120T083406Z-v24b-f55a

- Task: refresh
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 68dc6edc-dae0-4d97-a883-8d426950ca8f
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 866 MB, Power Query 772 MB, duration 1 min, CPU 157 s, rows 3,541,806, model 103 MB (Backup step in XMLA trace)
- Refresh request 5f5cc8c3-f4eb-4f03-a5a7-6a1c076cde67, 2026-11-20T08:36:51.407 to 2026-11-20T08:38:23.41, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v24b-second-fact-bidirectional on PPU data-1m-v1: refreshed, peak 794 MB (2026-11-19T23:06:45Z).
  - Peak change: +72 MB (+9.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 866 MB vs 666 MB (+200 MB), Power Query 772 MB vs 591 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 82 MB. The refresh may use the SKU maximum minus this: 102,318 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,984 MB: fits (29%); F16 5,038 MB: fits (17%); F32 10,158 MB: fits (9%); F64 25,518 MB: fits (3%); PPU 102,318 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  2b9c7b82-fae8-4534-8106-25e802c59a13 TabularSequencePoint         82.0     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         81.1    23.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         77.6    23.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         77.1    22.8 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh         22.8     6.9       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process         19.9     6.9       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData         17.3     6.8  980666
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.3    12.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.1    11.1       0
                                                  <NA>               Commit          7.6     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.2     2.3       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.2     2.3       0
```

## Log

```
2026-11-20T08:36:14Z run 20261120T083406Z-v24b-f55a: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T08:36:21Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:36:24Z PPU: v24b-second-fact-bidirectional is 2b9c7b82-fae8-4534-8106-25e802c59a13, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:36:47Z PPU: model size in memory before the refresh: 82.4 MB
2026-11-20T08:36:51Z PPU: trace started (full)
2026-11-20T08:36:51Z PPU: refresh started, request 5f5cc8c3-f4eb-4f03-a5a7-6a1c076cde67
2026-11-20T08:38:31Z PPU: refresh refreshed (Completed) 
2026-11-20T08:39:02Z PPU: trace captured 291 events: ProgressReportEnd 259, ExecutionMetrics 22, CommandEnd 10
2026-11-20T08:39:03Z PPU: model size in memory right after the refresh: 110.0 MB
```
