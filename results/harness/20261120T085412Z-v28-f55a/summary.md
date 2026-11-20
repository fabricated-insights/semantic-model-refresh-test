# Harness run 20261120T085412Z-v28-f55a

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: c5347c5e-1a83-4efd-936a-b593744dde51
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 693 MB, Power Query 400 MB, duration 1 min, CPU 120 s, rows 2,561,140, model 69 MB (Backup step in XMLA trace)
- Refresh request 55bfbb34-b20d-42a8-96da-972386e2cde1, 2026-11-20T08:57:18.657 to 2026-11-20T08:58:26.46, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v28-types-all-text on PPU data-1m-v1: refreshed, peak 706 MB (2026-11-19T23:24:15Z).
  - Peak change: -13 MB (-1.8%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 693 MB vs 666 MB (+27 MB), Power Query 400 MB vs 591 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 96 MB. The refresh may use the SKU maximum minus this: 102,304 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,970 MB: fits (23%); F16 5,024 MB: fits (14%); F32 10,144 MB: fits (7%); F64 25,504 MB: fits (3%); PPU 102,304 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  c247c1bb-bfef-4c45-b306-7b5ea0d8fe26 TabularSequencePoint         60.5     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         57.2    32.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         54.6    32.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         53.8    32.3 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.4    10.3       0
                                                  <NA>               Commit          5.2     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.0     2.0       0
                                    Sales.Order Number       TabularRefresh          3.0     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.7     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.5     1.9  104990
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.5     0.0       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.4     0.0       0
```

## Log

```
2026-11-20T08:56:43Z run 20261120T085412Z-v28-f55a: variant=v28-types-all-text data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T08:56:49Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:56:53Z PPU: v28-types-all-text is c247c1bb-bfef-4c45-b306-7b5ea0d8fe26, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:57:15Z PPU: model size in memory before the refresh: 95.8 MB
2026-11-20T08:57:18Z PPU: trace started (full)
2026-11-20T08:57:18Z PPU: refresh started, request 55bfbb34-b20d-42a8-96da-972386e2cde1
2026-11-20T08:58:29Z PPU: refresh refreshed (Completed) 
2026-11-20T08:58:59Z PPU: trace captured 268 events: ProgressReportEnd 236, ExecutionMetrics 22, CommandEnd 10
2026-11-20T08:59:00Z PPU: model size in memory right after the refresh: 171.5 MB
```
