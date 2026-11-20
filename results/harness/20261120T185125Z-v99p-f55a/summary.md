# Harness run 20261120T185125Z-v99p-f55a

- Task: refresh
- Variant: v99p-high-cardinality
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 37ca8049-c64d-404c-93b0-473e79faa4fe
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 684 MB, Power Query 497 MB, duration 2 min, CPU 140 s, rows 21,609,543, model 175 MB (Backup step in XMLA trace)
- Refresh request 56139ab9-ccb4-4326-a8a8-f861681706e0, 2026-11-20T18:54:32.373 to 2026-11-20T18:56:16.003, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99p-high-cardinality on PPU data-1m-v1: refreshed, peak 685 MB (2026-11-20T13:27:41Z).
  - Peak change: -1 MB (-0.1%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 684 MB vs 604 MB (+80 MB), Power Query 497 MB vs 529 MB, model 175 MB vs 73 MB.
- Model size in memory when the full refresh started: 174 MB. The refresh may use the SKU maximum minus this: 102,226 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,892 MB: fits (24%); F16 4,946 MB: fits (14%); F32 10,066 MB: fits (7%); F64 25,426 MB: fits (3%); PPU 102,226 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  7bc682e3-1008-458e-bb4b-0c0ce9e874f9 TabularSequencePoint         91.7     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         82.6    25.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         72.0    25.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         71.7    25.2 2349091
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         13.0     1.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql         10.5     0.0       0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh         10.2     0.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql         10.1     0.0       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh         10.0     0.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh         10.0     0.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          9.9     0.0       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          9.9     0.0       0
```

## Log

```
2026-11-20T18:53:50Z run 20261120T185125Z-v99p-f55a: variant=v99p-high-cardinality data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T18:53:58Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T18:54:03Z PPU: v99p-high-cardinality is 7bc682e3-1008-458e-bb4b-0c0ce9e874f9, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T18:54:28Z PPU: model size in memory before the refresh: 174.2 MB
2026-11-20T18:54:32Z PPU: trace started (full)
2026-11-20T18:54:32Z PPU: refresh started, request 56139ab9-ccb4-4326-a8a8-f861681706e0
2026-11-20T18:56:43Z PPU: refresh refreshed (Completed) 
2026-11-20T18:57:13Z PPU: trace captured 443 events: ProgressReportEnd 423, ExecutionMetrics 10, CommandEnd 10
2026-11-20T18:57:14Z PPU: model size in memory right after the refresh: 209.0 MB
```
