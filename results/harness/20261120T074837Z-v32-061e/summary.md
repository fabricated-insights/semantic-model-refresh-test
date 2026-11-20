# Harness run 20261120T074837Z-v32-061e

- Task: refresh
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 44e633fc-ca86-41e7-bc8a-295a8d336645
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 630 MB, Power Query 543 MB, duration 1 min, CPU 71 s, rows 24,570,331, model 221 MB (Backup step in SemanticModelLogs)
- Refresh request 55448d3c-a05d-4407-9bc7-019d501eb514, 2026-11-20T07:49:39.327 to 2026-11-20T07:50:27.067, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v32-calc-columns-aggregate on F64 data-1m-v1: refreshed, peak 1,459 MB (2026-11-19T23:47:39Z).
  - Peak change: -829 MB (-56.8%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 630 MB vs 716 MB (-86 MB), Power Query 543 MB vs 527 MB, model 221 MB vs 73 MB.
- Model size in memory when the full refresh started: 341 MB. The refresh may use the SKU maximum minus this: 25,259 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,725 MB: fits (23%); F16 4,779 MB: fits (13%); F32 9,899 MB: fits (6%); F64 25,259 MB: fits (2%); PPU 102,059 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    5c599620-07a4-4f5a-9f50-07e7127ad6ba TabularSequencePoint         40.9     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         37.0    12.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         35.6    12.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         35.5    12.0 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          2.9     4.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          2.7     2.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.3     1.0       0
                                            Sales.Line Share Of Customer       TabularRefresh          2.2     1.4       0
                                               Sales.Line Share Of Order       TabularRefresh          1.8     1.1       0
                                                       Sales.Order Total       TabularRefresh          1.6     1.1       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.4     0.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     1.0       0
```

## Log

```
2026-11-20T07:49:12Z run 20261120T074837Z-v32-061e: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T07:49:19Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:49:24Z F64: v32-calc-columns-aggregate is 5c599620-07a4-4f5a-9f50-07e7127ad6ba, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:49:39Z F64: model size in memory before the refresh: 341.3 MB
2026-11-20T07:49:39Z F64: refresh started, request 55448d3c-a05d-4407-9bc7-019d501eb514
2026-11-20T07:50:50Z F64: refresh refreshed (Completed) 
2026-11-20T07:50:50Z F64: monitoring database Monitoring KQL database
2026-11-20T07:52:25Z F64: ExecutionMetrics event found
2026-11-20T07:52:27Z F64: model size in memory right after the refresh: 367.9 MB
```
