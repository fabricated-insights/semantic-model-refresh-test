# Harness run 20261120T132826Z-v99q-f55a

- Task: refresh
- Variant: v99q-customer-stats
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ce85e895-e3d8-4057-b1a8-ea74cb8c6bc0
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 3,514 MB, Power Query 3,280 MB, duration 1 min, CPU 194 s, rows 22,055,454, model 114 MB (Backup step in XMLA trace)
- Refresh request 69cd4cad-9ca3-46f3-91e8-b95d2bfe4371, 2026-11-20T13:32:06.77 to 2026-11-20T13:33:37.367, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99q-customer-stats on PPU data-1m-v1: refreshed, peak 3,472 MB (2026-11-20T07:09:13Z).
  - Peak change: +42 MB (+1.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 3,514 MB vs 666 MB (+2,848 MB), Power Query 3,280 MB vs 591 MB, model 114 MB vs 73 MB.
- Model size in memory when the full refresh started: 127 MB. The refresh may use the SKU maximum minus this: 102,273 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,939 MB: OVER (120%); F16 4,993 MB: fits (70%); F32 10,113 MB: fits (35%); F64 25,473 MB: fits (14%); PPU 102,273 MB: fits (3%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            a0c7fd43-3720-419e-a1cf-b0e193d83052 TabularSequencePoint         77.6     0.2       0
                   Customer Stats.Customer Stats       TabularRefresh         76.1     2.3       0
                   Customer Stats.Customer Stats           ExecuteSql         66.0     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         60.1    20.4       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         57.5    20.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         57.0    20.2 2349091
                   Customer Stats.Customer Stats              Process         10.0     2.3       0
                   Customer Stats.Customer Stats             ReadData          9.4     1.9  471482
                                            <NA>               Commit          8.5     0.0    <NA>
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.2    10.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.0     8.0       0
                          Sales.Sales Line Label       TabularRefresh          5.3     5.0       0
```

## Log

```
2026-11-20T13:31:25Z run 20261120T132826Z-v99q-f55a: variant=v99q-customer-stats data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T13:31:32Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:31:35Z PPU: v99q-customer-stats is a0c7fd43-3720-419e-a1cf-b0e193d83052, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:32:03Z PPU: model size in memory before the refresh: 127.3 MB
2026-11-20T13:32:06Z PPU: trace started (full)
2026-11-20T13:32:06Z PPU: refresh started, request 69cd4cad-9ca3-46f3-91e8-b95d2bfe4371
2026-11-20T13:33:47Z PPU: refresh refreshed (Completed) 
2026-11-20T13:34:17Z PPU: trace captured 425 events: ProgressReportEnd 405, ExecutionMetrics 10, CommandEnd 10
2026-11-20T13:34:18Z PPU: model size in memory right after the refresh: 162.1 MB
```
