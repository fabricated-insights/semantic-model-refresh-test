# Harness run 20261120T055022Z-v18-061e

- Task: refresh
- Variant: v18-pq-10m-summary
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: aa16a939-af28-4b41-9244-47c03022e9b1
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,796 MB, Power Query 1,522 MB, duration 1 min, CPU 112 s, rows 2,561,730, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request c181b8ed-c91c-453d-b3c0-e14c633de6e4, 2026-11-20T05:53:12.707 to 2026-11-20T05:54:11.857, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v18-pq-10m-summary on F64 data-1m-v1: refreshed, peak 1,583 MB (2026-11-19T22:02:39Z).
  - Peak change: +213 MB (+13.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 1,796 MB vs 716 MB (+1,080 MB), Power Query 1,522 MB vs 527 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (60%); F16 5,054 MB: fits (36%); F32 10,174 MB: fits (18%); F64 25,534 MB: fits (7%); PPU 102,334 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  488c2f22-ab75-4ac9-87fa-79b129d25c49 TabularSequencePoint         54.7     0.1       0
                 Store Year Summary.Store Year Summary       TabularRefresh         54.5     0.0       0
                 Store Year Summary.Store Year Summary           ExecuteSql         54.4     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         37.4    11.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         36.4    11.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         36.1    11.4 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.8     5.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.7     4.7       0
                                                                     Commit          2.8     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.4     0.9       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.2     0.0       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          2.0     0.0       0
```

## Log

```
2026-11-20T05:52:39Z run 20261120T055022Z-v18-061e: variant=v18-pq-10m-summary data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T05:52:48Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T05:52:52Z F64: v18-pq-10m-summary is 488c2f22-ab75-4ac9-87fa-79b129d25c49, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T05:53:12Z F64: model size in memory before the refresh: 66.2 MB
2026-11-20T05:53:12Z F64: refresh started, request c181b8ed-c91c-453d-b3c0-e14c633de6e4
2026-11-20T05:54:23Z F64: refresh refreshed (Completed) 
2026-11-20T05:54:23Z F64: monitoring database Monitoring KQL database
2026-11-20T05:55:58Z F64: ExecutionMetrics event found
2026-11-20T05:56:16Z F64: model size in memory right after the refresh: 92.7 MB
```
