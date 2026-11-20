# Harness run 20261119T234251Z-v32-061e

- Task: refresh
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 9df2126a-5bb0-405f-b95f-d69be0416859
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,459 MB, Power Query 1,425 MB, duration 1 min, CPU 69 s, rows 24,570,331, model 221 MB (Backup step in SemanticModelLogs)
- Refresh request 499156be-c3a6-4ad1-bdde-959e1e2c8e96, 2026-11-19T23:43:50.407 to 2026-11-19T23:44:44.23, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v32-calc-columns-aggregate on F64 data-1m-v1: refreshed, peak 631 MB (2026-11-12T11:06:14Z).
  - Peak change: +828 MB (+131.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 1,459 MB vs 615 MB (+844 MB), Power Query 1,425 MB vs 335 MB, model 221 MB vs 73 MB.
- Model size in memory when the full refresh started: 341 MB. The refresh may use the SKU maximum minus this: 25,259 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,725 MB: fits (54%); F16 4,779 MB: fits (31%); F32 9,899 MB: fits (15%); F64 25,259 MB: fits (6%); PPU 102,059 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    5c599620-07a4-4f5a-9f50-07e7127ad6ba TabularSequencePoint         45.4     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         41.6    11.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.2    11.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.0    11.7 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          7.3     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          3.4     5.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          3.3     3.3       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.4     0.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.1     0.8       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          2.0     0.0       0
                                            Sales.Line Share Of Customer       TabularRefresh          1.9     1.3       0
                                                       Sales.Order Total       TabularRefresh          1.7     1.2       0
```

## Log

```
2026-11-19T23:43:24Z run 20261119T234251Z-v32-061e: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T23:43:33Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:43:38Z F64: v32-calc-columns-aggregate is 5c599620-07a4-4f5a-9f50-07e7127ad6ba, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:43:50Z F64: model size in memory before the refresh: 341.3 MB
2026-11-19T23:43:50Z F64: refresh started, request 499156be-c3a6-4ad1-bdde-959e1e2c8e96
2026-11-19T23:45:01Z F64: refresh refreshed (Completed) 
2026-11-19T23:45:01Z F64: monitoring database Monitoring KQL database
2026-11-19T23:47:37Z F64: ExecutionMetrics event found
2026-11-19T23:47:39Z F64: model size in memory right after the refresh: 367.9 MB
```
