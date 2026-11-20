# Harness run 20261120T113807Z-v20-061e

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a6a3de64-3b34-4010-8fab-8b37b0d409cf
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 5,176 MB, Power Query 4,910 MB, duration 7 min, CPU 587 s, rows 2,561,140, model 72 MB (Backup step in SemanticModelLogs)
- Refresh request 13ca7e42-b6c4-456e-8ccb-a6dac3d471c9, 2026-11-20T11:41:02.49 to 2026-11-20T11:48:13.803, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v20-pq-sort on F64 data-1m-v1: refreshed, peak 5,187 MB (2026-11-20T06:29:46Z).
  - Peak change: -11 MB (-0.2%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 5,176 MB vs 667 MB (+4,509 MB), Power Query 4,910 MB vs 592 MB, model 72 MB vs 73 MB.
- Model size in memory when the full refresh started: 65 MB. The refresh may use the SKU maximum minus this: 25,535 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,001 MB: OVER (172%); F16 5,055 MB: OVER (102%); F32 10,175 MB: fits (51%); F64 25,535 MB: fits (20%); PPU 102,335 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    d6f42335-d4fb-411e-9ca5-a063e204bb89 TabularSequencePoint        422.2     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        394.1    20.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        280.9    20.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        280.6    20.7 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        113.0     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.6     8.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.4     7.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.5     1.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.1     1.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.0     1.7  104990
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.1     0.1       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.1     0.7       0
```

## Log

```
2026-11-20T11:40:25Z run 20261120T113807Z-v20-061e: variant=v20-pq-sort data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T11:40:34Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:40:38Z F64: v20-pq-sort is d6f42335-d4fb-411e-9ca5-a063e204bb89, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:41:02Z F64: model size in memory before the refresh: 65.3 MB
2026-11-20T11:41:02Z F64: refresh started, request 13ca7e42-b6c4-456e-8ccb-a6dac3d471c9
2026-11-20T11:48:44Z F64: refresh refreshed (Completed) 
2026-11-20T11:48:44Z F64: monitoring database Monitoring KQL database
2026-11-20T11:50:20Z F64: ExecutionMetrics event found
2026-11-20T11:50:23Z F64: model size in memory right after the refresh: 91.9 MB
```
