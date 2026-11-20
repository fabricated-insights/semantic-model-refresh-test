# Harness run 20261120T014621Z-v99c-f55a

- Task: refresh
- Variant: v99c-crossjoin-only
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 137f00a8-b592-47a5-99f5-e3c3e5df9fed
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 26,157 MB, Power Query 25,996 MB, duration 33 min, CPU 7,080 s, rows 35,817,730, model 358 MB (Backup step in XMLA trace)
- Refresh request 83103344-4822-4697-8dcf-172c39b0a46d, 2026-11-20T01:49:49.037 to 2026-11-20T02:23:11.783, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99c-crossjoin-only on PPU data-1m-v1: refreshed, peak 25,918 MB (2026-11-17T20:36:37Z).
  - Peak change: +239 MB (+0.9%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 26,157 MB vs 551 MB (+25,606 MB), Power Query 25,996 MB vs 298 MB, model 358 MB vs 73 MB.
- Model size in memory when the full refresh started: 380 MB. The refresh may use the SKU maximum minus this: 102,020 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,686 MB: OVER (974%); F16 4,740 MB: OVER (552%); F32 9,860 MB: OVER (265%); F64 25,220 MB: OVER (104%); PPU 102,020 MB: fits (26%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            364f4109-e09b-4cda-a773-d642978613b4 TabularSequencePoint       1977.4     0.5       0
                           Sales Flat.Sales Flat       TabularRefresh       1887.3    82.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1850.6    26.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process       1298.0    26.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData       1297.6    26.5 2349091
                           Sales Flat.Sales Flat              Process       1008.1    82.2       0
                           Sales Flat.Sales Flat             ReadData       1007.0    82.2 2349091
                           Sales Flat.Sales Flat           ExecuteSql        879.2     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        598.8     2.6       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        552.5     0.0       0
                   Customer Stats.Customer Stats           ExecuteSql        372.2     0.0       0
                   Customer Stats.Customer Stats              Process        226.5     2.5       0
```

## Log

```
2026-11-20T01:49:06Z run 20261120T014621Z-v99c-f55a: variant=v99c-crossjoin-only data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T01:49:16Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T01:49:23Z PPU: v99c-crossjoin-only is 364f4109-e09b-4cda-a773-d642978613b4, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T01:49:45Z PPU: model size in memory before the refresh: 380.4 MB
2026-11-20T01:49:48Z PPU: trace started (full)
2026-11-20T01:49:49Z PPU: refresh started, request 83103344-4822-4697-8dcf-172c39b0a46d
2026-11-20T02:23:34Z PPU: refresh refreshed (Completed) 
2026-11-20T02:24:05Z PPU: trace captured 640 events: ProgressReportEnd 593, ExecutionMetrics 36, CommandEnd 11
2026-11-20T02:24:08Z PPU: model size in memory right after the refresh: 486.6 MB
```
