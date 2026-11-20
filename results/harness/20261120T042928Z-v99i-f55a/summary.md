# Harness run 20261120T042928Z-v99i-f55a

- Task: refresh
- Variant: v99i-buffer-stg-sales
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 098bcac0-dd1c-4928-8596-f85c0b42d1b6
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 25,773 MB, Power Query 25,653 MB, duration 42 min, CPU 8,522 s, rows 38,422,496, model 534 MB (Backup step in XMLA trace)
- Refresh request 3acb1764-e242-406f-99df-35ded0742a15, 2026-11-20T04:30:50.787 to 2026-11-20T05:13:23.443, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99i-buffer-stg-sales on PPU data-1m-v1: refreshed, peak 25,651 MB (2026-11-18T10:00:23Z).
  - Peak change: +122 MB (+0.5%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 25,773 MB vs 551 MB (+25,222 MB), Power Query 25,653 MB vs 298 MB, model 534 MB vs 73 MB.
- Model size in memory when the full refresh started: 541 MB. The refresh may use the SKU maximum minus this: 101,859 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,525 MB: OVER (1021%); F16 4,579 MB: OVER (563%); F32 9,699 MB: OVER (266%); F64 25,059 MB: OVER (103%); PPU 101,859 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            c22581d6-175d-489e-b120-eb36a486ebd1 TabularSequencePoint       2537.3     0.5       0
                           Sales Flat.Sales Flat       TabularRefresh       2491.8    72.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       2101.4    22.7       0
                           Sales Flat.Sales Flat           ExecuteSql       1275.4     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process       1220.3    22.6       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData       1219.9    22.6 2349091
                           Sales Flat.Sales Flat              Process       1216.3    72.0       0
                           Sales Flat.Sales Flat             ReadData       1215.8    71.9 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        881.0     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        723.6     2.7       0
                   Customer Stats.Customer Stats           ExecuteSql        400.0     0.0       0
                   Customer Stats.Customer Stats              Process        323.2     2.6       0
```

## Log

```
2026-11-20T04:30:04Z run 20261120T042928Z-v99i-f55a: variant=v99i-buffer-stg-sales data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T04:30:14Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T04:30:26Z PPU: v99i-buffer-stg-sales is c22581d6-175d-489e-b120-eb36a486ebd1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T04:30:44Z PPU: model size in memory before the refresh: 540.6 MB
2026-11-20T04:30:50Z PPU: trace started (full)
2026-11-20T04:30:51Z PPU: refresh started, request 3acb1764-e242-406f-99df-35ded0742a15
2026-11-20T05:13:38Z PPU: refresh refreshed (Completed) 
2026-11-20T05:14:09Z PPU: trace captured 840 events: ProgressReportEnd 799, ExecutionMetrics 32, CommandEnd 9
2026-11-20T05:14:11Z PPU: model size in memory right after the refresh: 660.7 MB
```
