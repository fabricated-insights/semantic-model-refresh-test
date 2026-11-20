# Harness run 20261120T123114Z-v99m-e764

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 974c19c8-fcc7-4c51-a3da-6baff4450159
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 580 MB, Power Query 551 MB, duration 2 min, CPU 183 s, rows 21,583,972, model 102 MB (Backup step in SemanticModelLogs)
- Refresh request e877146d-e8c3-4fb6-8cde-6e2c05c2488e, 2026-11-20T12:33:56.557 to 2026-11-20T12:36:11.463, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99m-baseline-pq on F64-NE data-1m-v1.
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T12:30:33Z): peak 580 MB vs 623 MB (-43 MB), Power Query 551 MB vs 583 MB, model 102 MB vs 72 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (19%); F16 5,120 MB: fits (11%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%); F2-csv 3,066 MB: fits (19%); F2-sql 3,066 MB: fits (19%); F64-NE 25,600 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    59d3a17d-96e6-4e9b-af01-47a2b7340201 TabularSequencePoint        124.3     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        113.8    22.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        105.3    22.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        104.7    22.4 2349091
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         15.4     2.5       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh         10.0     0.9       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          9.4     0.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          9.1     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          8.9     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          8.5     0.1       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          8.5     0.1       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          8.5     0.0       0
```

## Log

```
2026-11-20T12:33:21Z run 20261120T123114Z-v99m-e764: variant=v99m-baseline-pq data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T12:33:29Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T12:33:30Z F64-NE: v99m-baseline-pq is 59d3a17d-96e6-4e9b-af01-47a2b7340201, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T12:33:32Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T12:33:56Z F64-NE: model size in memory before the refresh: 0.1 MB
2026-11-20T12:33:56Z F64-NE: refresh started, request e877146d-e8c3-4fb6-8cde-6e2c05c2488e
2026-11-20T12:36:37Z F64-NE: refresh refreshed (Completed) 
2026-11-20T12:36:37Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T12:38:13Z F64-NE: ExecutionMetrics event found
2026-11-20T12:38:31Z F64-NE: model size in memory right after the refresh: 136.1 MB
```
