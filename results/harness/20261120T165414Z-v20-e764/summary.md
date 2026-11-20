# Harness run 20261120T165414Z-v20-e764

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 6fa51c8f-afeb-417f-884b-969b8a9f970d
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 3,890 MB, Power Query 3,672 MB, duration 8 min, CPU 664 s, rows 2,561,140, model 72 MB (Backup step in SemanticModelLogs)
- Refresh request 162ef71c-94af-438e-a3db-87edba99d7e7, 2026-11-20T16:55:10.22 to 2026-11-20T17:03:32.083, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v20-pq-sort on F64-NE data-1m-v1: refreshed, peak 3,960 MB (2026-11-20T15:19:06Z).
  - Peak change: -70 MB (-1.8%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T16:08:01Z): peak 3,890 MB vs 648 MB (+3,242 MB), Power Query 3,672 MB vs 616 MB, model 72 MB vs 73 MB.
- Model size in memory when the full refresh started: 92 MB. The refresh may use the SKU maximum minus this: 25,508 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,974 MB: OVER (131%); F16 5,028 MB: fits (77%); F32 10,148 MB: fits (38%); F64 25,508 MB: fits (15%); PPU 102,308 MB: fits (4%); F2-csv 2,974 MB: OVER (131%); F2-sql 2,974 MB: OVER (131%); F64-NE 25,508 MB: fits (15%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    a367c984-1137-4302-93ee-984a584d2d79 TabularSequencePoint        492.5     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        486.4    20.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        300.1    20.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        299.8    20.4 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        186.0     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          8.8     1.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.6     7.7       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          6.4     0.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.4     6.4       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          5.9     0.2       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          5.7     0.1       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          5.6     0.1       0
```

## Log

```
2026-11-20T16:54:47Z run 20261120T165414Z-v20-e764: variant=v20-pq-sort data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T16:54:52Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T16:54:53Z F64-NE: v20-pq-sort is a367c984-1137-4302-93ee-984a584d2d79, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T16:54:55Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T16:55:10Z F64-NE: model size in memory before the refresh: 91.9 MB
2026-11-20T16:55:10Z F64-NE: refresh started, request 162ef71c-94af-438e-a3db-87edba99d7e7
2026-11-20T17:03:51Z F64-NE: refresh refreshed (Completed) 
2026-11-20T17:03:52Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T17:05:28Z F64-NE: ExecutionMetrics event found
2026-11-20T17:05:31Z F64-NE: model size in memory right after the refresh: 91.9 MB
```
