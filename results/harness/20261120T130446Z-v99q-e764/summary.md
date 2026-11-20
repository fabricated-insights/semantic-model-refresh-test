# Harness run 20261120T130446Z-v99q-e764

- Task: refresh
- Variant: v99q-customer-stats
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 87aafb65-56ec-40b2-8c6e-2d03dc5f33e3
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 2,806 MB, Power Query 2,469 MB, duration 2 min, CPU 290 s, rows 22,055,454, model 114 MB (Backup step in SemanticModelLogs)
- Refresh request 95e75056-9d44-4fc1-bba4-f84a0c08791c, 2026-11-20T13:05:59.547 to 2026-11-20T13:08:09.573, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99q-customer-stats on F64-NE data-1m-v1.
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T12:30:33Z): peak 2,806 MB vs 623 MB (+2,183 MB), Power Query 2,469 MB vs 583 MB, model 114 MB vs 72 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (92%); F16 5,120 MB: fits (55%); F32 10,240 MB: fits (27%); F64 25,600 MB: fits (11%); PPU 102,400 MB: fits (3%); F2-csv 3,066 MB: fits (92%); F2-sql 3,066 MB: fits (92%); F64-NE 25,600 MB: fits (11%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  24e4f607-e268-413c-9f32-63cd98f108dd TabularSequencePoint        116.9     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        106.7    23.2       0
                         Customer Stats.Customer Stats       TabularRefresh        104.2     2.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        103.5    23.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        103.1    23.0 2349091
                         Customer Stats.Customer Stats           ExecuteSql         79.8     0.0       0
                         Customer Stats.Customer Stats              Process         24.1     2.7       0
                         Customer Stats.Customer Stats             ReadData         23.4     2.2  471482
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.4    10.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.1     8.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.4     1.9       0
                                Sales.Sales Line Label       TabularRefresh          6.8     6.5       0
```

## Log

```
2026-11-20T13:05:34Z run 20261120T130446Z-v99q-e764: variant=v99q-customer-stats data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T13:05:40Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T13:05:42Z F64-NE: v99q-customer-stats is 24e4f607-e268-413c-9f32-63cd98f108dd, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T13:05:44Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T13:05:59Z F64-NE: model size in memory before the refresh: 0.1 MB
2026-11-20T13:05:59Z F64-NE: refresh started, request 95e75056-9d44-4fc1-bba4-f84a0c08791c
2026-11-20T13:08:10Z F64-NE: refresh refreshed (Completed) 
2026-11-20T13:08:10Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T13:10:48Z F64-NE: ExecutionMetrics event found
2026-11-20T13:10:50Z F64-NE: model size in memory right after the refresh: 162.1 MB
```
