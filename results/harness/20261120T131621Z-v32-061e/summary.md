# Harness run 20261120T131621Z-v32-061e

- Task: refresh
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1baacb3e-1831-48bc-ba14-18c1cd7e656e
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 803 MB, Power Query 673 MB, duration 1 min, CPU 130 s, rows 24,570,331, model 221 MB (Backup step in SemanticModelLogs)
- Refresh request 2ccd7af3-6c9f-4026-b59e-ff848b799899, 2026-11-20T13:19:30.913 to 2026-11-20T13:21:02.647, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v32-calc-columns-aggregate on F64 data-1m-v1: refreshed, peak 630 MB (2026-11-20T07:52:27Z).
  - Peak change: +173 MB (+27.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 803 MB vs 667 MB (+136 MB), Power Query 673 MB vs 592 MB, model 221 MB vs 73 MB.
- Model size in memory when the full refresh started: 341 MB. The refresh may use the SKU maximum minus this: 25,259 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,725 MB: fits (29%); F16 4,779 MB: fits (17%); F32 9,899 MB: fits (8%); F64 25,259 MB: fits (3%); PPU 102,059 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  5c599620-07a4-4f5a-9f50-07e7127ad6ba TabularSequencePoint         76.3     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         68.8    22.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         60.8    22.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         60.5    22.0 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.1    11.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.8     8.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          7.8     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.4     1.8       0
                          Sales.Line Share Of Customer       TabularRefresh          4.0     2.6       0
                                     Sales.Order Total       TabularRefresh          3.1     2.0       0
                             Sales.Line Share Of Order       TabularRefresh          3.0     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.9     1.8       0
```

## Log

```
2026-11-20T13:18:50Z run 20261120T131621Z-v32-061e: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T13:19:00Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:19:05Z F64: v32-calc-columns-aggregate is 5c599620-07a4-4f5a-9f50-07e7127ad6ba, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:19:30Z F64: model size in memory before the refresh: 341.3 MB
2026-11-20T13:19:31Z F64: refresh started, request 2ccd7af3-6c9f-4026-b59e-ff848b799899
2026-11-20T13:21:11Z F64: refresh refreshed (Completed) 
2026-11-20T13:21:11Z F64: monitoring database Monitoring KQL database
2026-11-20T13:23:49Z F64: ExecutionMetrics event found
2026-11-20T13:23:53Z F64: model size in memory right after the refresh: 367.9 MB
```
