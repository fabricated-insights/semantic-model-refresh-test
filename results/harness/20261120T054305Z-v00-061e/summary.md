# Harness run 20261120T054305Z-v00-061e

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 8e399fa8-ab3b-496d-92c7-fad8c51baf30
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 716 MB, Power Query 527 MB, duration 1 min, CPU 104 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 0271725d-9b33-4d93-ac47-11d8ba7b887b, 2026-11-20T05:46:06.533 to 2026-11-20T05:47:13.823, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64 data-1m-v1: refreshed, peak 615 MB (2026-11-19T21:56:46Z).
  - Peak change: +101 MB (+16.4%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (24%); F16 5,054 MB: fits (14%); F32 10,174 MB: fits (7%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    aee1f825-0998-43ef-9b7c-fa80d819f127 TabularSequencePoint         60.7     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         60.0    20.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         58.3    20.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         57.9    20.3 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.4    12.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.2    10.2       0
                                                                                       Commit          4.9     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.3     1.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     1.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.9     1.8  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.1     0.6       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          1.8     0.1       0
```

## Log

```
2026-11-20T05:45:32Z run 20261120T054305Z-v00-061e: variant=v00-baseline data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T05:45:42Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T05:45:45Z F64: v00-baseline is aee1f825-0998-43ef-9b7c-fa80d819f127, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T05:46:06Z F64: model size in memory before the refresh: 66.2 MB
2026-11-20T05:46:06Z F64: refresh started, request 0271725d-9b33-4d93-ac47-11d8ba7b887b
2026-11-20T05:47:17Z F64: refresh refreshed (Completed) 
2026-11-20T05:47:17Z F64: monitoring database Monitoring KQL database
2026-11-20T05:49:54Z F64: ExecutionMetrics event found
2026-11-20T05:49:56Z F64: model size in memory right after the refresh: 92.7 MB
```
