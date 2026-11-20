# Harness run 20261120T160742Z-v99n-061e

- Task: refresh
- Variant: v99n-text-staging
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ade8cb20-37b5-4aab-9fe9-1c8d37682a6b
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 695 MB, Power Query 454 MB, duration 5 min, CPU 317 s, rows 21,587,990, model 92 MB (Backup step in SemanticModelLogs)
- Refresh request fc48767b-bd4f-4973-8929-46a292781150, 2026-11-20T16:10:21.98 to 2026-11-20T16:15:09.98, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99n-text-staging on F64 data-1m-v1: refreshed, peak 688 MB (2026-11-20T11:01:23Z).
  - Peak change: +7 MB (+1.0%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 695 MB vs 667 MB (+28 MB), Power Query 454 MB vs 592 MB, model 92 MB vs 73 MB.
- Model size in memory when the full refresh started: 91 MB. The refresh may use the SKU maximum minus this: 25,509 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,975 MB: fits (23%); F16 5,029 MB: fits (14%); F32 10,149 MB: fits (7%); F64 25,509 MB: fits (3%); PPU 102,309 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  08ef8a12-823e-4975-bebb-3bc315fc0c5d TabularSequencePoint        283.6     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        280.3    16.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        279.2    16.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        279.1    16.3 2349091
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.1     0.9       0
                                                                     Commit          2.8     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.3     0.9       0
                                Sales.Sales Line Label       TabularRefresh          2.2     2.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          2.2     3.5       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.2     0.9  104990
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          2.0     2.0       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          1.4     0.0       0
```

## Log

```
2026-11-20T16:09:48Z run 20261120T160742Z-v99n-061e: variant=v99n-text-staging data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T16:09:55Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T16:09:58Z F64: v99n-text-staging is 08ef8a12-823e-4975-bebb-3bc315fc0c5d, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T16:10:21Z F64: model size in memory before the refresh: 90.7 MB
2026-11-20T16:10:22Z F64: refresh started, request fc48767b-bd4f-4973-8929-46a292781150
2026-11-20T16:15:33Z F64: refresh refreshed (Completed) 
2026-11-20T16:15:33Z F64: monitoring database Monitoring KQL database
2026-11-20T16:17:08Z F64: ExecutionMetrics event found
2026-11-20T16:17:11Z F64: model size in memory right after the refresh: 124.3 MB
```
