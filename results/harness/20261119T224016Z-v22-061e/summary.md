# Harness run 20261119T224016Z-v22-061e

- Task: refresh
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 95ca72e2-09a0-4bec-bb3d-d78431717c3d
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 622 MB, Power Query 272 MB, duration 1 min, CPU 66 s, rows 21,353,868, model 101 MB (Backup step in SemanticModelLogs)
- Refresh request bb4aae4c-6369-48b3-9e16-37885e2d155b, 2026-11-19T22:41:16.237 to 2026-11-19T22:42:02.787, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v22-dax-calc-columns on F64 data-1m-v1: refreshed, peak 794 MB (2026-11-13T17:42:19Z).
  - Peak change: -172 MB (-21.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 622 MB vs 615 MB (+7 MB), Power Query 272 MB vs 335 MB, model 101 MB vs 73 MB.
- Model size in memory when the full refresh started: 98 MB. The refresh may use the SKU maximum minus this: 25,502 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,968 MB: fits (21%); F16 5,022 MB: fits (12%); F32 10,142 MB: fits (6%); F64 25,502 MB: fits (2%); PPU 102,302 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    683e80a5-7d57-493c-a708-3a0b8ce5350c TabularSequencePoint         40.7     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         36.3    11.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.7    11.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.5    10.9 2349091
                                                                                       Commit          3.4     0.0       0
                                                  Sales.Sales Line Label       TabularRefresh          3.3     3.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.2     0.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          3.1     3.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          2.9     2.9       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          2.6     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          2.5     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.3     0.4       0
```

## Log

```
2026-11-19T22:40:51Z run 20261119T224016Z-v22-061e: variant=v22-dax-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T22:41:00Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:41:03Z F64: v22-dax-calc-columns is 683e80a5-7d57-493c-a708-3a0b8ce5350c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:41:16Z F64: model size in memory before the refresh: 97.8 MB
2026-11-19T22:41:16Z F64: refresh started, request bb4aae4c-6369-48b3-9e16-37885e2d155b
2026-11-19T22:42:26Z F64: refresh refreshed (Completed) 
2026-11-19T22:42:26Z F64: monitoring database Monitoring KQL database
2026-11-19T22:45:03Z F64: ExecutionMetrics event found
2026-11-19T22:45:05Z F64: model size in memory right after the refresh: 132.6 MB
```
