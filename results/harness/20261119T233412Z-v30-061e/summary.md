# Harness run 20261119T233412Z-v30-061e

- Task: refresh
- Variant: v30-double-instead-of-fixed
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 0e6b0b32-d74b-47b8-8f37-878e504f4a73
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 677 MB, Power Query 397 MB, duration 1 min, CPU 92 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 4f375212-c2a3-411a-ad36-8d93931f22b6, 2026-11-19T23:35:16.74 to 2026-11-19T23:36:19.54, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v30-double-instead-of-fixed on F64 data-1m-v1: refreshed, peak 550 MB (2026-11-12T08:28:16Z).
  - Peak change: +127 MB (+23.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 677 MB vs 615 MB (+62 MB), Power Query 397 MB vs 335 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (23%); F16 5,054 MB: fits (13%); F32 10,174 MB: fits (7%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    82a0b18f-7fcc-4d91-84c8-ad3d394d13f0 TabularSequencePoint         52.9     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         52.2    18.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         49.6    18.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         48.7    18.4 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.6    11.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.4    10.4       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.5     1.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     1.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.9     1.8  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.6     0.7       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          2.5     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          2.4     0.0       0
```

## Log

```
2026-11-19T23:34:50Z run 20261119T233412Z-v30-061e: variant=v30-double-instead-of-fixed data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T23:34:59Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:35:03Z F64: v30-double-instead-of-fixed is 82a0b18f-7fcc-4d91-84c8-ad3d394d13f0, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:35:16Z F64: model size in memory before the refresh: 66.4 MB
2026-11-19T23:35:16Z F64: refresh started, request 4f375212-c2a3-411a-ad36-8d93931f22b6
2026-11-19T23:36:28Z F64: refresh refreshed (Completed) 
2026-11-19T23:36:28Z F64: monitoring database Monitoring KQL database
2026-11-19T23:38:03Z F64: ExecutionMetrics event found
2026-11-19T23:38:06Z F64: model size in memory right after the refresh: 92.9 MB
```
