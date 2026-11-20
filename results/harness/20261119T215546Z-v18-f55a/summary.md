# Harness run 20261119T215546Z-v18-f55a

- Task: refresh
- Variant: v18-pq-10m-summary
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 72b70294-d4cc-4840-ab96-62c4031cc5e6
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,834 MB, Power Query 1,624 MB, duration 1 min, CPU 189 s, rows 2,561,730, model 73 MB (Backup step in XMLA trace)
- Refresh request 2c915150-f5cf-4f6d-b5f4-3113031a8a62, 2026-11-19T21:56:49.55 to 2026-11-19T21:58:21.85, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v18-pq-10m-summary on PPU data-1m-v1: refreshed, peak 1,519 MB (2026-11-17T09:27:21Z).
  - Peak change: +315 MB (+20.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 1,834 MB vs 551 MB (+1,283 MB), Power Query 1,624 MB vs 298 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (61%); F16 5,054 MB: fits (36%); F32 10,174 MB: fits (18%); F64 25,534 MB: fits (7%); PPU 102,334 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  5f501e01-52ef-4e24-81c1-aa3cafd4c095 TabularSequencePoint         84.2     0.1       0
                 Store Year Summary.Store Year Summary       TabularRefresh         83.8     0.0       0
                 Store Year Summary.Store Year Summary           ExecuteSql         83.7     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         65.6    19.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         64.3    19.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         63.6    19.1 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.0    12.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.8    10.9       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          7.4     0.0       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          7.3     0.0       0
                                                  <NA>               Commit          4.7     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.0     2.0       0
```

## Log

```
2026-11-19T21:56:19Z run 20261119T215546Z-v18-f55a: variant=v18-pq-10m-summary data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T21:56:26Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T21:56:29Z PPU: v18-pq-10m-summary is 5f501e01-52ef-4e24-81c1-aa3cafd4c095, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T21:56:46Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-19T21:56:49Z PPU: trace started (full)
2026-11-19T21:56:49Z PPU: refresh started, request 2c915150-f5cf-4f6d-b5f4-3113031a8a62
2026-11-19T21:58:30Z PPU: refresh refreshed (Completed) 
2026-11-19T21:59:00Z PPU: trace captured 288 events: ProgressReportEnd 255, ExecutionMetrics 22, CommandEnd 11
2026-11-19T21:59:01Z PPU: model size in memory right after the refresh: 92.7 MB
```
