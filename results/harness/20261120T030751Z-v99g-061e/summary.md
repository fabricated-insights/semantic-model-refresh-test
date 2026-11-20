# Harness run 20261120T030751Z-v99g-061e

- Task: refresh
- Variant: v99g-sales-copy
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 92297efd-4e7b-451f-a192-ce39aa0ff509
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 22,952 MB, Power Query 22,816 MB, duration 18 min, CPU 3,677 s, rows 38,422,496, model 536 MB (Backup step in SemanticModelLogs)
- Refresh request 72850f8d-91c9-4cc6-b351-bb71a7e5714b, 2026-11-20T03:09:07.873 to 2026-11-20T03:27:22.007, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99g-sales-copy on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 22,952 MB vs 615 MB (+22,337 MB), Power Query 22,816 MB vs 335 MB, model 536 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (749%); F16 5,120 MB: OVER (448%); F32 10,240 MB: OVER (224%); F64 25,600 MB: fits (90%); PPU 102,400 MB: fits (22%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            7019bbb5-e7cd-4985-bc14-7af18c43cc4e TabularSequencePoint       1079.4     0.4       0
                           Sales Flat.Sales Flat       TabularRefresh       1064.6    66.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1019.8    23.9       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        655.2    23.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        655.0    23.8 2349091
                           Sales Flat.Sales Flat           ExecuteSql        542.4     0.0       0
                           Sales Flat.Sales Flat              Process        522.1    66.3       0
                           Sales Flat.Sales Flat             ReadData        521.6    66.3 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        364.4     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        328.9     2.3       0
                   Customer Stats.Customer Stats           ExecuteSql        199.5     0.0       0
                   Customer Stats.Customer Stats              Process        129.3     2.2       0
```

## Log

```
2026-11-20T03:08:29Z run 20261120T030751Z-v99g-061e: variant=v99g-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T03:08:44Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T03:08:50Z F64: v99g-sales-copy is 7019bbb5-e7cd-4985-bc14-7af18c43cc4e, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T03:09:07Z F64: model size in memory before the refresh: 0.4 MB
2026-11-20T03:09:08Z F64: refresh started, request 72850f8d-91c9-4cc6-b351-bb71a7e5714b
2026-11-20T03:27:51Z F64: refresh refreshed (Completed) 
2026-11-20T03:27:51Z F64: monitoring database Monitoring KQL database
2026-11-20T03:28:40Z F64: ExecutionMetrics event found
2026-11-20T03:28:59Z F64: model size in memory right after the refresh: 662.8 MB
```
