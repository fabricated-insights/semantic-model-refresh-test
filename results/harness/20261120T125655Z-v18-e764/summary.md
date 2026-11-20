# Harness run 20261120T125655Z-v18-e764

- Task: refresh
- Variant: v18-pq-10m-summary
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 63191bd4-0dc7-49b6-bf26-ecd23d0f59e5
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 587 MB, Power Query 569 MB, duration 1 min, CPU 129 s, rows 2,561,730, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 949d4f3e-d925-4a9d-9b22-cef97bbdf997, 2026-11-20T12:59:45.767 to 2026-11-20T13:01:11.35, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v18-pq-10m-summary on F64-NE data-1m-v1.
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T12:30:33Z): peak 587 MB vs 623 MB (-36 MB), Power Query 569 MB vs 583 MB, model 73 MB vs 72 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (19%); F16 5,120 MB: fits (11%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%); F2-csv 3,066 MB: fits (19%); F2-sql 3,066 MB: fits (19%); F64-NE 25,600 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    bc6f6aac-ed6e-4b37-9b1e-d5afc029b466 TabularSequencePoint         78.5     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         77.8    19.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         72.2    18.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         71.5    18.7 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         12.5    13.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         12.3    12.2       0
                                   Store Year Summary.Store Year Summary       TabularRefresh         10.5     0.1       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          8.7     1.7       0
                                   Store Year Summary.Store Year Summary           ExecuteSql          6.5     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          6.4     0.7       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          5.8     0.1       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          5.7     0.1       0
```

## Log

```
2026-11-20T12:59:09Z run 20261120T125655Z-v18-e764: variant=v18-pq-10m-summary data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T12:59:20Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T12:59:22Z F64-NE: v18-pq-10m-summary is bc6f6aac-ed6e-4b37-9b1e-d5afc029b466, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T12:59:24Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T12:59:45Z F64-NE: model size in memory before the refresh: 0.0 MB
2026-11-20T12:59:45Z F64-NE: refresh started, request 949d4f3e-d925-4a9d-9b22-cef97bbdf997
2026-11-20T13:01:26Z F64-NE: refresh refreshed (Completed) 
2026-11-20T13:01:26Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T13:03:02Z F64-NE: ExecutionMetrics event found
2026-11-20T13:04:09Z F64-NE: model size in memory right after the refresh: 92.7 MB
```
