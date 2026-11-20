# Harness run 20261120T132734Z-v99o-e764

- Task: refresh
- Variant: v99o-sorts
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: cfe5e870-1e99-409e-8713-4c94b551abfb
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 3,973 MB, Power Query 3,679 MB, duration 9 min, CPU 772 s, rows 21,583,972, model 99 MB (Backup step in SemanticModelLogs)
- Refresh request 07003a82-1bcf-4175-a70b-06f551d3617f, 2026-11-20T13:30:26.657 to 2026-11-20T13:39:50.72, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99o-sorts on F64-NE data-1m-v1.
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T12:30:33Z): peak 3,973 MB vs 623 MB (+3,350 MB), Power Query 3,679 MB vs 583 MB, model 99 MB vs 72 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (130%); F16 5,120 MB: fits (78%); F32 10,240 MB: fits (39%); F64 25,600 MB: fits (16%); PPU 102,400 MB: fits (4%); F2-csv 3,066 MB: OVER (130%); F2-sql 3,066 MB: OVER (130%); F64-NE 25,600 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    2ca525b8-ba2f-43d0-8174-7a5309142f7a TabularSequencePoint        554.6     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        521.6    24.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        322.4    24.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        322.0    24.3 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        198.7     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.1     9.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.8     2.4       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          6.6     0.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.6     6.6       0
                                                  Sales.Sales Line Label       TabularRefresh          6.3     6.1       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          6.1     0.2       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          5.5     0.2       0
```

## Log

```
2026-11-20T13:29:48Z run 20261120T132734Z-v99o-e764: variant=v99o-sorts data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T13:29:58Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T13:29:59Z F64-NE: v99o-sorts is 2ca525b8-ba2f-43d0-8174-7a5309142f7a, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T13:30:01Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T13:30:26Z F64-NE: model size in memory before the refresh: 0.1 MB
2026-11-20T13:30:26Z F64-NE: refresh started, request 07003a82-1bcf-4175-a70b-06f551d3617f
2026-11-20T13:40:08Z F64-NE: refresh refreshed (Completed) 
2026-11-20T13:40:08Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T13:41:44Z F64-NE: ExecutionMetrics event found
2026-11-20T13:41:47Z F64-NE: model size in memory right after the refresh: 133.8 MB
```
