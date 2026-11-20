# Harness run 20261120T142307Z-v99m-e764

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: c7cdca61-8944-4b22-a75b-ec9c88a1de21
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 521 MB, Power Query 470 MB, duration 1 min, CPU 149 s, rows 21,583,972, model 102 MB (Backup step in SemanticModelLogs)
- Refresh request 282c894c-df6a-401b-bbf9-cbe4cb68eb08, 2026-11-20T14:26:08.17 to 2026-11-20T14:27:45.543, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99m-baseline-pq on F64-NE data-1m-v1: refreshed, peak 580 MB (2026-11-20T12:38:30Z).
  - Peak change: -59 MB (-10.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T14:22:30Z): peak 521 MB vs 949 MB (-428 MB), Power Query 470 MB vs 904 MB, model 102 MB vs 72 MB.
- Model size in memory when the full refresh started: 101 MB. The refresh may use the SKU maximum minus this: 25,499 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,965 MB: fits (18%); F16 5,019 MB: fits (10%); F32 10,139 MB: fits (5%); F64 25,499 MB: fits (2%); PPU 102,299 MB: fits (1%); F2-csv 2,965 MB: fits (18%); F2-sql 2,965 MB: fits (18%); F64-NE 25,499 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    59d3a17d-96e6-4e9b-af01-47a2b7340201 TabularSequencePoint         87.2     0.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         79.5    21.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         74.5    21.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         74.1    21.4 2349091
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          8.3     1.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.5     9.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.3     7.3       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          6.0     0.6       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          5.9     0.2       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          5.9     0.2       0
                                                  Sales.Sales Line Label       TabularRefresh          5.6     5.5       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          5.4     0.0       0
```

## Log

```
2026-11-20T14:25:33Z run 20261120T142307Z-v99m-e764: variant=v99m-baseline-pq data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T14:25:40Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T14:25:44Z F64-NE: v99m-baseline-pq is 59d3a17d-96e6-4e9b-af01-47a2b7340201, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T14:25:46Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T14:26:08Z F64-NE: model size in memory before the refresh: 101.3 MB
2026-11-20T14:26:08Z F64-NE: refresh started, request 282c894c-df6a-401b-bbf9-cbe4cb68eb08
2026-11-20T14:27:48Z F64-NE: refresh refreshed (Completed) 
2026-11-20T14:27:48Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T14:28:38Z F64-NE: ExecutionMetrics event found
2026-11-20T14:29:12Z F64-NE: model size in memory right after the refresh: 136.1 MB
```
