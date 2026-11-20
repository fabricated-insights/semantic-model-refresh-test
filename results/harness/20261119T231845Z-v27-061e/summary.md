# Harness run 20261119T231845Z-v27-061e

- Task: refresh
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 2e44afc7-11c6-49d6-ab7c-d9c5d60ddbcb
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 569 MB, Power Query 530 MB, duration 1 min, CPU 57 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 68c05630-206a-4e60-8395-a697c7d0e51a, 2026-11-19T23:19:38.227 to 2026-11-19T23:20:23.367, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v27-high-cardinality-visuals on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 569 MB vs 615 MB (-46 MB), Power Query 530 MB vs 335 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (19%); F16 5,120 MB: fits (11%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    65980d29-ea56-4b4c-9a03-d5c7d50cb6db TabularSequencePoint         40.1     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         39.8    10.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.1    10.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         33.9    10.3 2349091
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.0     0.8       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          5.9     0.3       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          5.7     0.1       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          5.6     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          5.5     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          5.5     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          5.4     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          5.4     0.0       0
```

## Log

```
2026-11-19T23:19:13Z run 20261119T231845Z-v27-061e: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T23:19:23Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:19:25Z F64: v27-high-cardinality-visuals is 65980d29-ea56-4b4c-9a03-d5c7d50cb6db, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:19:38Z F64: model size in memory before the refresh: 0.0 MB
2026-11-19T23:19:38Z F64: refresh started, request 68c05630-206a-4e60-8395-a697c7d0e51a
2026-11-19T23:20:23Z F64: refresh refreshed (Completed) 
2026-11-19T23:20:23Z F64: monitoring database Monitoring KQL database
2026-11-19T23:23:00Z F64: ExecutionMetrics event found
2026-11-19T23:23:02Z F64: model size in memory right after the refresh: 92.7 MB
```
