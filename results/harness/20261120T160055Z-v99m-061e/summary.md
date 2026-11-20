# Harness run 20261120T160055Z-v99m-061e

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 77fac262-6b4c-4da2-8134-b8f2e32f40c4
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 801 MB, Power Query 722 MB, duration 1 min, CPU 132 s, rows 21,583,972, model 102 MB (Backup step in SemanticModelLogs)
- Refresh request fdc05379-71d2-48ab-a38b-539ab8b8a75a, 2026-11-20T16:03:56.453 to 2026-11-20T16:05:22.637, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99m-baseline-pq on F64 data-1m-v1: refreshed, peak 625 MB (2026-11-20T10:45:21Z).
  - Peak change: +176 MB (+28.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 801 MB vs 667 MB (+134 MB), Power Query 722 MB vs 592 MB, model 102 MB vs 73 MB.
- Model size in memory when the full refresh started: 101 MB. The refresh may use the SKU maximum minus this: 25,499 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,965 MB: fits (27%); F16 5,019 MB: fits (16%); F32 10,139 MB: fits (8%); F64 25,499 MB: fits (3%); PPU 102,299 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    653e733e-f558-46e8-a7e4-42a4c2c8fddd TabularSequencePoint         75.8     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         67.1    22.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         64.9    22.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         64.4    22.6 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.5    10.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.2     8.2       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          7.9     0.1       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          7.7     0.0       0
                                                  Sales.Sales Line Label       TabularRefresh          6.0     5.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.6     2.2       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.8     0.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.6     2.1       0
```

## Log

```
2026-11-20T16:03:16Z run 20261120T160055Z-v99m-061e: variant=v99m-baseline-pq data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T16:03:28Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T16:03:33Z F64: v99m-baseline-pq is 653e733e-f558-46e8-a7e4-42a4c2c8fddd, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T16:03:56Z F64: model size in memory before the refresh: 101.3 MB
2026-11-20T16:03:56Z F64: refresh started, request fdc05379-71d2-48ab-a38b-539ab8b8a75a
2026-11-20T16:05:37Z F64: refresh refreshed (Completed) 
2026-11-20T16:05:37Z F64: monitoring database Monitoring KQL database
2026-11-20T16:07:12Z F64: ExecutionMetrics event found
2026-11-20T16:07:14Z F64: model size in memory right after the refresh: 136.1 MB
```
