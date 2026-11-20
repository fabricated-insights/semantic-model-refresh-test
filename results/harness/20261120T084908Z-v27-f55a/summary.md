# Harness run 20261120T084908Z-v27-f55a

- Task: refresh
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e0446ed4-31f3-4d92-b88d-fa914fdeea04
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 607 MB, Power Query 531 MB, duration 1 min, CPU 96 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 9f4eebf1-0884-41d3-ae34-2cd5dd1e925b, 2026-11-20T08:52:11.587 to 2026-11-20T08:53:12.947, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v27-high-cardinality-visuals on PPU data-1m-v1: refreshed, peak 550 MB (2026-11-19T23:21:19Z).
  - Peak change: +57 MB (+10.4%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 607 MB vs 666 MB (-59 MB), Power Query 531 MB vs 591 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (20%); F16 5,054 MB: fits (12%); F32 10,174 MB: fits (6%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    c613573e-80fa-4597-8fae-8cbf73e69fa6 TabularSequencePoint         55.7     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         55.1    18.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         51.9    18.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         51.6    18.3 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.4    10.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.2     9.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.5     1.7       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          4.0     0.5       0
                                                                    <NA>               Commit          3.8     0.0    <NA>
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          3.3     0.1       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          3.2     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          3.1     0.0       0
```

## Log

```
2026-11-20T08:51:35Z run 20261120T084908Z-v27-f55a: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T08:51:42Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:51:45Z PPU: v27-high-cardinality-visuals is c613573e-80fa-4597-8fae-8cbf73e69fa6, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:52:08Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-20T08:52:11Z PPU: trace started (full)
2026-11-20T08:52:11Z PPU: refresh started, request 9f4eebf1-0884-41d3-ae34-2cd5dd1e925b
2026-11-20T08:53:22Z PPU: refresh refreshed (Completed) 
2026-11-20T08:53:52Z PPU: trace captured 268 events: ProgressReportEnd 236, ExecutionMetrics 22, CommandEnd 10
2026-11-20T08:53:53Z PPU: model size in memory right after the refresh: 92.7 MB
```
