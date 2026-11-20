# Harness run 20261120T185737Z-v99q-f55a

- Task: refresh
- Variant: v99q-customer-stats
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1e16a8e1-ab34-4415-a812-01024063cc72
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 3,511 MB, Power Query 3,281 MB, duration 1 min, CPU 197 s, rows 22,055,454, model 114 MB (Backup step in XMLA trace)
- Refresh request b362d1fd-9ddc-4a68-9b09-f9d7213ff6bd, 2026-11-20T18:58:53.703 to 2026-11-20T19:00:24.013, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99q-customer-stats on PPU data-1m-v1: refreshed, peak 3,514 MB (2026-11-20T13:34:18Z).
  - Peak change: -3 MB (-0.1%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 3,511 MB vs 604 MB (+2,907 MB), Power Query 3,281 MB vs 529 MB, model 114 MB vs 73 MB.
- Model size in memory when the full refresh started: 127 MB. The refresh may use the SKU maximum minus this: 102,273 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,939 MB: OVER (119%); F16 4,993 MB: fits (70%); F32 10,113 MB: fits (35%); F64 25,473 MB: fits (14%); PPU 102,273 MB: fits (3%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            a0c7fd43-3720-419e-a1cf-b0e193d83052 TabularSequencePoint         77.8     0.2       0
                   Customer Stats.Customer Stats       TabularRefresh         76.1     2.3       0
                   Customer Stats.Customer Stats           ExecuteSql         65.1     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.9    20.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         58.1    20.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         57.7    20.0 2349091
                   Customer Stats.Customer Stats              Process         10.9     2.2       0
                   Customer Stats.Customer Stats             ReadData         10.2     1.8  471482
                                            <NA>               Commit          8.2     0.0    <NA>
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.7     9.7       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.5     7.4       0
                          Sales.Sales Line Label       TabularRefresh          5.7     5.4       0
```

## Log

```
2026-11-20T18:58:23Z run 20261120T185737Z-v99q-f55a: variant=v99q-customer-stats data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T18:58:30Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T18:58:34Z PPU: v99q-customer-stats is a0c7fd43-3720-419e-a1cf-b0e193d83052, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T18:58:50Z PPU: model size in memory before the refresh: 127.3 MB
2026-11-20T18:58:53Z PPU: trace started (full)
2026-11-20T18:58:53Z PPU: refresh started, request b362d1fd-9ddc-4a68-9b09-f9d7213ff6bd
2026-11-20T19:00:34Z PPU: refresh refreshed (Completed) 
2026-11-20T19:01:04Z PPU: trace captured 425 events: ProgressReportEnd 405, ExecutionMetrics 10, CommandEnd 10
2026-11-20T19:01:05Z PPU: model size in memory right after the refresh: 162.1 MB
```
