# Harness run 20261120T170607Z-v99o-e764

- Task: refresh
- Variant: v99o-sorts
- Data tag: data-1m-v1
- Targets: F64-NE
- Expected commit: {"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"}
- Notebook run: 077ca904-7b66-40c5-ae62-84d18029bd64
- Refresh parallelism requested: 6

## F64-NE

- Result: **refreshed** 
- Peak 3,987 MB, Power Query 3,690 MB, duration 7 min, CPU 534 s, rows 21,583,972, model 100 MB (Backup step in SemanticModelLogs)
- Refresh request a5b529cf-7249-4331-9ad3-969354297011, 2026-11-20T17:08:59.41 to 2026-11-20T17:15:45.59, workspace at 3da515c, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99o-sorts on F64-NE data-1m-v1: refreshed, peak 3,960 MB (2026-11-20T15:31:29Z).
  - Peak change: +27 MB (+0.7%).
- Against v00-baseline on F64-NE data-1m-v1 (2026-11-20T16:08:01Z): peak 3,987 MB vs 648 MB (+3,339 MB), Power Query 3,690 MB vs 616 MB, model 100 MB vs 73 MB.
- Model size in memory when the full refresh started: 99 MB. The refresh may use the SKU maximum minus this: 25,501 MB on F64-NE.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,967 MB: OVER (134%); F16 5,021 MB: fits (79%); F32 10,141 MB: fits (39%); F64 25,501 MB: fits (16%); PPU 102,301 MB: fits (4%); F2-csv 2,967 MB: OVER (134%); F2-sql 2,967 MB: OVER (134%); F64-NE 25,501 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    2ca525b8-ba2f-43d0-8174-7a5309142f7a TabularSequencePoint        399.4     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        387.8    19.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        214.7    19.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        214.4    19.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        172.7     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.4     2.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.2     8.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.0     6.0       0
                                                  Sales.Sales Line Label       TabularRefresh          5.0     4.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.1     2.5       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.0     2.4  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.1     0.8       0
```

## Log

```
2026-11-20T17:08:20Z run 20261120T170607Z-v99o-e764: variant=v99o-sorts data_tag=data-1m-v1 source_type=sql targets=['F64-NE'] expected_commit={"main": "eb585e4bb20f00c4f5196dab488d2b31c10568a2", "sql-switch": "3da515cabe58b53b303bcc7f0415e6f1f028fa69"} pipeline_run=e764457e-a202-4642-9ec1-3d3817ced16a
2026-11-20T17:08:30Z F64-NE: workspace already at 3da515cabe58b53b303bcc7f0415e6f1f028fa69
2026-11-20T17:08:35Z F64-NE: v99o-sorts is 2ca525b8-ba2f-43d0-8174-7a5309142f7a, DataTag reads back data-1m-v1, SourceType sql
2026-11-20T17:08:35Z F64-NE: data sources set up (GitHub anonymous, SQL bound to the shared connection)
2026-11-20T17:08:59Z F64-NE: model size in memory before the refresh: 99.0 MB
2026-11-20T17:08:59Z F64-NE: refresh started, request a5b529cf-7249-4331-9ad3-969354297011
2026-11-20T17:16:10Z F64-NE: refresh refreshed (Completed) 
2026-11-20T17:16:11Z F64-NE: monitoring database Monitoring KQL database
2026-11-20T17:17:46Z F64-NE: ExecutionMetrics event found
2026-11-20T17:17:48Z F64-NE: model size in memory right after the refresh: 133.8 MB
```
