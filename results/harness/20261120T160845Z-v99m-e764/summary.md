# Harness run 20261120T160845Z-v99m-e764

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 87409a4a-1df3-41c0-8171-072bc4803233
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 979 MB, Power Query 970 MB, duration 2 min, CPU 192 s, rows 21,583,972, model 102 MB (Backup step in SemanticModelLogs)
- Refresh request 8b246d81-a1b7-4a1a-af6d-54d864dfe2f2, 2026-11-20T16:09:53.213 to 2026-11-20T16:12:13.503, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99m-baseline-pq on F64-NE data-1m-v1: refreshed, peak 521 MB (2026-11-20T14:29:11Z).
  - Peak change: +458 MB (+87.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T16:08:01Z): peak 979 MB vs 648 MB (+331 MB), Power Query 970 MB vs 616 MB, model 102 MB vs 73 MB.
- Model size in memory when the full refresh started: 101 MB. The refresh may use the SKU maximum minus this: 25,499 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,965 MB: fits (33%); F16 5,019 MB: fits (20%); F32 10,139 MB: fits (10%); F64 25,499 MB: fits (4%); PPU 102,299 MB: fits (1%); F2-csv 2,965 MB: fits (33%); F2-sql 2,965 MB: fits (33%); F64-NE 25,499 MB: fits (4%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    59d3a17d-96e6-4e9b-af01-47a2b7340201 TabularSequencePoint        129.0     0.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        120.0    26.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        111.3    26.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        110.8    26.6 2349091
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         14.1     2.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.2    13.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.9    10.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          9.5     0.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          8.3     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          8.3     0.0       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          8.2     0.1       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          7.6     0.2       0
```

## Log

```
2026-11-20T16:09:22Z run 20261120T160845Z-v99m-e764: variant=v99m-baseline-pq data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T16:09:31Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T16:09:34Z F64-NE: v99m-baseline-pq is 59d3a17d-96e6-4e9b-af01-47a2b7340201, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T16:09:35Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T16:09:53Z F64-NE: model size in memory before the refresh: 101.3 MB
2026-11-20T16:09:53Z F64-NE: refresh started, request 8b246d81-a1b7-4a1a-af6d-54d864dfe2f2
2026-11-20T16:12:34Z F64-NE: refresh refreshed (Completed) 
2026-11-20T16:12:34Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T16:14:16Z F64-NE: ExecutionMetrics event found
2026-11-20T16:14:18Z F64-NE: model size in memory right after the refresh: 136.1 MB
```
