# Harness run 20261120T104014Z-v99m-061e

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 58d45d62-8f07-4019-b0f7-88743c29d368
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 625 MB, Power Query 439 MB, duration 1 min, CPU 118 s, rows 21,583,972, model 102 MB (Backup step in SemanticModelLogs)
- Refresh request abc7bbe9-7718-4e7a-b2c0-5bb456475249, 2026-11-20T10:41:47.453 to 2026-11-20T10:43:04.82, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99m-baseline-pq on F64 data-1m-v1: refreshed, peak 625 MB (2026-11-20T05:01:28Z).
  - Peak change: +0 MB (+0.0%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 625 MB vs 716 MB (-91 MB), Power Query 439 MB vs 527 MB, model 102 MB vs 73 MB.
- Model size in memory when the full refresh started: 101 MB. The refresh may use the SKU maximum minus this: 25,499 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,965 MB: fits (21%); F16 5,019 MB: fits (12%); F32 10,139 MB: fits (6%); F64 25,499 MB: fits (2%); PPU 102,299 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    653e733e-f558-46e8-a7e4-42a4c2c8fddd TabularSequencePoint         68.7     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         60.2    21.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         57.9    21.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         57.6    21.0 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.6     9.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.3     7.3       0
                                                  Sales.Sales Line Label       TabularRefresh          6.0     5.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.3     1.8       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.2     0.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.8     1.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.7     1.7  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          2.3     0.0       0
```

## Log

```
2026-11-20T10:41:16Z run 20261120T104014Z-v99m-061e: variant=v99m-baseline-pq data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T10:41:27Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T10:41:31Z F64: v99m-baseline-pq is 653e733e-f558-46e8-a7e4-42a4c2c8fddd, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T10:41:47Z F64: model size in memory before the refresh: 101.3 MB
2026-11-20T10:41:47Z F64: refresh started, request abc7bbe9-7718-4e7a-b2c0-5bb456475249
2026-11-20T10:43:28Z F64: refresh refreshed (Completed) 
2026-11-20T10:43:28Z F64: monitoring database Monitoring KQL database
2026-11-20T10:45:04Z F64: ExecutionMetrics event found
2026-11-20T10:45:22Z F64: model size in memory right after the refresh: 136.1 MB
```
