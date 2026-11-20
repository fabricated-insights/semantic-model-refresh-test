# Harness run 20261120T144238Z-v18-e764

- Task: refresh
- Variant: v18-pq-10m-summary
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: bcd71f0a-89a7-4c33-b912-2b907c5aaa21
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 1,436 MB, Power Query 1,411 MB, duration 1 min, CPU 115 s, rows 2,561,730, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request a2e2e8cf-230f-436c-a378-11b04ba44e84, 2026-11-20T14:45:30.28 to 2026-11-20T14:46:52.707, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v18-pq-10m-summary on F64-NE data-1m-v1: refreshed, peak 587 MB (2026-11-20T13:04:08Z).
  - Peak change: +849 MB (+144.6%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T14:22:30Z): peak 1,436 MB vs 949 MB (+487 MB), Power Query 1,411 MB vs 904 MB, model 73 MB vs 72 MB.
- Model size in memory when the full refresh started: 93 MB. The refresh may use the SKU maximum minus this: 25,507 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,973 MB: fits (48%); F16 5,027 MB: fits (29%); F32 10,147 MB: fits (14%); F64 25,507 MB: fits (6%); PPU 102,307 MB: fits (1%); F2-csv 2,973 MB: fits (48%); F2-sql 2,973 MB: fits (48%); F64-NE 25,507 MB: fits (6%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  bc6f6aac-ed6e-4b37-9b1e-d5afc029b466 TabularSequencePoint         74.4     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         73.7    18.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         70.9    18.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         70.3    18.5 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.4    12.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.2    11.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          6.6     0.2       0
                 Store Year Summary.Store Year Summary       TabularRefresh          6.3     0.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          6.0     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.4     1.5       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          4.1     0.1       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          4.0     0.0       0
```

## Log

```
2026-11-20T14:44:53Z run 20261120T144238Z-v18-e764: variant=v18-pq-10m-summary data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T14:45:05Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T14:45:06Z F64-NE: v18-pq-10m-summary is bc6f6aac-ed6e-4b37-9b1e-d5afc029b466, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T14:45:07Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T14:45:30Z F64-NE: model size in memory before the refresh: 92.7 MB
2026-11-20T14:45:30Z F64-NE: refresh started, request a2e2e8cf-230f-436c-a378-11b04ba44e84
2026-11-20T14:47:10Z F64-NE: refresh refreshed (Completed) 
2026-11-20T14:47:11Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T14:49:47Z F64-NE: ExecutionMetrics event found
2026-11-20T14:49:49Z F64-NE: model size in memory right after the refresh: 92.7 MB
```
