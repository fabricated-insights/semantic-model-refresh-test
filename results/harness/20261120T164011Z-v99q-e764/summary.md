# Harness run 20261120T164011Z-v99q-e764

- Task: refresh
- Variant: v99q-customer-stats
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 08b37e7e-f80e-4ab4-9d03-190a1cc35888
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 2,773 MB, Power Query 2,463 MB, duration 2 min, CPU 236 s, rows 22,055,454, model 114 MB (Backup step in SemanticModelLogs)
- Refresh request b6adcefc-944c-4ccc-abc4-9a1286c15235, 2026-11-20T16:43:19.74 to 2026-11-20T16:45:01.71, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99q-customer-stats on F64-NE data-1m-v1: refreshed, peak 2,805 MB (2026-11-20T14:55:30Z).
  - Peak change: -32 MB (-1.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T16:08:01Z): peak 2,773 MB vs 648 MB (+2,125 MB), Power Query 2,463 MB vs 616 MB, model 114 MB vs 73 MB.
- Model size in memory when the full refresh started: 162 MB. The refresh may use the SKU maximum minus this: 25,438 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,904 MB: fits (95%); F16 4,958 MB: fits (56%); F32 10,078 MB: fits (28%); F64 25,438 MB: fits (11%); PPU 102,238 MB: fits (3%); F2-csv 2,904 MB: fits (95%); F2-sql 2,904 MB: fits (95%); F64-NE 25,438 MB: fits (11%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    24e4f607-e268-413c-9f32-63cd98f108dd TabularSequencePoint         90.9     0.2       0
                                           Customer Stats.Customer Stats       TabularRefresh         87.1     2.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         78.9    21.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         75.7    21.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         75.2    20.9 2349091
                                           Customer Stats.Customer Stats           ExecuteSql         70.4     0.0       0
                                           Customer Stats.Customer Stats              Process         16.4     2.5       0
                                           Customer Stats.Customer Stats             ReadData         15.9     2.1  471482
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.1    11.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.9     8.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.6     1.7       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          5.8     0.6       0
```

## Log

```
2026-11-20T16:42:45Z run 20261120T164011Z-v99q-e764: variant=v99q-customer-stats data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T16:42:51Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T16:42:53Z F64-NE: v99q-customer-stats is 24e4f607-e268-413c-9f32-63cd98f108dd, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T16:42:55Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T16:43:19Z F64-NE: model size in memory before the refresh: 162.1 MB
2026-11-20T16:43:19Z F64-NE: refresh started, request b6adcefc-944c-4ccc-abc4-9a1286c15235
2026-11-20T16:45:30Z F64-NE: refresh refreshed (Completed) 
2026-11-20T16:45:30Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T16:46:20Z F64-NE: ExecutionMetrics event found
2026-11-20T16:46:22Z F64-NE: model size in memory right after the refresh: 162.1 MB
```
