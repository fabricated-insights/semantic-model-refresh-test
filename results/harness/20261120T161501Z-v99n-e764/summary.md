# Harness run 20261120T161501Z-v99n-e764

- Task: refresh
- Variant: v99n-text-staging
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: e75d680e-00cf-41d2-b30e-7451671da23a
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 589 MB, Power Query 562 MB, duration 10 min, CPU 698 s, rows 21,587,990, model 92 MB (Backup step in SemanticModelLogs)
- Refresh request ac052596-637c-42b3-91da-fe147a2ba7b2, 2026-11-20T16:18:19.627 to 2026-11-20T16:28:50.203, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99n-text-staging on F64-NE data-1m-v1: refreshed, peak 467 MB (2026-11-20T14:42:03Z).
  - Peak change: +122 MB (+26.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T16:08:01Z): peak 589 MB vs 648 MB (-59 MB), Power Query 562 MB vs 616 MB, model 92 MB vs 73 MB.
- Model size in memory when the full refresh started: 91 MB. The refresh may use the SKU maximum minus this: 25,509 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,975 MB: fits (20%); F16 5,029 MB: fits (12%); F32 10,149 MB: fits (6%); F64 25,509 MB: fits (2%); PPU 102,309 MB: fits (1%); F2-csv 2,975 MB: fits (20%); F2-sql 2,975 MB: fits (20%); F64-NE 25,509 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    814c5612-7ecd-4e32-9903-3ac0847a5987 TabularSequencePoint        622.1     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        615.7    29.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        608.9    29.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        608.5    29.7 2349091
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         12.0     1.7       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          7.7     0.6       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          6.9     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          6.8     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          6.6     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.5     8.3       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          6.3     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.3     6.3       0
```

## Log

```
2026-11-20T16:17:42Z run 20261120T161501Z-v99n-e764: variant=v99n-text-staging data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T16:17:50Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T16:17:53Z F64-NE: v99n-text-staging is 814c5612-7ecd-4e32-9903-3ac0847a5987, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T16:17:55Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T16:18:19Z F64-NE: model size in memory before the refresh: 90.7 MB
2026-11-20T16:18:19Z F64-NE: refresh started, request ac052596-637c-42b3-91da-fe147a2ba7b2
2026-11-20T16:29:02Z F64-NE: refresh refreshed (Completed) 
2026-11-20T16:29:02Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T16:30:37Z F64-NE: ExecutionMetrics event found
2026-11-20T16:30:40Z F64-NE: model size in memory right after the refresh: 124.3 MB
```
