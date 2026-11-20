# Harness run 20261120T014114Z-v99e-061e

- Task: refresh
- Variant: v99e-sales-flat
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 7fc1353f-2001-44fc-a0f0-9aeac0019837
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 22,822 MB, Power Query 22,714 MB, duration 18 min, CPU 3,645 s, rows 24,459,705, model 323 MB (Backup step in SemanticModelLogs)
- Refresh request 6f463b3f-c855-452b-8894-46ed3de1c91b, 2026-11-20T01:44:07.927 to 2026-11-20T02:02:42.037, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99e-sales-flat on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 22,822 MB vs 615 MB (+22,207 MB), Power Query 22,714 MB vs 335 MB, model 323 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (744%); F16 5,120 MB: OVER (446%); F32 10,240 MB: OVER (223%); F64 25,600 MB: fits (89%); PPU 102,400 MB: fits (22%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            b8cd0fd3-0d59-484f-8fea-ac343761db7b TabularSequencePoint       1094.4     0.2       0
                           Sales Flat.Sales Flat       TabularRefresh       1067.9    73.1       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1042.4    24.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        688.4    24.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        688.2    24.5 2349091
                           Sales Flat.Sales Flat           ExecuteSql        558.7     0.0       0
                           Sales Flat.Sales Flat              Process        509.1    73.1       0
                           Sales Flat.Sales Flat             ReadData        508.7    73.1 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        353.8     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        303.6     2.3       0
                   Customer Stats.Customer Stats           ExecuteSql        195.2     0.0       0
                   Customer Stats.Customer Stats              Process        108.2     2.3       0
```

## Log

```
2026-11-20T01:43:29Z run 20261120T014114Z-v99e-061e: variant=v99e-sales-flat data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T01:43:43Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T01:43:47Z F64: v99e-sales-flat is b8cd0fd3-0d59-484f-8fea-ac343761db7b, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T01:44:07Z F64: model size in memory before the refresh: 0.4 MB
2026-11-20T01:44:08Z F64: refresh started, request 6f463b3f-c855-452b-8894-46ed3de1c91b
2026-11-20T02:02:50Z F64: refresh refreshed (Completed) 
2026-11-20T02:02:51Z F64: monitoring database Monitoring KQL database
2026-11-20T02:04:27Z F64: ExecutionMetrics event found
2026-11-20T02:04:30Z F64: model size in memory right after the refresh: 459.7 MB
```
