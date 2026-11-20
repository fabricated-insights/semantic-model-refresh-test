# Harness run 20261120T003435Z-v99-f55a

- Task: refresh
- Variant: v99-kitchen-sink
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 188888d9-3941-4f30-b3bc-f815dcefb08b
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 26,212 MB, Power Query 26,056 MB, duration 36 min, CPU 7,638 s, rows 40,515,912, model 622 MB (Backup step in XMLA trace)
- Refresh request 8ecbb4ff-53f9-430e-bbd9-060545247bf9, 2026-11-20T00:35:48.917 to 2026-11-20T01:11:43.303, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99-kitchen-sink on PPU data-1m-v1: refreshed, peak 25,882 MB (2026-11-18T00:00:56Z).
  - Peak change: +330 MB (+1.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 26,212 MB vs 551 MB (+25,661 MB), Power Query 26,056 MB vs 298 MB, model 622 MB vs 73 MB.
- Model size in memory when the full refresh started: 624 MB. The refresh may use the SKU maximum minus this: 101,776 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,442 MB: OVER (1073%); F16 4,496 MB: OVER (583%); F32 9,616 MB: OVER (273%); F64 24,976 MB: OVER (105%); PPU 101,776 MB: fits (26%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            67527e72-ce42-4278-b95a-711034a934b6 TabularSequencePoint       2139.1     0.5       0
                           Sales Flat.Sales Flat       TabularRefresh       2109.4    77.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1867.5    26.1       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process       1258.8    26.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData       1258.5    26.0 2349091
                           Sales Flat.Sales Flat              Process       1201.9    76.9       0
                           Sales Flat.Sales Flat             ReadData       1201.1    76.9 2349091
                           Sales Flat.Sales Flat           ExecuteSql        907.4     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        651.4     2.6       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        608.7     0.0       0
                   Customer Stats.Customer Stats           ExecuteSql        427.2     0.0       0
                   Customer Stats.Customer Stats              Process        224.1     2.5       0
```

## Log

```
2026-11-20T00:35:12Z run 20261120T003435Z-v99-f55a: variant=v99-kitchen-sink data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T00:35:21Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T00:35:32Z PPU: v99-kitchen-sink is 67527e72-ce42-4278-b95a-711034a934b6, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:35:45Z PPU: model size in memory before the refresh: 624.0 MB
2026-11-20T00:35:48Z PPU: trace started (full)
2026-11-20T00:35:49Z PPU: refresh started, request 8ecbb4ff-53f9-430e-bbd9-060545247bf9
2026-11-20T01:12:04Z PPU: refresh refreshed (Completed) 
2026-11-20T01:12:35Z PPU: trace captured 773 events: ProgressReportEnd 726, ExecutionMetrics 36, CommandEnd 11
2026-11-20T01:12:37Z PPU: model size in memory right after the refresh: 746.5 MB
```
