# Harness run 20261120T162813Z-v99p-061e

- Task: refresh
- Variant: v99p-high-cardinality
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ccc37fd0-5273-42ab-9eb5-c338fbd67dbb
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 685 MB, Power Query 271 MB, duration 1 min, CPU 75 s, rows 21,609,543, model 175 MB (Backup step in SemanticModelLogs)
- Refresh request a5131ab1-9946-4910-9730-84e6d4c12a1c, 2026-11-20T16:29:22 to 2026-11-20T16:30:15.803, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99p-high-cardinality on F64 data-1m-v1: refreshed, peak 1,179 MB (2026-11-20T11:15:25Z).
  - Peak change: -494 MB (-41.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 685 MB vs 667 MB (+18 MB), Power Query 271 MB vs 592 MB, model 175 MB vs 73 MB.
- Model size in memory when the full refresh started: 174 MB. The refresh may use the SKU maximum minus this: 25,426 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,892 MB: fits (24%); F16 4,946 MB: fits (14%); F32 10,066 MB: fits (7%); F64 25,426 MB: fits (3%); PPU 102,226 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    5369ab57-f76f-43d8-9a2b-7448b05f00d8 TabularSequencePoint         45.9     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         41.0    12.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         39.3    12.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         39.1    12.7 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          3.7     5.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          3.6     3.6       0
                                                  Sales.Sales Line Label       TabularRefresh          3.3     3.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.9     1.0       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          1.9     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          1.8     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.8     0.3       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          1.6     0.0       0
```

## Log

```
2026-11-20T16:28:52Z run 20261120T162813Z-v99p-061e: variant=v99p-high-cardinality data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T16:29:02Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T16:29:06Z F64: v99p-high-cardinality is 5369ab57-f76f-43d8-9a2b-7448b05f00d8, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T16:29:21Z F64: model size in memory before the refresh: 174.2 MB
2026-11-20T16:29:22Z F64: refresh started, request a5131ab1-9946-4910-9730-84e6d4c12a1c
2026-11-20T16:30:32Z F64: refresh refreshed (Completed) 
2026-11-20T16:30:32Z F64: monitoring database Monitoring KQL database
2026-11-20T16:32:07Z F64: ExecutionMetrics event found
2026-11-20T16:32:09Z F64: model size in memory right after the refresh: 209.0 MB
```
