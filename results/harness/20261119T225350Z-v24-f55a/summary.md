# Harness run 20261119T225350Z-v24-f55a

- Task: refresh
- Variant: v24-bidirectional
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: c611d071-856d-4bb7-92bf-d0090ce90c92
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 677 MB, Power Query 613 MB, duration 1 min, CPU 98 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 85086b40-96d3-4cf3-872f-b0ee60bbd28f, 2026-11-19T22:54:41.897 to 2026-11-19T22:55:47.73, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v24-bidirectional on PPU data-1m-v1: refreshed, peak 551 MB (2026-11-17T05:58:36Z).
  - Peak change: +126 MB (+22.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 677 MB vs 551 MB (+126 MB), Power Query 613 MB vs 298 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (23%); F16 5,054 MB: fits (13%); F32 10,174 MB: fits (7%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  396b5678-cec7-4bcd-98dc-b22a8c270567 TabularSequencePoint         58.2     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         57.3    18.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         54.0    18.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         53.6    18.7 2349091
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          9.3     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.3    10.3       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          9.2     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.1     9.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.4     1.6       0
                                                  <NA>               Commit          4.8     0.0    <NA>
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          4.5     0.1       0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          4.3     0.0       0
```

## Log

```
2026-11-19T22:54:15Z run 20261119T225350Z-v24-f55a: variant=v24-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T22:54:20Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:54:24Z PPU: v24-bidirectional is 396b5678-cec7-4bcd-98dc-b22a8c270567, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:54:38Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-19T22:54:41Z PPU: trace started (full)
2026-11-19T22:54:42Z PPU: refresh started, request 85086b40-96d3-4cf3-872f-b0ee60bbd28f
2026-11-19T22:55:52Z PPU: refresh refreshed (Completed) 
2026-11-19T22:56:22Z PPU: trace captured 282 events: ProgressReportEnd 237, ExecutionMetrics 34, CommandEnd 11
2026-11-19T22:56:23Z PPU: model size in memory right after the refresh: 92.7 MB
```
