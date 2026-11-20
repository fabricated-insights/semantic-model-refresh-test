# Harness run 20261120T131134Z-v21-e764

- Task: refresh
- Variant: v21-pq-group-by
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: f231e58e-3cc4-460f-8148-e93bc192d824
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 2,761 MB, Power Query 2,463 MB, duration 1 min, CPU 221 s, rows 3,032,622, model 85 MB (Backup step in SemanticModelLogs)
- Refresh request 0f2b3e11-b681-4850-b06c-86b88f51cb9f, 2026-11-20T13:12:35.45 to 2026-11-20T13:14:11.59, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v21-pq-group-by on F64-NE data-1m-v1.
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T12:30:33Z): peak 2,761 MB vs 623 MB (+2,138 MB), Power Query 2,463 MB vs 583 MB, model 85 MB vs 72 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (90%); F16 5,120 MB: fits (54%); F32 10,240 MB: fits (27%); F64 25,600 MB: fits (11%); PPU 102,400 MB: fits (3%); F2-csv 3,066 MB: fits (90%); F2-sql 3,066 MB: fits (90%); F64-NE 25,600 MB: fits (11%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  d5535df7-7b8d-4929-b7bc-e37c2cd4c00f TabularSequencePoint         84.9     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         83.7    21.9       0
                         Customer Stats.Customer Stats       TabularRefresh         83.3     2.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         79.9    21.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         79.3    21.7 2349091
                         Customer Stats.Customer Stats           ExecuteSql         70.4     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         14.2    15.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         14.0    14.0       0
                         Customer Stats.Customer Stats              Process         12.6     2.6       0
                         Customer Stats.Customer Stats             ReadData         11.9     2.1  471482
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.4     2.2       0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          4.6     0.1       0
```

## Log

```
2026-11-20T13:12:08Z run 20261120T131134Z-v21-e764: variant=v21-pq-group-by data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T13:12:16Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T13:12:17Z F64-NE: v21-pq-group-by is d5535df7-7b8d-4929-b7bc-e37c2cd4c00f, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T13:12:19Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T13:12:35Z F64-NE: model size in memory before the refresh: 0.0 MB
2026-11-20T13:12:35Z F64-NE: refresh started, request 0f2b3e11-b681-4850-b06c-86b88f51cb9f
2026-11-20T13:14:16Z F64-NE: refresh refreshed (Completed) 
2026-11-20T13:14:16Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T13:15:52Z F64-NE: ExecutionMetrics event found
2026-11-20T13:16:26Z F64-NE: model size in memory right after the refresh: 118.6 MB
```
