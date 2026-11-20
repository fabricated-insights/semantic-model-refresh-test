# Harness run 20261120T164700Z-v21-e764

- Task: refresh
- Variant: v21-pq-group-by
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 55b4760d-fa12-439b-8b61-2e3eba045c05
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 2,743 MB, Power Query 2,460 MB, duration 2 min, CPU 233 s, rows 3,032,622, model 85 MB (Backup step in SemanticModelLogs)
- Refresh request c8697e61-ac01-457c-b7c1-d512498f4d4f, 2026-11-20T16:48:04.327 to 2026-11-20T16:49:47.19, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v21-pq-group-by on F64-NE data-1m-v1: refreshed, peak 2,805 MB (2026-11-20T15:03:01Z).
  - Peak change: -62 MB (-2.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T16:08:01Z): peak 2,743 MB vs 648 MB (+2,095 MB), Power Query 2,460 MB vs 616 MB, model 85 MB vs 73 MB.
- Model size in memory when the full refresh started: 92 MB. The refresh may use the SKU maximum minus this: 25,508 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,974 MB: fits (92%); F16 5,028 MB: fits (55%); F32 10,148 MB: fits (27%); F64 25,508 MB: fits (11%); PPU 102,308 MB: fits (3%); F2-csv 2,974 MB: fits (92%); F2-sql 2,974 MB: fits (92%); F64-NE 25,508 MB: fits (11%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    d5535df7-7b8d-4929-b7bc-e37c2cd4c00f TabularSequencePoint         92.3     0.1       0
                                           Customer Stats.Customer Stats       TabularRefresh         89.7     2.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         84.5    22.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         80.1    22.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         79.7    22.0 2349091
                                           Customer Stats.Customer Stats           ExecuteSql         72.2     0.0       0
                                           Customer Stats.Customer Stats              Process         17.2     2.4       0
                                           Customer Stats.Customer Stats             ReadData         16.7     2.0  471482
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.2    12.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.0    10.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.4     2.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          5.2     0.7       0
```

## Log

```
2026-11-20T16:47:37Z run 20261120T164700Z-v21-e764: variant=v21-pq-group-by data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T16:47:43Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T16:47:46Z F64-NE: v21-pq-group-by is d5535df7-7b8d-4929-b7bc-e37c2cd4c00f, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T16:47:48Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T16:48:04Z F64-NE: model size in memory before the refresh: 92.1 MB
2026-11-20T16:48:04Z F64-NE: refresh started, request c8697e61-ac01-457c-b7c1-d512498f4d4f
2026-11-20T16:50:15Z F64-NE: refresh refreshed (Completed) 
2026-11-20T16:50:15Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T16:52:51Z F64-NE: ExecutionMetrics event found
2026-11-20T16:53:26Z F64-NE: model size in memory right after the refresh: 118.6 MB
```
