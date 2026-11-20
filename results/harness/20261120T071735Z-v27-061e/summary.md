# Harness run 20261120T071735Z-v27-061e

- Task: refresh
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ff2ac73e-4bcc-4f8d-9df8-9ed30fefc8b2
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 550 MB, Power Query 459 MB, duration 1 min, CPU 104 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request abfefcb2-fa97-4286-8e5e-10931f012629, 2026-11-20T07:20:26.963 to 2026-11-20T07:21:36.11, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v27-high-cardinality-visuals on F64 data-1m-v1: refreshed, peak 569 MB (2026-11-19T23:23:01Z).
  - Peak change: -19 MB (-3.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 550 MB vs 716 MB (-166 MB), Power Query 459 MB vs 527 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (18%); F16 5,054 MB: fits (11%); F32 10,174 MB: fits (5%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    65980d29-ea56-4b4c-9a03-d5c7d50cb6db TabularSequencePoint         60.8     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         60.0    18.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         57.2    18.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         56.8    18.8 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.2    11.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.1    10.1       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.1     1.7       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.1     0.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.7     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.7     1.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.6     1.6  104990
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.5     0.1       0
```

## Log

```
2026-11-20T07:19:52Z run 20261120T071735Z-v27-061e: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T07:19:59Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:20:04Z F64: v27-high-cardinality-visuals is 65980d29-ea56-4b4c-9a03-d5c7d50cb6db, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:20:26Z F64: model size in memory before the refresh: 66.2 MB
2026-11-20T07:20:27Z F64: refresh started, request abfefcb2-fa97-4286-8e5e-10931f012629
2026-11-20T07:21:37Z F64: refresh refreshed (Completed) 
2026-11-20T07:21:37Z F64: monitoring database Monitoring KQL database
2026-11-20T07:23:13Z F64: ExecutionMetrics event found
2026-11-20T07:23:31Z F64: model size in memory right after the refresh: 92.7 MB
```
