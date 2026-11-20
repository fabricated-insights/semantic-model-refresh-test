# Harness run 20261120T134224Z-v99k-e764

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 25080f3b-b664-4dd9-b530-42ed24fa50b1
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 10,580 MB, Power Query 10,470 MB, duration 22 min, CPU 2,337 s, rows 22,085,043, model 185 MB (Backup step in SemanticModelLogs)
- Refresh request b89067d4-50d4-400d-b12f-8079b3f044a3, 2026-11-20T13:45:04.583 to 2026-11-20T14:07:43.487, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99k-no-buffers on F64-NE data-1m-v1.
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T12:30:33Z): peak 10,580 MB vs 623 MB (+9,957 MB), Power Query 10,470 MB vs 583 MB, model 185 MB vs 72 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (345%); F16 5,120 MB: OVER (207%); F32 10,240 MB: OVER (103%); F64 25,600 MB: fits (41%); PPU 102,400 MB: fits (10%); F2-csv 3,066 MB: OVER (345%); F2-sql 3,066 MB: OVER (345%); F64-NE 25,600 MB: fits (41%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    f08f1af1-3890-4e46-ad6f-94a1633bdd17 TabularSequencePoint       1342.0     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1305.4    26.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        875.5    26.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        875.2    26.0 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        429.8     0.0       0
                                           Customer Stats.Customer Stats       TabularRefresh        325.5     2.6       0
                                           Customer Stats.Customer Stats              Process        171.6     2.5       0
                                           Customer Stats.Customer Stats             ReadData        170.8     2.0  471482
                                           Customer Stats.Customer Stats           ExecuteSql        153.6     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         11.7     1.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          6.3     0.9       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          6.2     0.2       0
```

## Log

```
2026-11-20T13:44:25Z run 20261120T134224Z-v99k-e764: variant=v99k-no-buffers data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T13:44:38Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T13:44:40Z F64-NE: v99k-no-buffers is f08f1af1-3890-4e46-ad6f-94a1633bdd17, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T13:44:42Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T13:45:04Z F64-NE: model size in memory before the refresh: 0.1 MB
2026-11-20T13:45:04Z F64-NE: refresh started, request b89067d4-50d4-400d-b12f-8079b3f044a3
2026-11-20T14:07:48Z F64-NE: refresh refreshed (Completed) 
2026-11-20T14:07:48Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T14:08:39Z F64-NE: ExecutionMetrics event found
2026-11-20T14:09:30Z F64-NE: model size in memory right after the refresh: 232.6 MB
```
