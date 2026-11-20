# Harness run 20261120T034647Z-v99j-061e

- Task: refresh
- Variant: v99j-buffer-stg-customer
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 7554e3ec-c1b5-4929-bce4-331750d1d79e
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 23,051 MB, Power Query 22,919 MB, duration 13 min, CPU 2,410 s, rows 38,422,496, model 534 MB (Backup step in SemanticModelLogs)
- Refresh request b006c843-51a5-4a43-bc70-29d86ac75cb9, 2026-11-20T03:47:43.99 to 2026-11-20T04:00:45.117, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99j-buffer-stg-customer on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 23,051 MB vs 615 MB (+22,436 MB), Power Query 22,919 MB vs 335 MB, model 534 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (752%); F16 5,120 MB: OVER (450%); F32 10,240 MB: OVER (225%); F64 25,600 MB: fits (90%); PPU 102,400 MB: fits (23%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            49b9c9d3-9a88-4664-8d54-995932ee7dc2 TabularSequencePoint        767.1     0.4       0
                           Sales Flat.Sales Flat       TabularRefresh        727.7    68.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        718.9    21.9       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        425.8    21.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        425.5    21.8 2349091
                           Sales Flat.Sales Flat           ExecuteSql        378.1     0.0       0
                           Sales Flat.Sales Flat              Process        349.5    68.7       0
                           Sales Flat.Sales Flat             ReadData        349.0    68.7 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        292.9     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        269.4     2.4       0
                   Customer Stats.Customer Stats           ExecuteSql        181.7     0.0       0
                   Customer Stats.Customer Stats              Process         87.5     2.3       0
```

## Log

```
2026-11-20T03:47:16Z run 20261120T034647Z-v99j-061e: variant=v99j-buffer-stg-customer data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T03:47:27Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T03:47:31Z F64: v99j-buffer-stg-customer is 49b9c9d3-9a88-4664-8d54-995932ee7dc2, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T03:47:43Z F64: model size in memory before the refresh: 0.4 MB
2026-11-20T03:47:44Z F64: refresh started, request b006c843-51a5-4a43-bc70-29d86ac75cb9
2026-11-20T04:00:56Z F64: refresh refreshed (Completed) 
2026-11-20T04:00:56Z F64: monitoring database Monitoring KQL database
2026-11-20T04:02:32Z F64: ExecutionMetrics event found
2026-11-20T04:02:35Z F64: model size in memory right after the refresh: 660.7 MB
```
