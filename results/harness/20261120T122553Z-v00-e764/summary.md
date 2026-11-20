# Harness run 20261120T122553Z-v00-e764

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 82a7a98f-11de-402f-8a54-54c84bef02eb
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 623 MB, Power Query 583 MB, duration 1 min, CPU 130 s, rows 2,561,140, model 72 MB (Backup step in SemanticModelLogs)
- Refresh request c0d010a6-098a-403b-bc42-11507dee424d, 2026-11-20T12:27:16.293 to 2026-11-20T12:28:53.803, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v00-baseline on F64-NE data-1m-v1.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%); F2-csv 3,066 MB: fits (20%); F2-sql 3,066 MB: fits (20%); F64-NE 25,600 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    19cc20ca-dba3-4570-95d8-761af4ab7063 TabularSequencePoint         89.3     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         88.7    19.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         78.8    19.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         78.3    19.3 2349091
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         18.2     1.6       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh         16.3     0.7       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh         15.8     0.1       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh         15.7     0.1       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh         15.7     0.1       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql         14.9     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.5    11.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.4    10.3       0
```

## Log

```
2026-11-20T12:26:52Z run 20261120T122553Z-v00-e764: variant=v00-baseline data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T12:26:57Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T12:26:59Z F64-NE: v00-baseline is 19cc20ca-dba3-4570-95d8-761af4ab7063, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T12:27:01Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T12:27:16Z F64-NE: model size in memory before the refresh: 0.0 MB
2026-11-20T12:27:16Z F64-NE: refresh started, request c0d010a6-098a-403b-bc42-11507dee424d
2026-11-20T12:28:56Z F64-NE: refresh refreshed (Completed) 
2026-11-20T12:28:57Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T12:30:32Z F64-NE: ExecutionMetrics event found
2026-11-20T12:30:34Z F64-NE: model size in memory right after the refresh: 92.1 MB
```
