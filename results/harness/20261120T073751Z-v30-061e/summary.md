# Harness run 20261120T073751Z-v30-061e

- Task: refresh
- Variant: v30-double-instead-of-fixed
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 2712bb06-5012-4ec3-932f-6d0dd1587ecb
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 614 MB, Power Query 334 MB, duration 1 min, CPU 53 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request c0464cf4-9cc4-4c6b-b51c-8e8ff663123c, 2026-11-20T07:38:53.64 to 2026-11-20T07:39:30.183, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v30-double-instead-of-fixed on F64 data-1m-v1: refreshed, peak 677 MB (2026-11-19T23:38:05Z).
  - Peak change: -63 MB (-9.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 614 MB vs 716 MB (-102 MB), Power Query 334 MB vs 527 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (20%); F16 5,054 MB: fits (12%); F32 10,174 MB: fits (6%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    82a0b18f-7fcc-4d91-84c8-ad3d394d13f0 TabularSequencePoint         30.9     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         30.5    11.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         29.3    11.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         29.0    11.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.3     6.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.2     5.1       0
                                                                                       Commit          3.0     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.4     0.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.5     0.8  104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.5     0.8       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.2     0.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.1     0.0       0
```

## Log

```
2026-11-20T07:38:28Z run 20261120T073751Z-v30-061e: variant=v30-double-instead-of-fixed data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T07:38:33Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:38:37Z F64: v30-double-instead-of-fixed is 82a0b18f-7fcc-4d91-84c8-ad3d394d13f0, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:38:53Z F64: model size in memory before the refresh: 66.4 MB
2026-11-20T07:38:53Z F64: refresh started, request c0464cf4-9cc4-4c6b-b51c-8e8ff663123c
2026-11-20T07:39:39Z F64: refresh refreshed (Completed) 
2026-11-20T07:39:39Z F64: monitoring database Monitoring KQL database
2026-11-20T07:41:15Z F64: ExecutionMetrics event found
2026-11-20T07:41:17Z F64: model size in memory right after the refresh: 92.9 MB
```
