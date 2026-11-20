# Harness run 20261120T153211Z-v99k-e764

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 61d287da-81d5-4786-b785-3b483bfebd57
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 10,620 MB, Power Query 10,497 MB, duration 21 min, CPU 2,212 s, rows 22,085,043, model 185 MB (Backup step in SemanticModelLogs)
- Refresh request 25f271c5-3c55-408d-8c1c-d6b955e9151c, 2026-11-20T15:34:54.66 to 2026-11-20T15:55:53.507, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99k-no-buffers on F64-NE data-1m-v1: refreshed, peak 10,580 MB (2026-11-20T14:09:28Z).
  - Peak change: +40 MB (+0.4%).
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T14:22:30Z): peak 10,620 MB vs 949 MB (+9,671 MB), Power Query 10,497 MB vs 904 MB, model 185 MB vs 72 MB.
- Model size in memory when the full refresh started: 233 MB. The refresh may use the SKU maximum minus this: 25,367 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,833 MB: OVER (375%); F16 4,887 MB: OVER (217%); F32 10,007 MB: OVER (106%); F64 25,367 MB: fits (42%); PPU 102,167 MB: fits (10%); F2-csv 2,833 MB: OVER (375%); F2-sql 2,833 MB: OVER (375%); F64-NE 25,367 MB: fits (42%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  f08f1af1-3890-4e46-ad6f-94a1633bdd17 TabularSequencePoint       1245.2     0.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1235.2    24.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        656.4    24.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        656.2    24.6 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        578.5     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        425.0     3.3       0
                         Customer Stats.Customer Stats              Process        213.8     3.2       0
                         Customer Stats.Customer Stats             ReadData        212.9     2.5  471482
                         Customer Stats.Customer Stats           ExecuteSql        211.0     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         15.9     3.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          9.1     3.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          8.9     2.9  104990
```

## Log

```
2026-11-20T15:34:18Z run 20261120T153211Z-v99k-e764: variant=v99k-no-buffers data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T15:34:27Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T15:34:29Z F64-NE: v99k-no-buffers is f08f1af1-3890-4e46-ad6f-94a1633bdd17, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T15:34:31Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T15:34:54Z F64-NE: model size in memory before the refresh: 232.6 MB
2026-11-20T15:34:54Z F64-NE: refresh started, request 25f271c5-3c55-408d-8c1c-d6b955e9151c
2026-11-20T15:56:08Z F64-NE: refresh refreshed (Completed) 
2026-11-20T15:56:08Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T15:56:58Z F64-NE: ExecutionMetrics event found
2026-11-20T15:57:17Z F64-NE: model size in memory right after the refresh: 232.6 MB
```
