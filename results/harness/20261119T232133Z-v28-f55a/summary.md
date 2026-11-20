# Harness run 20261119T232133Z-v28-f55a

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 267cd07c-24ac-4b38-a720-972efd12f86c
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 706 MB, Power Query 448 MB, duration 1 min, CPU 105 s, rows 2,561,140, model 69 MB (Backup step in XMLA trace)
- Refresh request 15fd27fe-f27d-4057-95f6-50af4cdb145f, 2026-11-19T23:22:34.62 to 2026-11-19T23:23:35.383, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v28-types-all-text on PPU data-1m-v1: refreshed, peak 687 MB (2026-11-17T06:38:51Z).
  - Peak change: +19 MB (+2.8%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 706 MB vs 551 MB (+155 MB), Power Query 448 MB vs 298 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 96 MB. The refresh may use the SKU maximum minus this: 102,304 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,970 MB: fits (24%); F16 5,024 MB: fits (14%); F32 10,144 MB: fits (7%); F64 25,504 MB: fits (3%); PPU 102,304 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  c247c1bb-bfef-4c45-b306-7b5ea0d8fe26 TabularSequencePoint         53.8     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         50.6    29.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         48.7    29.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         48.3    29.3 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.2     9.2       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          7.4     0.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          7.3     0.0       0
                                                  <NA>               Commit          4.4     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.8     1.9       0
                                    Sales.Order Number       TabularRefresh          2.9     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.6     1.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.5     1.8  104990
```

## Log

```
2026-11-19T23:22:07Z run 20261119T232133Z-v28-f55a: variant=v28-types-all-text data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T23:22:14Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:22:18Z PPU: v28-types-all-text is c247c1bb-bfef-4c45-b306-7b5ea0d8fe26, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:22:31Z PPU: model size in memory before the refresh: 95.8 MB
2026-11-19T23:22:34Z PPU: trace started (full)
2026-11-19T23:22:34Z PPU: refresh started, request 15fd27fe-f27d-4057-95f6-50af4cdb145f
2026-11-19T23:23:45Z PPU: refresh refreshed (Completed) 
2026-11-19T23:24:15Z PPU: trace captured 282 events: ProgressReportEnd 237, ExecutionMetrics 34, CommandEnd 11
2026-11-19T23:24:16Z PPU: model size in memory right after the refresh: 171.5 MB
```
