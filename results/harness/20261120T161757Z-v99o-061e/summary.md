# Harness run 20261120T161757Z-v99o-061e

- Task: refresh
- Variant: v99o-sorts
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 524cc5b9-99e5-46d5-b067-e63182f38dbb
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 5,205 MB, Power Query 4,919 MB, duration 4 min, CPU 292 s, rows 21,583,972, model 100 MB (Backup step in SemanticModelLogs)
- Refresh request 23c846a9-9a75-4f4a-87eb-c33e3f1869d5, 2026-11-20T16:20:57.24 to 2026-11-20T16:25:05.563, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99o-sorts on F64 data-1m-v1: refreshed, peak 5,340 MB (2026-11-20T11:08:23Z).
  - Peak change: -135 MB (-2.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 5,205 MB vs 667 MB (+4,538 MB), Power Query 4,919 MB vs 592 MB, model 100 MB vs 73 MB.
- Model size in memory when the full refresh started: 99 MB. The refresh may use the SKU maximum minus this: 25,501 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,967 MB: OVER (175%); F16 5,021 MB: OVER (104%); F32 10,141 MB: fits (51%); F64 25,501 MB: fits (20%); PPU 102,301 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  de183c23-bc85-4924-a529-71615701050c TabularSequencePoint        239.3     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        227.5    21.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        129.5    21.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        129.1    21.3 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql         97.9     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.2     8.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.0     6.0       0
                                Sales.Sales Line Label       TabularRefresh          6.0     5.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.9     1.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.7     1.7       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.6     1.7  104990
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.1     0.1       0
```

## Log

```
2026-11-20T16:20:21Z run 20261120T161757Z-v99o-061e: variant=v99o-sorts data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T16:20:33Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T16:20:36Z F64: v99o-sorts is de183c23-bc85-4924-a529-71615701050c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T16:20:57Z F64: model size in memory before the refresh: 99.0 MB
2026-11-20T16:20:57Z F64: refresh started, request 23c846a9-9a75-4f4a-87eb-c33e3f1869d5
2026-11-20T16:25:08Z F64: refresh refreshed (Completed) 
2026-11-20T16:25:08Z F64: monitoring database Monitoring KQL database
2026-11-20T16:27:45Z F64: ExecutionMetrics event found
2026-11-20T16:27:47Z F64: model size in memory right after the refresh: 133.8 MB
```
