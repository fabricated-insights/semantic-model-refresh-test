# Harness run 20261120T180000Z-v99l-f55a

- Task: refresh
- Variant: v99l-no-calc-columns
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 9d6bdafc-c2b6-4567-95bf-613aa7365950
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 12,901 MB, Power Query 12,766 MB, duration 22 min, CPU 2,265 s, rows 3,292,315, model 158 MB (Backup step in XMLA trace)
- Refresh request 770ffc1d-bb39-4f3c-8b25-cc06e4e91e46, 2026-11-20T18:01:12.937 to 2026-11-20T18:23:20.753, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99l-no-calc-columns on PPU data-1m-v1: refreshed, peak 12,855 MB (2026-11-20T12:46:11Z).
  - Peak change: +46 MB (+0.4%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 12,901 MB vs 604 MB (+12,297 MB), Power Query 12,766 MB vs 529 MB, model 158 MB vs 73 MB.
- Model size in memory when the full refresh started: 168 MB. The refresh may use the SKU maximum minus this: 102,232 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,898 MB: OVER (445%); F16 4,952 MB: OVER (261%); F32 10,072 MB: OVER (128%); F64 25,432 MB: fits (51%); PPU 102,232 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            bd05e14c-0c16-4a5f-9ea0-0eac63361a0c TabularSequencePoint       1315.3     0.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1309.0    25.0       0
                   Customer Stats.Customer Stats       TabularRefresh        928.8     3.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        850.9     0.0       0
                   Customer Stats.Customer Stats           ExecuteSql        609.8     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        457.9    24.9       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        457.5    24.7 2349091
                   Customer Stats.Customer Stats              Process        318.9     3.7       0
                   Customer Stats.Customer Stats             ReadData        317.9     3.1  471482
                                            <NA>               Commit         10.2     0.0    <NA>
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.6     9.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.4     7.4       0
```

## Log

```
2026-11-20T18:00:37Z run 20261120T180000Z-v99l-f55a: variant=v99l-no-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T18:00:48Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T18:00:52Z PPU: v99l-no-calc-columns is bd05e14c-0c16-4a5f-9ea0-0eac63361a0c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T18:01:09Z PPU: model size in memory before the refresh: 167.7 MB
2026-11-20T18:01:12Z PPU: trace started (full)
2026-11-20T18:01:13Z PPU: refresh started, request 770ffc1d-bb39-4f3c-8b25-cc06e4e91e46
2026-11-20T18:23:26Z PPU: refresh refreshed (Completed) 
2026-11-20T18:23:57Z PPU: trace captured 423 events: ProgressReportEnd 402, ExecutionMetrics 11, CommandEnd 10
2026-11-20T18:23:58Z PPU: model size in memory right after the refresh: 194.2 MB
```
