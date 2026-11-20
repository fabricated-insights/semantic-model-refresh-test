# Harness run 20261120T151952Z-v99o-e764

- Task: refresh
- Variant: v99o-sorts
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: bcbad987-ae8c-4e6b-a038-6298e5c12e74
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 3,960 MB, Power Query 3,670 MB, duration 8 min, CPU 652 s, rows 21,583,972, model 100 MB (Backup step in SemanticModelLogs)
- Refresh request cde0b948-183f-4fa3-9d22-9e6fb6ba525e, 2026-11-20T15:20:54.773 to 2026-11-20T15:29:12.547, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99o-sorts on F64-NE data-1m-v1: refreshed, peak 3,973 MB (2026-11-20T13:41:45Z).
  - Peak change: -13 MB (-0.3%).
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T14:22:30Z): peak 3,960 MB vs 949 MB (+3,011 MB), Power Query 3,670 MB vs 904 MB, model 100 MB vs 72 MB.
- Model size in memory when the full refresh started: 99 MB. The refresh may use the SKU maximum minus this: 25,501 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,967 MB: OVER (133%); F16 5,021 MB: fits (79%); F32 10,141 MB: fits (39%); F64 25,501 MB: fits (16%); PPU 102,301 MB: fits (4%); F2-csv 2,967 MB: OVER (133%); F2-sql 2,967 MB: OVER (133%); F64-NE 25,501 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    2ca525b8-ba2f-43d0-8174-7a5309142f7a TabularSequencePoint        487.5     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        475.2    21.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        258.3    21.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        257.9    21.6 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        216.6     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.0     8.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.7     6.7       0
                                                  Sales.Sales Line Label       TabularRefresh          6.0     5.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.6     2.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          5.1     0.7       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          4.8     0.2       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          4.6     0.1       0
```

## Log

```
2026-11-20T15:20:25Z run 20261120T151952Z-v99o-e764: variant=v99o-sorts data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T15:20:35Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T15:20:39Z F64-NE: v99o-sorts is 2ca525b8-ba2f-43d0-8174-7a5309142f7a, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T15:20:39Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T15:20:54Z F64-NE: model size in memory before the refresh: 99.0 MB
2026-11-20T15:20:54Z F64-NE: refresh started, request cde0b948-183f-4fa3-9d22-9e6fb6ba525e
2026-11-20T15:29:36Z F64-NE: refresh refreshed (Completed) 
2026-11-20T15:29:36Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T15:31:11Z F64-NE: ExecutionMetrics event found
2026-11-20T15:31:30Z F64-NE: model size in memory right after the refresh: 133.8 MB
```
