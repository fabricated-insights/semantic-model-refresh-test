# Harness run 20261120T163124Z-v18-e764

- Task: refresh
- Variant: v18-pq-10m-summary
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: c87ff7fa-99cc-4bea-94fb-c3ae2efdbf22
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 3,633 MB, Power Query 3,605 MB, duration 2 min, CPU 172 s, rows 2,561,730, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 2d4a320c-3633-405d-9102-cb1ed01abde5, 2026-11-20T16:34:41.673 to 2026-11-20T16:36:39.41, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v18-pq-10m-summary on F64-NE data-1m-v1: refreshed, peak 1,436 MB (2026-11-20T14:49:48Z).
  - Peak change: +2,197 MB (+153.0%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T16:08:01Z): peak 3,633 MB vs 648 MB (+2,985 MB), Power Query 3,605 MB vs 616 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 93 MB. The refresh may use the SKU maximum minus this: 25,507 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,973 MB: OVER (122%); F16 5,027 MB: fits (72%); F32 10,147 MB: fits (36%); F64 25,507 MB: fits (14%); PPU 102,307 MB: fits (4%); F2-csv 2,973 MB: OVER (122%); F2-sql 2,973 MB: OVER (122%); F64-NE 25,507 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  bc6f6aac-ed6e-4b37-9b1e-d5afc029b466 TabularSequencePoint        108.4     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        107.6    24.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        104.5    24.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        103.8    24.1 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         12.4    13.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         12.2    12.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         10.7     2.3       0
                 Store Year Summary.Store Year Summary       TabularRefresh          7.9     0.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          5.9     2.3       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          5.7     2.2  104990
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          4.7     0.0       0
                 Store Year Summary.Store Year Summary           ExecuteSql          3.9     0.0       0
```

## Log

```
2026-11-20T16:34:03Z run 20261120T163124Z-v18-e764: variant=v18-pq-10m-summary data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T16:34:11Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T16:34:12Z F64-NE: v18-pq-10m-summary is bc6f6aac-ed6e-4b37-9b1e-d5afc029b466, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T16:34:14Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T16:34:41Z F64-NE: model size in memory before the refresh: 92.7 MB
2026-11-20T16:34:41Z F64-NE: refresh started, request 2d4a320c-3633-405d-9102-cb1ed01abde5
2026-11-20T16:36:52Z F64-NE: refresh refreshed (Completed) 
2026-11-20T16:36:52Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T16:39:29Z F64-NE: ExecutionMetrics event found
2026-11-20T16:39:31Z F64-NE: model size in memory right after the refresh: 92.7 MB
```
