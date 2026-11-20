# Harness run 20261120T150028Z-v31-f55a

- Task: refresh
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: cd83ecb3-b536-4e32-aef2-8d6c8c5b63c8
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,003 MB, Power Query 884 MB, duration 2 min, CPU 212 s, rows 77,732,052, model 223 MB (Backup step in XMLA trace)
- Refresh request c86a9429-5905-4b5c-ad59-e2586338ff21, 2026-11-20T15:03:57.75 to 2026-11-20T15:06:23.933, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v31-calc-columns-row on PPU data-1m-v1: refreshed, peak 1,001 MB (2026-11-20T09:18:38Z).
  - Peak change: +2 MB (+0.2%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 1,003 MB vs 604 MB (+399 MB), Power Query 884 MB vs 529 MB, model 223 MB vs 73 MB.
- Model size in memory when the full refresh started: 234 MB. The refresh may use the SKU maximum minus this: 102,166 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,832 MB: fits (35%); F16 4,886 MB: fits (21%); F32 10,006 MB: fits (10%); F64 25,366 MB: fits (4%); PPU 102,166 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  ac3ebe29-9abb-4067-9007-e7d601187a3c TabularSequencePoint        121.9     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        100.1    29.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         97.2    29.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         96.1    29.2 2349091
                                                  <NA>               Commit         20.3     0.0    <NA>
                                  Sales.Order Line Key       TabularRefresh         14.6     4.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.1    14.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.6    10.4       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          7.5     0.1       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          7.4     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.8     2.3       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.1     2.3       0
```

## Log

```
2026-11-20T15:03:11Z run 20261120T150028Z-v31-f55a: variant=v31-calc-columns-row data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T15:03:16Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T15:03:22Z PPU: v31-calc-columns-row is ac3ebe29-9abb-4067-9007-e7d601187a3c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T15:03:54Z PPU: model size in memory before the refresh: 233.5 MB
2026-11-20T15:03:57Z PPU: trace started (full)
2026-11-20T15:03:57Z PPU: refresh started, request c86a9429-5905-4b5c-ad59-e2586338ff21
2026-11-20T15:06:38Z PPU: refresh refreshed (Completed) 
2026-11-20T15:07:09Z PPU: trace captured 416 events: ProgressReportEnd 396, ExecutionMetrics 10, CommandEnd 10
2026-11-20T15:07:10Z PPU: model size in memory right after the refresh: 316.8 MB
```
