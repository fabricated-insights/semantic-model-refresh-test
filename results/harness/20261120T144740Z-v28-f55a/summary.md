# Harness run 20261120T144740Z-v28-f55a

- Task: refresh
- Variant: v28-types-all-text
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 7d08d1ef-5c74-4999-9b87-c9be7273a1a4
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 981 MB, Power Query 954 MB, duration 1 min, CPU 119 s, rows 2,561,140, model 69 MB (Backup step in XMLA trace)
- Refresh request 87865d79-fc89-43b2-915a-3c69a589c8ee, 2026-11-20T14:51:05.787 to 2026-11-20T14:52:16.853, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v28-types-all-text on PPU data-1m-v1: refreshed, peak 693 MB (2026-11-20T08:58:59Z).
  - Peak change: +288 MB (+41.6%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 981 MB vs 604 MB (+377 MB), Power Query 954 MB vs 529 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 96 MB. The refresh may use the SKU maximum minus this: 102,304 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,970 MB: fits (33%); F16 5,024 MB: fits (20%); F32 10,144 MB: fits (10%); F64 25,504 MB: fits (4%); PPU 102,304 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  c247c1bb-bfef-4c45-b306-7b5ea0d8fe26 TabularSequencePoint         62.2     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.7    33.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         57.0    33.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         56.1    33.2 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.1    11.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          7.5     0.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          7.3     0.0       0
                                                  <NA>               Commit          5.2     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.5     2.2       0
                                    Sales.Order Number       TabularRefresh          3.0     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.0     2.2  104990
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     2.2       0
```

## Log

```
2026-11-20T14:50:31Z run 20261120T144740Z-v28-f55a: variant=v28-types-all-text data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T14:50:36Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:50:39Z PPU: v28-types-all-text is c247c1bb-bfef-4c45-b306-7b5ea0d8fe26, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:51:02Z PPU: model size in memory before the refresh: 95.8 MB
2026-11-20T14:51:05Z PPU: trace started (full)
2026-11-20T14:51:06Z PPU: refresh started, request 87865d79-fc89-43b2-915a-3c69a589c8ee
2026-11-20T14:52:46Z PPU: refresh refreshed (Completed) 
2026-11-20T14:53:17Z PPU: trace captured 256 events: ProgressReportEnd 236, ExecutionMetrics 10, CommandEnd 10
2026-11-20T14:53:17Z PPU: model size in memory right after the refresh: 171.5 MB
```
