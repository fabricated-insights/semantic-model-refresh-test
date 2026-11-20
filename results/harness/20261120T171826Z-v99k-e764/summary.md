# Harness run 20261120T171826Z-v99k-e764

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: e2cd38ca-6d89-421f-89d8-c266c8d2e086
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 10,447 MB, Power Query 10,334 MB, duration 18 min, CPU 1,988 s, rows 22,085,043, model 185 MB (Backup step in SemanticModelLogs)
- Refresh request 9541a49a-14c0-4635-a3fb-a9edaf3c4d0c, 2026-11-20T17:21:40.883 to 2026-11-20T17:40:17.557, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99k-no-buffers on F64-NE data-1m-v1: refreshed, peak 10,620 MB (2026-11-20T15:57:15Z).
  - Peak change: -173 MB (-1.6%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T16:08:01Z): peak 10,447 MB vs 648 MB (+9,799 MB), Power Query 10,334 MB vs 616 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 233 MB. The refresh may use the SKU maximum minus this: 25,367 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,833 MB: OVER (369%); F16 4,887 MB: OVER (214%); F32 10,007 MB: OVER (104%); F64 25,367 MB: fits (41%); PPU 102,167 MB: fits (10%); F2-csv 2,833 MB: OVER (369%); F2-sql 2,833 MB: OVER (369%); F64-NE 25,367 MB: fits (41%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  f08f1af1-3890-4e46-ad6f-94a1633bdd17 TabularSequencePoint       1102.7     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1091.7    22.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        658.7    22.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        658.4    22.3 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        432.7     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        261.4     2.4       0
                         Customer Stats.Customer Stats           ExecuteSql        133.7     0.0       0
                         Customer Stats.Customer Stats              Process        127.6     2.3       0
                         Customer Stats.Customer Stats             ReadData        127.1     1.9  471482
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         11.3     1.7       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          6.4     0.2       0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          6.3     0.1       0
```

## Log

```
2026-11-20T17:21:02Z run 20261120T171826Z-v99k-e764: variant=v99k-no-buffers data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T17:21:12Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T17:21:13Z F64-NE: v99k-no-buffers is f08f1af1-3890-4e46-ad6f-94a1633bdd17, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T17:21:15Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T17:21:40Z F64-NE: model size in memory before the refresh: 232.6 MB
2026-11-20T17:21:41Z F64-NE: refresh started, request 9541a49a-14c0-4635-a3fb-a9edaf3c4d0c
2026-11-20T17:40:23Z F64-NE: refresh refreshed (Completed) 
2026-11-20T17:40:24Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T17:41:59Z F64-NE: ExecutionMetrics event found
2026-11-20T17:42:18Z F64-NE: model size in memory right after the refresh: 232.6 MB
```
