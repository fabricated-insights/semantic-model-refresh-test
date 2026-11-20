# Harness run 20261120T183026Z-v99n-f55a

- Task: refresh
- Variant: v99n-text-staging
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 0381bf41-f487-4b8a-aed0-748c01e6ad2b
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 703 MB, Power Query 594 MB, duration 7 min, CPU 490 s, rows 21,587,990, model 92 MB (Backup step in XMLA trace)
- Refresh request eb285342-4641-4be3-bbc1-c60ba1d87fcb, 2026-11-20T18:33:21.423 to 2026-11-20T18:40:32.713, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99n-text-staging on PPU data-1m-v1: refreshed, peak 627 MB (2026-11-20T13:03:57Z).
  - Peak change: +76 MB (+12.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 703 MB vs 604 MB (+99 MB), Power Query 594 MB vs 529 MB, model 92 MB vs 73 MB.
- Model size in memory when the full refresh started: 91 MB. The refresh may use the SKU maximum minus this: 102,309 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,975 MB: fits (24%); F16 5,029 MB: fits (14%); F32 10,149 MB: fits (7%); F64 25,509 MB: fits (3%); PPU 102,309 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  b50ca483-f3ad-48d4-bf77-74585e534ddb TabularSequencePoint        423.6     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        417.9    29.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        416.6    29.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        416.3    29.6 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.4     8.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.1     6.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.7     2.1       0
                                                  <NA>               Commit          5.1     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.6     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.5     2.0  104990
                                Sales.Sales Line Label       TabularRefresh          3.7     3.7       0
                                   Sales.Customer Name       TabularRefresh          1.9     1.5       0
```

## Log

```
2026-11-20T18:32:44Z run 20261120T183026Z-v99n-f55a: variant=v99n-text-staging data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T18:32:51Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T18:32:54Z PPU: v99n-text-staging is b50ca483-f3ad-48d4-bf77-74585e534ddb, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T18:33:17Z PPU: model size in memory before the refresh: 90.7 MB
2026-11-20T18:33:21Z PPU: trace started (full)
2026-11-20T18:33:21Z PPU: refresh started, request eb285342-4641-4be3-bbc1-c60ba1d87fcb
2026-11-20T18:41:02Z PPU: refresh refreshed (Completed) 
2026-11-20T18:41:33Z PPU: trace captured 408 events: ProgressReportEnd 388, ExecutionMetrics 10, CommandEnd 10
2026-11-20T18:41:34Z PPU: model size in memory right after the refresh: 124.3 MB
```
