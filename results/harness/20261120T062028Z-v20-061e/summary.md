# Harness run 20261120T062028Z-v20-061e

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: cc969c87-1f8b-42c0-9340-9c26532b236c
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 5,187 MB, Power Query 4,940 MB, duration 4 min, CPU 255 s, rows 2,561,140, model 72 MB (Backup step in SemanticModelLogs)
- Refresh request e9abc5cb-fecc-446d-b9c6-e232bcb9e05a, 2026-11-20T06:23:27.727 to 2026-11-20T06:27:05.963, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v20-pq-sort on F64 data-1m-v1: refreshed, peak 5,200 MB (2026-11-19T22:31:08Z).
  - Peak change: -13 MB (-0.2%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 5,187 MB vs 716 MB (+4,471 MB), Power Query 4,940 MB vs 527 MB, model 72 MB vs 73 MB.
- Model size in memory when the full refresh started: 65 MB. The refresh may use the SKU maximum minus this: 25,535 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,001 MB: OVER (173%); F16 5,055 MB: OVER (103%); F32 10,175 MB: fits (51%); F64 25,535 MB: fits (20%); PPU 102,335 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    d6f42335-d4fb-411e-9ca5-a063e204bb89 TabularSequencePoint        210.5     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        207.9    19.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        105.7    19.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        105.4    19.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        102.1     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.5     9.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.4     8.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.5     1.6       0
                                                                                       Commit          4.4     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.5     1.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.4     1.5  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.3     0.6       0
```

## Log

```
2026-11-20T06:22:47Z run 20261120T062028Z-v20-061e: variant=v20-pq-sort data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T06:23:01Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T06:23:05Z F64: v20-pq-sort is d6f42335-d4fb-411e-9ca5-a063e204bb89, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T06:23:27Z F64: model size in memory before the refresh: 65.3 MB
2026-11-20T06:23:27Z F64: refresh started, request e9abc5cb-fecc-446d-b9c6-e232bcb9e05a
2026-11-20T06:27:08Z F64: refresh refreshed (Completed) 
2026-11-20T06:27:08Z F64: monitoring database Monitoring KQL database
2026-11-20T06:29:45Z F64: ExecutionMetrics event found
2026-11-20T06:29:47Z F64: model size in memory right after the refresh: 91.9 MB
```
