# Harness run 20261120T150329Z-v20-e764

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 7ef32a0d-aa83-40d0-9649-1005afd385d0
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 3,960 MB, Power Query 3,744 MB, duration 9 min, CPU 670 s, rows 2,561,140, model 72 MB (Backup step in SemanticModelLogs)
- Refresh request b75efbc9-91c9-4350-8880-738c9b839b7e, 2026-11-20T15:07:45.85 to 2026-11-20T15:16:25.707, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v20-pq-sort on F64-NE data-1m-v1: refreshed, peak 3,895 MB (2026-11-20T13:26:39Z).
  - Peak change: +65 MB (+1.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T14:22:30Z): peak 3,960 MB vs 949 MB (+3,011 MB), Power Query 3,744 MB vs 904 MB, model 72 MB vs 72 MB.
- Model size in memory when the full refresh started: 65 MB. The refresh may use the SKU maximum minus this: 25,535 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,001 MB: OVER (132%); F16 5,055 MB: fits (78%); F32 10,175 MB: fits (39%); F64 25,535 MB: fits (16%); PPU 102,335 MB: fits (4%); F2-csv 3,001 MB: OVER (132%); F2-sql 3,001 MB: OVER (132%); F64-NE 25,535 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    a367c984-1137-4302-93ee-984a584d2d79 TabularSequencePoint        511.5     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        505.2    22.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        285.7    21.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        285.3    21.8 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        219.1     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          9.0     1.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.3     8.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.1     7.1       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          6.8     0.7       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          6.0     0.2       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          5.9     0.1       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          5.7     0.0       0
```

## Log

```
2026-11-20T15:07:06Z run 20261120T150329Z-v20-e764: variant=v20-pq-sort data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T15:07:12Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T15:07:15Z F64-NE: v20-pq-sort is a367c984-1137-4302-93ee-984a584d2d79, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T15:07:15Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T15:07:45Z F64-NE: model size in memory before the refresh: 65.3 MB
2026-11-20T15:07:45Z F64-NE: refresh started, request b75efbc9-91c9-4350-8880-738c9b839b7e
2026-11-20T15:16:27Z F64-NE: refresh refreshed (Completed) 
2026-11-20T15:16:27Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T15:19:04Z F64-NE: ExecutionMetrics event found
2026-11-20T15:19:08Z F64-NE: model size in memory right after the refresh: 91.9 MB
```
