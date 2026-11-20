# Harness run 20261120T121211Z-v24-061e

- Task: refresh
- Variant: v24-bidirectional
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: dc5f699f-c35c-4644-a4fd-3cac480198e2
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 2,097 MB, Power Query 2,070 MB, duration 1 min, CPU 96 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request a63adeeb-0e42-4232-b5b4-c151987d1597, 2026-11-20T12:14:52.057 to 2026-11-20T12:15:56.697, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v24-bidirectional on F64 data-1m-v1: refreshed, peak 608 MB (2026-11-20T06:53:44Z).
  - Peak change: +1,489 MB (+244.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 2,097 MB vs 667 MB (+1,430 MB), Power Query 2,070 MB vs 592 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (70%); F16 5,054 MB: fits (41%); F32 10,174 MB: fits (21%); F64 25,534 MB: fits (8%); PPU 102,334 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    6b149a33-ae47-4ec8-8d3a-22bfd227d31b TabularSequencePoint         56.6     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         55.8    17.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         53.6    17.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         53.3    17.5 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.9    11.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.7     9.7       0
                                                                                       Commit          4.8     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.4     1.7       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.4     0.5       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.3     1.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.1     1.6  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          2.4     0.0       0
```

## Log

```
2026-11-20T12:14:16Z run 20261120T121211Z-v24-061e: variant=v24-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T12:14:26Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:14:29Z F64: v24-bidirectional is 6b149a33-ae47-4ec8-8d3a-22bfd227d31b, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:14:51Z F64: model size in memory before the refresh: 66.2 MB
2026-11-20T12:14:52Z F64: refresh started, request a63adeeb-0e42-4232-b5b4-c151987d1597
2026-11-20T12:16:02Z F64: refresh refreshed (Completed) 
2026-11-20T12:16:02Z F64: monitoring database Monitoring KQL database
2026-11-20T12:17:38Z F64: ExecutionMetrics event found
2026-11-20T12:18:28Z F64: model size in memory right after the refresh: 92.7 MB
```
