# Harness run 20261120T123908Z-v99n-e764

- Task: refresh
- Variant: v99n-text-staging
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: b93ef568-607c-4590-a5b2-5c53880f3b75
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 545 MB, Power Query 351 MB, duration 11 min, CPU 751 s, rows 21,587,990, model 92 MB (Backup step in SemanticModelLogs)
- Refresh request 3a9ee08f-baa4-4fab-8b9f-9a942c62b863, 2026-11-20T12:41:49.087 to 2026-11-20T12:53:14.6, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99n-text-staging on F64-NE data-1m-v1.
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T12:30:33Z): peak 545 MB vs 623 MB (-78 MB), Power Query 351 MB vs 583 MB, model 92 MB vs 72 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (18%); F16 5,120 MB: fits (11%); F32 10,240 MB: fits (5%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%); F2-csv 3,066 MB: fits (18%); F2-sql 3,066 MB: fits (18%); F64-NE 25,600 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    814c5612-7ecd-4e32-9903-3ac0847a5987 TabularSequencePoint        676.5     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        669.8    34.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        665.4    33.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        665.0    33.8 2349091
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         13.0     2.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.5     9.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.2     7.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          6.9     1.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          6.7     1.8  104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          5.8     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          5.6     0.7       0
                                                  Sales.Sales Line Label       TabularRefresh          4.7     4.7       0
```

## Log

```
2026-11-20T12:41:14Z run 20261120T123908Z-v99n-e764: variant=v99n-text-staging data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T12:41:20Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T12:41:21Z F64-NE: v99n-text-staging is 814c5612-7ecd-4e32-9903-3ac0847a5987, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T12:41:22Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T12:41:48Z F64-NE: model size in memory before the refresh: 0.1 MB
2026-11-20T12:41:49Z F64-NE: refresh started, request 3a9ee08f-baa4-4fab-8b9f-9a942c62b863
2026-11-20T12:53:31Z F64-NE: refresh refreshed (Completed) 
2026-11-20T12:53:31Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T12:56:07Z F64-NE: ExecutionMetrics event found
2026-11-20T12:56:10Z F64-NE: model size in memory right after the refresh: 124.3 MB
```
