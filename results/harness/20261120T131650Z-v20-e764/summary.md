# Harness run 20261120T131650Z-v20-e764

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: ccb06fe0-fd29-4f3c-99eb-e84b4ab5f2db
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 3,895 MB, Power Query 3,682 MB, duration 7 min, CPU 532 s, rows 2,561,140, model 72 MB (Backup step in SemanticModelLogs)
- Refresh request b0a92a36-527b-4b27-b7c1-b3dbd16450cf, 2026-11-20T13:17:48.033 to 2026-11-20T13:24:37.643, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v20-pq-sort on F64-NE data-1m-v1.
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T12:30:33Z): peak 3,895 MB vs 623 MB (+3,272 MB), Power Query 3,682 MB vs 583 MB, model 72 MB vs 72 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (127%); F16 5,120 MB: fits (76%); F32 10,240 MB: fits (38%); F64 25,600 MB: fits (15%); PPU 102,400 MB: fits (4%); F2-csv 3,066 MB: OVER (127%); F2-sql 3,066 MB: OVER (127%); F64-NE 25,600 MB: fits (15%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  a367c984-1137-4302-93ee-984a584d2d79 TabularSequencePoint        402.6     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        389.1    20.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        220.8    20.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        220.5    19.9 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        168.0     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          9.9     1.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.9     9.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.8     7.7       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          7.1     0.2       0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          7.1     0.2       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          6.9     0.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          6.6     0.0       0
```

## Log

```
2026-11-20T13:17:23Z run 20261120T131650Z-v20-e764: variant=v20-pq-sort data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T13:17:31Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T13:17:32Z F64-NE: v20-pq-sort is a367c984-1137-4302-93ee-984a584d2d79, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T13:17:33Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T13:17:47Z F64-NE: model size in memory before the refresh: 0.0 MB
2026-11-20T13:17:48Z F64-NE: refresh started, request b0a92a36-527b-4b27-b7c1-b3dbd16450cf
2026-11-20T13:24:59Z F64-NE: refresh refreshed (Completed) 
2026-11-20T13:24:59Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T13:25:49Z F64-NE: ExecutionMetrics event found
2026-11-20T13:26:40Z F64-NE: model size in memory right after the refresh: 91.9 MB
```
