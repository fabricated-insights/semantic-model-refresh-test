# Harness run 20261120T142953Z-v99n-e764

- Task: refresh
- Variant: v99n-text-staging
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 0278e740-cb48-411c-9729-5f8c7ceff7e2
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 467 MB, Power Query 284 MB, duration 9 min, CPU 607 s, rows 21,587,990, model 92 MB (Backup step in SemanticModelLogs)
- Refresh request e02909cc-cf18-4331-923c-7e1051b60a96, 2026-11-20T14:30:58.52 to 2026-11-20T14:40:03.49, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99n-text-staging on F64-NE data-1m-v1: refreshed, peak 545 MB (2026-11-20T12:56:09Z).
  - Peak change: -78 MB (-14.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T14:22:30Z): peak 467 MB vs 949 MB (-482 MB), Power Query 284 MB vs 904 MB, model 92 MB vs 72 MB.
- Model size in memory when the full refresh started: 91 MB. The refresh may use the SKU maximum minus this: 25,509 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,975 MB: fits (16%); F16 5,029 MB: fits (9%); F32 10,149 MB: fits (5%); F64 25,509 MB: fits (2%); PPU 102,309 MB: fits (0%); F2-csv 2,975 MB: fits (16%); F2-sql 2,975 MB: fits (16%); F64-NE 25,509 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    814c5612-7ecd-4e32-9903-3ac0847a5987 TabularSequencePoint        536.1     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        530.5    30.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        525.0    30.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        524.7    30.5 2349091
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         16.6     3.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          9.6     3.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          9.4     3.1  104990
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.6     9.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.3     7.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          6.7     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          6.1     0.6       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          5.3     0.0       0
```

## Log

```
2026-11-20T14:30:28Z run 20261120T142953Z-v99n-e764: variant=v99n-text-staging data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T14:30:35Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T14:30:39Z F64-NE: v99n-text-staging is 814c5612-7ecd-4e32-9903-3ac0847a5987, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T14:30:41Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T14:30:58Z F64-NE: model size in memory before the refresh: 90.7 MB
2026-11-20T14:30:58Z F64-NE: refresh started, request e02909cc-cf18-4331-923c-7e1051b60a96
2026-11-20T14:40:10Z F64-NE: refresh refreshed (Completed) 
2026-11-20T14:40:10Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T14:41:46Z F64-NE: ExecutionMetrics event found
2026-11-20T14:42:05Z F64-NE: model size in memory right after the refresh: 124.3 MB
```
