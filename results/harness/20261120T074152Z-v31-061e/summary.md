# Harness run 20261120T074152Z-v31-061e

- Task: refresh
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1beea314-6237-458d-b66f-630352bf040a
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 990 MB, Power Query 821 MB, duration 1 min, CPU 160 s, rows 77,732,052, model 223 MB (Backup step in SemanticModelLogs)
- Refresh request b5479d61-2f16-4be5-bc91-fcf3ca4e38c0, 2026-11-20T07:44:40.98 to 2026-11-20T07:46:22.587, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v31-calc-columns-row on F64 data-1m-v1: refreshed, peak 890 MB (2026-11-19T23:42:23Z).
  - Peak change: +100 MB (+11.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 990 MB vs 716 MB (+274 MB), Power Query 821 MB vs 527 MB, model 223 MB vs 73 MB.
- Model size in memory when the full refresh started: 234 MB. The refresh may use the SKU maximum minus this: 25,366 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,832 MB: fits (35%); F16 4,886 MB: fits (20%); F32 10,006 MB: fits (10%); F64 25,366 MB: fits (4%); PPU 102,166 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    3c4e1e09-8d9a-4ac4-b01e-178c2d6bae18 TabularSequencePoint         81.0     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         60.9    24.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         59.4    24.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         58.3    24.4 2349091
                                                    Sales.Order Line Key       TabularRefresh         14.2     4.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.3    15.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.9    10.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          8.1     0.6       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          7.3     0.1       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          7.2     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          7.2     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.6     1.9       0
```

## Log

```
2026-11-20T07:44:05Z run 20261120T074152Z-v31-061e: variant=v31-calc-columns-row data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T07:44:14Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:44:20Z F64: v31-calc-columns-row is 3c4e1e09-8d9a-4ac4-b01e-178c2d6bae18, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:44:40Z F64: model size in memory before the refresh: 233.5 MB
2026-11-20T07:44:41Z F64: refresh started, request b5479d61-2f16-4be5-bc91-fcf3ca4e38c0
2026-11-20T07:46:51Z F64: refresh refreshed (Completed) 
2026-11-20T07:46:51Z F64: monitoring database Monitoring KQL database
2026-11-20T07:47:42Z F64: ExecutionMetrics event found
2026-11-20T07:48:00Z F64: model size in memory right after the refresh: 316.8 MB
```
