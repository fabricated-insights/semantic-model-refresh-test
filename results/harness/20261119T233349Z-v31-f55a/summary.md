# Harness run 20261119T233349Z-v31-f55a

- Task: refresh
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e1506e8e-be0d-48ce-8dd5-4b1f77596fd2
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 938 MB, Power Query 737 MB, duration 2 min, CPU 174 s, rows 77,732,052, model 223 MB (Backup step in XMLA trace)
- Refresh request 77113656-2824-4bde-9676-eddee2c0363b, 2026-11-19T23:34:51.723 to 2026-11-19T23:36:47.033, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v31-calc-columns-row on PPU data-1m-v1: refreshed, peak 849 MB (2026-11-17T14:33:16Z).
  - Peak change: +89 MB (+10.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 938 MB vs 551 MB (+387 MB), Power Query 737 MB vs 298 MB, model 223 MB vs 73 MB.
- Model size in memory when the full refresh started: 234 MB. The refresh may use the SKU maximum minus this: 102,166 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,832 MB: fits (33%); F16 4,886 MB: fits (19%); F32 10,006 MB: fits (9%); F64 25,366 MB: fits (4%); PPU 102,166 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  ac3ebe29-9abb-4067-9007-e7d601187a3c TabularSequencePoint         97.2     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         78.4    26.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         76.8    26.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         75.8    26.4 2349091
                                                  <NA>               Commit         13.9     0.0    <NA>
                                  Sales.Order Line Key       TabularRefresh         13.0     3.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.4    14.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.0    10.8       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          7.6     0.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          7.4     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.7     2.2       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.1     2.2       0
```

## Log

```
2026-11-19T23:34:23Z run 20261119T233349Z-v31-f55a: variant=v31-calc-columns-row data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T23:34:30Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:34:35Z PPU: v31-calc-columns-row is ac3ebe29-9abb-4067-9007-e7d601187a3c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:34:48Z PPU: model size in memory before the refresh: 233.5 MB
2026-11-19T23:34:51Z PPU: trace started (full)
2026-11-19T23:34:51Z PPU: refresh started, request 77113656-2824-4bde-9676-eddee2c0363b
2026-11-19T23:37:03Z PPU: refresh refreshed (Completed) 
2026-11-19T23:37:34Z PPU: trace captured 442 events: ProgressReportEnd 397, ExecutionMetrics 34, CommandEnd 11
2026-11-19T23:37:34Z PPU: model size in memory right after the refresh: 316.8 MB
```
