# Harness run 20261120T141522Z-v00-e764

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 0e3c6717-0255-458d-9f9f-6cf580b9f81c
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 949 MB, Power Query 904 MB, duration 2 min, CPU 157 s, rows 2,561,140, model 72 MB (Backup step in SemanticModelLogs)
- Refresh request 19162f74-3901-4c19-94f8-bc8492d037d5, 2026-11-20T14:18:42.23 to 2026-11-20T14:20:33.543, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64-NE data-1m-v1: refreshed, peak 623 MB (2026-11-20T12:30:33Z).
  - Peak change: +326 MB (+52.3%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (32%); F16 5,054 MB: fits (19%); F32 10,174 MB: fits (9%); F64 25,534 MB: fits (4%); PPU 102,334 MB: fits (1%); F2-csv 3,000 MB: fits (32%); F2-sql 3,000 MB: fits (32%); F64-NE 25,534 MB: fits (4%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    19cc20ca-dba3-4570-95d8-761af4ab7063 TabularSequencePoint        104.2     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        103.4    25.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        101.7    25.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        101.1    25.0 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         13.7    13.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         13.3    12.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.6     2.1       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          4.9     0.7       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          4.9     0.1       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          4.4     0.0       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          4.2     0.0       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          4.2     0.2       0
```

## Log

```
2026-11-20T14:18:03Z run 20261120T141522Z-v00-e764: variant=v00-baseline data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T14:18:09Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T14:18:12Z F64-NE: v00-baseline is 19cc20ca-dba3-4570-95d8-761af4ab7063, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T14:18:13Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T14:18:42Z F64-NE: model size in memory before the refresh: 65.5 MB
2026-11-20T14:18:42Z F64-NE: refresh started, request 19162f74-3901-4c19-94f8-bc8492d037d5
2026-11-20T14:20:52Z F64-NE: refresh refreshed (Completed) 
2026-11-20T14:20:53Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T14:22:28Z F64-NE: ExecutionMetrics event found
2026-11-20T14:22:30Z F64-NE: model size in memory right after the refresh: 92.1 MB
```
