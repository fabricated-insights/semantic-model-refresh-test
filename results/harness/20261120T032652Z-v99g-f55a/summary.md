# Harness run 20261120T032652Z-v99g-f55a

- Task: refresh
- Variant: v99g-sales-copy
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ec497542-98de-4201-9e56-6d3873eab86d
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 22,945 MB, Power Query 22,803 MB, duration 20 min, CPU 4,076 s, rows 38,422,496, model 536 MB (Backup step in XMLA trace)
- Refresh request 04ef71ee-ac4a-4224-a83e-918e6e441ea2, 2026-11-20T03:30:07.4 to 2026-11-20T03:50:16.423, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99g-sales-copy on PPU data-1m-v1: refreshed, peak 22,919 MB (2026-11-17T21:09:30Z).
  - Peak change: +26 MB (+0.1%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 22,945 MB vs 551 MB (+22,394 MB), Power Query 22,803 MB vs 298 MB, model 536 MB vs 73 MB.
- Model size in memory when the full refresh started: 541 MB. The refresh may use the SKU maximum minus this: 101,859 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,525 MB: OVER (909%); F16 4,579 MB: OVER (501%); F32 9,699 MB: OVER (237%); F64 25,059 MB: fits (92%); PPU 101,859 MB: fits (23%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            0fc043ea-05ca-437e-b339-49dc7a786423 TabularSequencePoint       1193.4     0.5       0
                           Sales Flat.Sales Flat       TabularRefresh       1177.5    65.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1130.7    24.5       0
                           Sales Flat.Sales Flat           ExecuteSql        853.4     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        587.1    24.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        586.8    24.5 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        543.5     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        434.9     2.3       0
                           Sales Flat.Sales Flat              Process        324.0    65.4       0
                           Sales Flat.Sales Flat             ReadData        323.4    65.3 2349091
                   Customer Stats.Customer Stats           ExecuteSql        239.4     0.0       0
                   Customer Stats.Customer Stats              Process        195.4     2.3       0
```

## Log

```
2026-11-20T03:29:22Z run 20261120T032652Z-v99g-f55a: variant=v99g-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T03:29:32Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T03:29:41Z PPU: v99g-sales-copy is 0fc043ea-05ca-437e-b339-49dc7a786423, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T03:30:03Z PPU: model size in memory before the refresh: 540.6 MB
2026-11-20T03:30:07Z PPU: trace started (full)
2026-11-20T03:30:07Z PPU: refresh started, request 04ef71ee-ac4a-4224-a83e-918e6e441ea2
2026-11-20T03:50:20Z PPU: refresh refreshed (Completed) 
2026-11-20T03:50:51Z PPU: trace captured 845 events: ProgressReportEnd 799, ExecutionMetrics 35, CommandEnd 11
2026-11-20T03:50:53Z PPU: model size in memory right after the refresh: 662.8 MB
```
