# Harness run 20261120T145612Z-v21-e764

- Task: refresh
- Variant: v21-pq-group-by
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 690d1088-e85d-4c86-84c8-dc483608c583
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 2,805 MB, Power Query 2,517 MB, duration 2 min, CPU 239 s, rows 3,032,622, model 85 MB (Backup step in SemanticModelLogs)
- Refresh request c3fd94db-e000-4b51-be19-6d403947f302, 2026-11-20T14:59:13.33 to 2026-11-20T15:00:55.85, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v21-pq-group-by on F64-NE data-1m-v1: refreshed, peak 2,761 MB (2026-11-20T13:16:25Z).
  - Peak change: +44 MB (+1.6%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T14:22:30Z): peak 2,805 MB vs 949 MB (+1,856 MB), Power Query 2,517 MB vs 904 MB, model 85 MB vs 72 MB.
- Model size in memory when the full refresh started: 92 MB. The refresh may use the SKU maximum minus this: 25,508 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,974 MB: fits (94%); F16 5,028 MB: fits (56%); F32 10,148 MB: fits (28%); F64 25,508 MB: fits (11%); PPU 102,308 MB: fits (3%); F2-csv 2,974 MB: fits (94%); F2-sql 2,974 MB: fits (94%); F64-NE 25,508 MB: fits (11%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  d5535df7-7b8d-4929-b7bc-e37c2cd4c00f TabularSequencePoint         94.4     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         92.1    20.9       0
                         Customer Stats.Customer Stats       TabularRefresh         91.6     2.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         87.5    20.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         87.1    20.7 2349091
                         Customer Stats.Customer Stats           ExecuteSql         71.7     0.0       0
                         Customer Stats.Customer Stats              Process         19.6     2.6       0
                         Customer Stats.Customer Stats             ReadData         19.0     2.1  471482
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.8    11.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.6    10.5       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.9     1.8       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          4.8     0.1       0
```

## Log

```
2026-11-20T14:58:38Z run 20261120T145612Z-v21-e764: variant=v21-pq-group-by data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T14:58:43Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T14:58:46Z F64-NE: v21-pq-group-by is d5535df7-7b8d-4929-b7bc-e37c2cd4c00f, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T14:58:48Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T14:59:13Z F64-NE: model size in memory before the refresh: 92.1 MB
2026-11-20T14:59:13Z F64-NE: refresh started, request c3fd94db-e000-4b51-be19-6d403947f302
2026-11-20T15:01:24Z F64-NE: refresh refreshed (Completed) 
2026-11-20T15:01:24Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T15:03:00Z F64-NE: ExecutionMetrics event found
2026-11-20T15:03:02Z F64-NE: model size in memory right after the refresh: 118.6 MB
```
