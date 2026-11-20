# Harness run 20261120T035138Z-v99h-f55a

- Task: refresh
- Variant: v99h-staging-buffers
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1260369c-b116-41d2-83c4-be3ee0d31220
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 25,832 MB, Power Query 25,705 MB, duration 33 min, CPU 6,599 s, rows 38,422,496, model 536 MB (Backup step in XMLA trace)
- Refresh request 4a8ffd0b-7c86-4489-8c09-530f42eeeec1, 2026-11-20T03:54:27.757 to 2026-11-20T04:27:51.86, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99h-staging-buffers on PPU data-1m-v1: refreshed, peak 25,939 MB (2026-11-17T23:18:47Z).
  - Peak change: -107 MB (-0.4%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 25,832 MB vs 551 MB (+25,281 MB), Power Query 25,705 MB vs 298 MB, model 536 MB vs 73 MB.
- Model size in memory when the full refresh started: 541 MB. The refresh may use the SKU maximum minus this: 101,859 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,525 MB: OVER (1023%); F16 4,579 MB: OVER (564%); F32 9,699 MB: OVER (266%); F64 25,059 MB: OVER (103%); PPU 101,859 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            fceac6f8-d619-41bc-83ea-24304ed40142 TabularSequencePoint       1981.7     0.6       0
                           Sales Flat.Sales Flat       TabularRefresh       1845.0    82.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1758.0    27.9       0
                           Sales Flat.Sales Flat           ExecuteSql       1132.3     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process       1036.1    27.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData       1035.8    27.8 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        721.8     0.0       0
                           Sales Flat.Sales Flat              Process        712.6    82.2       0
                           Sales Flat.Sales Flat             ReadData        711.9    82.2 2349091
                   Customer Stats.Customer Stats       TabularRefresh        647.0     2.8       0
                   Customer Stats.Customer Stats           ExecuteSql        355.6     0.0       0
                   Customer Stats.Customer Stats              Process        291.2     2.7       0
```

## Log

```
2026-11-20T03:53:42Z run 20261120T035138Z-v99h-f55a: variant=v99h-staging-buffers data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T03:53:54Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T03:54:02Z PPU: v99h-staging-buffers is fceac6f8-d619-41bc-83ea-24304ed40142, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T03:54:24Z PPU: model size in memory before the refresh: 540.6 MB
2026-11-20T03:54:27Z PPU: trace started (full)
2026-11-20T03:54:27Z PPU: refresh started, request 4a8ffd0b-7c86-4489-8c09-530f42eeeec1
2026-11-20T04:28:13Z PPU: refresh refreshed (Completed) 
2026-11-20T04:28:44Z PPU: trace captured 846 events: ProgressReportEnd 799, ExecutionMetrics 36, CommandEnd 11
2026-11-20T04:28:45Z PPU: model size in memory right after the refresh: 662.8 MB
```
