# Harness run 20261120T055621Z-v99l-f55a

- Task: refresh
- Variant: v99l-no-calc-columns
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 31586227-e6d6-4a64-b43f-5f4b5bcd1e66
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 12,995 MB, Power Query 12,898 MB, duration 23 min, CPU 2,327 s, rows 3,292,315, model 158 MB (Backup step in XMLA trace)
- Refresh request dbe0fbc2-d043-482d-a854-5a1ca373cf34, 2026-11-20T05:59:03.767 to 2026-11-20T06:22:15.29, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99l-no-calc-columns on PPU data-1m-v1: refreshed, peak 12,878 MB (2026-11-17T15:59:04Z).
  - Peak change: +117 MB (+0.9%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 12,995 MB vs 551 MB (+12,444 MB), Power Query 12,898 MB vs 298 MB, model 158 MB vs 73 MB.
- Model size in memory when the full refresh started: 168 MB. The refresh may use the SKU maximum minus this: 102,232 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,898 MB: OVER (448%); F16 4,952 MB: OVER (262%); F32 10,072 MB: OVER (129%); F64 25,432 MB: fits (51%); PPU 102,232 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            bd05e14c-0c16-4a5f-9ea0-0eac63361a0c TabularSequencePoint       1378.1     0.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1374.8    24.6       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process       1114.3    24.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData       1113.9    24.4 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        260.4     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        219.0     2.4       0
                   Customer Stats.Customer Stats           ExecuteSql        152.3     0.0       0
                   Customer Stats.Customer Stats              Process         66.5     2.4       0
                   Customer Stats.Customer Stats             ReadData         65.9     1.9  471482
                                            <NA>               Commit         10.6     0.0    <NA>
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.1     8.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.9     6.9       0
```

## Log

```
2026-11-20T05:58:26Z run 20261120T055621Z-v99l-f55a: variant=v99l-no-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T05:58:35Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T05:58:39Z PPU: v99l-no-calc-columns is bd05e14c-0c16-4a5f-9ea0-0eac63361a0c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T05:59:00Z PPU: model size in memory before the refresh: 167.7 MB
2026-11-20T05:59:03Z PPU: trace started (full)
2026-11-20T05:59:03Z PPU: refresh started, request dbe0fbc2-d043-482d-a854-5a1ca373cf34
2026-11-20T06:22:17Z PPU: refresh refreshed (Completed) 
2026-11-20T06:22:48Z PPU: trace captured 450 events: ProgressReportEnd 403, ExecutionMetrics 36, CommandEnd 11
2026-11-20T06:22:49Z PPU: model size in memory right after the refresh: 194.2 MB
```
