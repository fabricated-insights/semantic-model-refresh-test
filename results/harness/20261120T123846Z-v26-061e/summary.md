# Harness run 20261120T123846Z-v26-061e

- Task: refresh
- Variant: v26-bad-dax
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1c6ecf89-5a23-4ff3-81bf-06b298422074
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 550 MB, Power Query 487 MB, duration 1 min, CPU 101 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 75b874d8-6bfb-47de-8bc8-95d17b5b6ccf, 2026-11-20T12:41:41.323 to 2026-11-20T12:42:46.6, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v26-bad-dax on F64 data-1m-v1: refreshed, peak 645 MB (2026-11-20T07:16:58Z).
  - Peak change: -95 MB (-14.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 550 MB vs 667 MB (-117 MB), Power Query 487 MB vs 592 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (18%); F16 5,054 MB: fits (11%); F32 10,174 MB: fits (5%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  59ff6c07-aebe-46b6-b8b5-9ad2216819f2 TabularSequencePoint         58.6     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         57.8    21.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         55.3    21.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         54.9    20.9 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.6    11.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.4     9.4       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.6     1.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.6     1.7       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.5     1.7  104990
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.4     0.0       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.1     0.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          1.9     0.0       0
```

## Log

```
2026-11-20T12:41:03Z run 20261120T123846Z-v26-061e: variant=v26-bad-dax data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T12:41:15Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:41:19Z F64: v26-bad-dax is 59ff6c07-aebe-46b6-b8b5-9ad2216819f2, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:41:41Z F64: model size in memory before the refresh: 66.2 MB
2026-11-20T12:41:41Z F64: refresh started, request 75b874d8-6bfb-47de-8bc8-95d17b5b6ccf
2026-11-20T12:42:51Z F64: refresh refreshed (Completed) 
2026-11-20T12:42:52Z F64: monitoring database Monitoring KQL database
2026-11-20T12:44:27Z F64: ExecutionMetrics event found
2026-11-20T12:44:29Z F64: model size in memory right after the refresh: 92.7 MB
```
