# Harness run 20261120T064731Z-v24-061e

- Task: refresh
- Variant: v24-bidirectional
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 8c2019a8-8e5c-43ba-b509-29bc1af0a5e4
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 608 MB, Power Query 334 MB, duration 1 min, CPU 58 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 757bc0d0-e982-45aa-9f2e-92d066fcb1e9, 2026-11-20T06:50:20.14 to 2026-11-20T06:51:01.383, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v24-bidirectional on F64 data-1m-v1: refreshed, peak 706 MB (2026-11-19T22:56:01Z).
  - Peak change: -98 MB (-13.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 608 MB vs 716 MB (-108 MB), Power Query 334 MB vs 527 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (20%); F16 5,054 MB: fits (12%); F32 10,174 MB: fits (6%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    6b149a33-ae47-4ec8-8d3a-22bfd227d31b TabularSequencePoint         35.8     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         35.4    11.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.2    11.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.0    10.9 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.0     5.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.8     4.8       0
                                                                                       Commit          2.8     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.7     1.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.7     0.9  104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.7     0.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.2     0.4       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          1.1     0.1       0
```

## Log

```
2026-11-20T06:49:46Z run 20261120T064731Z-v24-061e: variant=v24-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T06:49:54Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T06:49:58Z F64: v24-bidirectional is 6b149a33-ae47-4ec8-8d3a-22bfd227d31b, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T06:50:20Z F64: model size in memory before the refresh: 66.2 MB
2026-11-20T06:50:20Z F64: refresh started, request 757bc0d0-e982-45aa-9f2e-92d066fcb1e9
2026-11-20T06:51:05Z F64: refresh refreshed (Completed) 
2026-11-20T06:51:05Z F64: monitoring database Monitoring KQL database
2026-11-20T06:53:42Z F64: ExecutionMetrics event found
2026-11-20T06:53:44Z F64: model size in memory right after the refresh: 92.7 MB
```
