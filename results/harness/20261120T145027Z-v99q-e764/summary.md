# Harness run 20261120T145027Z-v99q-e764

- Task: refresh
- Variant: v99q-customer-stats
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: ff363c5d-01ac-44fc-9b6d-33e08c12cd4b
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 2,805 MB, Power Query 2,441 MB, duration 2 min, CPU 243 s, rows 22,055,454, model 114 MB (Backup step in SemanticModelLogs)
- Refresh request 8c08d843-9b07-4e6a-9bf4-57479d6ae112, 2026-11-20T14:51:42.197 to 2026-11-20T14:53:25.377, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99q-customer-stats on F64-NE data-1m-v1: refreshed, peak 2,806 MB (2026-11-20T13:10:49Z).
  - Peak change: -1 MB (-0.0%).
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T14:22:30Z): peak 2,805 MB vs 949 MB (+1,856 MB), Power Query 2,441 MB vs 904 MB, model 114 MB vs 72 MB.
- Model size in memory when the full refresh started: 127 MB. The refresh may use the SKU maximum minus this: 25,473 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,939 MB: fits (95%); F16 4,993 MB: fits (56%); F32 10,113 MB: fits (28%); F64 25,473 MB: fits (11%); PPU 102,273 MB: fits (3%); F2-csv 2,939 MB: fits (95%); F2-sql 2,939 MB: fits (95%); F64-NE 25,473 MB: fits (11%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    24e4f607-e268-413c-9f32-63cd98f108dd TabularSequencePoint         91.4     0.2       0
                                           Customer Stats.Customer Stats       TabularRefresh         89.3     2.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         82.7    21.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         77.6    21.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         77.2    21.0 2349091
                                           Customer Stats.Customer Stats           ExecuteSql         72.7     0.0       0
                                           Customer Stats.Customer Stats              Process         16.3     2.3       0
                                           Customer Stats.Customer Stats             ReadData         15.7     1.8  471482
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.5    11.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.3     9.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          8.1     1.8       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          5.9     0.7       0
```

## Log

```
2026-11-20T14:51:15Z run 20261120T145027Z-v99q-e764: variant=v99q-customer-stats data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T14:51:21Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T14:51:25Z F64-NE: v99q-customer-stats is 24e4f607-e268-413c-9f32-63cd98f108dd, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T14:51:26Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T14:51:42Z F64-NE: model size in memory before the refresh: 127.3 MB
2026-11-20T14:51:42Z F64-NE: refresh started, request 8c08d843-9b07-4e6a-9bf4-57479d6ae112
2026-11-20T14:53:53Z F64-NE: refresh refreshed (Completed) 
2026-11-20T14:53:53Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T14:55:28Z F64-NE: ExecutionMetrics event found
2026-11-20T14:55:30Z F64-NE: model size in memory right after the refresh: 162.1 MB
```
