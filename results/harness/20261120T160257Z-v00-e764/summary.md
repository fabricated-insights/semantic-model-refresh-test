# Harness run 20261120T160257Z-v00-e764

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: bc929f84-f6ff-4e2a-a3e5-338fe5825a38
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 648 MB, Power Query 616 MB, duration 2 min, CPU 146 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request f589a732-2352-4f51-8454-d641bf45d7fa, 2026-11-20T16:04:11.783 to 2026-11-20T16:05:52.593, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v00-baseline on F64-NE data-1m-v1: refreshed, peak 949 MB (2026-11-20T14:22:30Z).
  - Peak change: -301 MB (-31.7%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 25,534 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (22%); F16 5,054 MB: fits (13%); F32 10,174 MB: fits (6%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%); F2-csv 3,000 MB: fits (22%); F2-sql 3,000 MB: fits (22%); F64-NE 25,534 MB: fits (3%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    19cc20ca-dba3-4570-95d8-761af4ab7063 TabularSequencePoint         91.6     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         90.9    21.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         85.9    21.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         85.6    21.4 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.9    12.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.7    10.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          8.3     2.4       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          5.9     0.8       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          5.5     0.2       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          5.1     0.1       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          4.9     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          4.8     0.0       0
```

## Log

```
2026-11-20T16:03:44Z run 20261120T160257Z-v00-e764: variant=v00-baseline data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T16:03:49Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T16:03:52Z F64-NE: v00-baseline is 19cc20ca-dba3-4570-95d8-761af4ab7063, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T16:03:55Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T16:04:11Z F64-NE: model size in memory before the refresh: 65.5 MB
2026-11-20T16:04:11Z F64-NE: refresh started, request f589a732-2352-4f51-8454-d641bf45d7fa
2026-11-20T16:06:22Z F64-NE: refresh refreshed (Completed) 
2026-11-20T16:06:22Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T16:07:11Z F64-NE: ExecutionMetrics event found
2026-11-20T16:08:02Z F64-NE: model size in memory right after the refresh: 92.7 MB
```
