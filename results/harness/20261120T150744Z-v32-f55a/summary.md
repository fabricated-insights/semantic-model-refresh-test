# Harness run 20261120T150744Z-v32-f55a

- Task: refresh
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6d884b2a-9fb3-41fa-ad43-c2988238cecf
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 802 MB, Power Query 463 MB, duration 1 min, CPU 127 s, rows 24,570,331, model 221 MB (Backup step in XMLA trace)
- Refresh request faf9ae66-8664-4804-bc08-5f08a3e9b05e, 2026-11-20T15:10:53.523 to 2026-11-20T15:12:17.973, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v32-calc-columns-aggregate on PPU data-1m-v1: refreshed, peak 868 MB (2026-11-20T09:24:52Z).
  - Peak change: -66 MB (-7.6%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 802 MB vs 604 MB (+198 MB), Power Query 463 MB vs 529 MB, model 221 MB vs 73 MB.
- Model size in memory when the full refresh started: 341 MB. The refresh may use the SKU maximum minus this: 102,059 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,725 MB: fits (29%); F16 4,779 MB: fits (17%); F32 9,899 MB: fits (8%); F64 25,259 MB: fits (3%); PPU 102,059 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  6873b8a8-fea6-4828-b1a1-ee4b78ed0d69 TabularSequencePoint         69.4     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         61.8    22.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         60.1    21.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         59.8    21.9 2349091
                                                  <NA>               Commit         11.5     0.0    <NA>
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.9     9.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.6     6.7       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.2     1.9       0
                          Sales.Line Share Of Customer       TabularRefresh          3.9     2.6       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     1.8       0
                             Sales.Line Share Of Order       TabularRefresh          2.9     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.8     1.8  104990
```

## Log

```
2026-11-20T15:10:11Z run 20261120T150744Z-v32-f55a: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T15:10:18Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T15:10:23Z PPU: v32-calc-columns-aggregate is 6873b8a8-fea6-4828-b1a1-ee4b78ed0d69, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T15:10:49Z PPU: model size in memory before the refresh: 341.3 MB
2026-11-20T15:10:53Z PPU: trace started (full)
2026-11-20T15:10:53Z PPU: refresh started, request faf9ae66-8664-4804-bc08-5f08a3e9b05e
2026-11-20T15:12:34Z PPU: refresh refreshed (Completed) 
2026-11-20T15:13:04Z PPU: trace captured 364 events: ProgressReportEnd 344, ExecutionMetrics 10, CommandEnd 10
2026-11-20T15:13:05Z PPU: model size in memory right after the refresh: 367.9 MB
```
