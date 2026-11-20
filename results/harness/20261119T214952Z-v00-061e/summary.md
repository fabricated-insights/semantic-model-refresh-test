# Harness run 20261119T214952Z-v00-061e

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 4f739911-73b3-4154-a919-e1610e951408
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 615 MB, Power Query 335 MB, duration 1 min, CPU 56 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 1579bf1b-9dbe-41d8-81bd-5e1e5313597c, 2026-11-19T21:53:23.333 to 2026-11-19T21:54:04.073, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64 data-1m-v1: refreshed, peak 602 MB (2026-11-13T20:33:20Z).
  - Peak change: +13 MB (+2.2%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (21%); F16 5,054 MB: fits (12%); F32 10,174 MB: fits (6%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    aee1f825-0998-43ef-9b7c-fa80d819f127 TabularSequencePoint         36.4     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         36.1    11.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         32.9    11.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         32.7    10.9 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.0     5.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.9     4.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.6     0.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.4     0.3       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          3.0     0.0       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          3.0     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          3.0     0.0       0
                                                                                       Commit          2.5     0.0       0
```

## Log

```
2026-11-19T21:52:39Z run 20261119T214952Z-v00-061e: variant=v00-baseline data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T21:52:49Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T21:52:51Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T21:53:20Z F64: model size in memory before the refresh: 66.2 MB
2026-11-19T21:53:23Z F64: refresh started, request 1579bf1b-9dbe-41d8-81bd-5e1e5313597c
2026-11-19T21:54:08Z F64: refresh refreshed (Completed) 
2026-11-19T21:54:09Z F64: monitoring database Monitoring KQL database
2026-11-19T21:56:45Z F64: ExecutionMetrics event found
2026-11-19T21:56:47Z F64: model size in memory right after the refresh: 92.7 MB
```
