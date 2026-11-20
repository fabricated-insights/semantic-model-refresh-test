# Harness run 20261120T130246Z-v30-061e

- Task: refresh
- Variant: v30-double-instead-of-fixed
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 5ca98f42-b2f4-4511-bceb-88a81fad4888
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 683 MB, Power Query 411 MB, duration 1 min, CPU 55 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request b3b41627-2a9f-4065-9030-9096f15c13a1, 2026-11-20T13:06:58.833 to 2026-11-20T13:07:38.53, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v30-double-instead-of-fixed on F64 data-1m-v1: refreshed, peak 614 MB (2026-11-20T07:41:17Z).
  - Peak change: +69 MB (+11.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 683 MB vs 667 MB (+16 MB), Power Query 411 MB vs 592 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (23%); F16 5,054 MB: fits (14%); F32 10,174 MB: fits (7%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    82a0b18f-7fcc-4d91-84c8-ad3d394d13f0 TabularSequencePoint         32.3     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         31.8    11.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         30.7    11.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         30.2    11.5 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.3     7.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.2     6.1       0
                                                                                       Commit          4.3     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.6     0.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.5     0.8       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          2.1     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.7     0.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.6     0.7  104990
```

## Log

```
2026-11-20T13:06:22Z run 20261120T130246Z-v30-061e: variant=v30-double-instead-of-fixed data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T13:06:30Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:06:33Z F64: v30-double-instead-of-fixed is 82a0b18f-7fcc-4d91-84c8-ad3d394d13f0, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:06:58Z F64: model size in memory before the refresh: 66.4 MB
2026-11-20T13:06:58Z F64: refresh started, request b3b41627-2a9f-4065-9030-9096f15c13a1
2026-11-20T13:07:44Z F64: refresh refreshed (Completed) 
2026-11-20T13:07:44Z F64: monitoring database Monitoring KQL database
2026-11-20T13:10:21Z F64: ExecutionMetrics event found
2026-11-20T13:10:23Z F64: model size in memory right after the refresh: 92.9 MB
```
