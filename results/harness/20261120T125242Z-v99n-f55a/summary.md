# Harness run 20261120T125242Z-v99n-f55a

- Task: refresh
- Variant: v99n-text-staging
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 20d4ec24-37ca-43ea-ab3a-833626bd956b
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 627 MB, Power Query 531 MB, duration 9 min, CPU 624 s, rows 21,587,990, model 92 MB (Backup step in XMLA trace)
- Refresh request fa704f54-a7c1-42d1-9384-d72206062bf1, 2026-11-20T12:53:44.233 to 2026-11-20T13:03:05.997, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99n-text-staging on PPU data-1m-v1: refreshed, peak 668 MB (2026-11-20T06:43:38Z).
  - Peak change: -41 MB (-6.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 627 MB vs 666 MB (-39 MB), Power Query 531 MB vs 591 MB, model 92 MB vs 73 MB.
- Model size in memory when the full refresh started: 91 MB. The refresh may use the SKU maximum minus this: 102,309 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,975 MB: fits (21%); F16 5,029 MB: fits (12%); F32 10,149 MB: fits (6%); F64 25,509 MB: fits (2%); PPU 102,309 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    b50ca483-f3ad-48d4-bf77-74585e534ddb TabularSequencePoint        551.8     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        545.5    32.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        542.3    32.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        542.0    32.1 2349091
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.5     2.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.4     8.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.2     6.2       0
                                                                    <NA>               Commit          5.9     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.8     2.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.7     2.0  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          4.6     0.6       0
                                                  Sales.Sales Line Label       TabularRefresh          4.1     4.1       0
```

## Log

```
2026-11-20T12:53:15Z run 20261120T125242Z-v99n-f55a: variant=v99n-text-staging data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T12:53:20Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:53:24Z PPU: v99n-text-staging is b50ca483-f3ad-48d4-bf77-74585e534ddb, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:53:40Z PPU: model size in memory before the refresh: 90.7 MB
2026-11-20T12:53:44Z PPU: trace started (full)
2026-11-20T12:53:44Z PPU: refresh started, request fa704f54-a7c1-42d1-9384-d72206062bf1
2026-11-20T13:03:26Z PPU: refresh refreshed (Completed) 
2026-11-20T13:03:57Z PPU: trace captured 408 events: ProgressReportEnd 388, ExecutionMetrics 10, CommandEnd 10
2026-11-20T13:03:59Z PPU: model size in memory right after the refresh: 124.3 MB
```
