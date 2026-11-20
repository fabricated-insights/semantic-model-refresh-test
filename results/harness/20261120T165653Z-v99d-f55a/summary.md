# Harness run 20261120T165653Z-v99d-f55a

- Task: refresh
- Variant: v99d-power-query
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ee59a2cb-e8e8-4315-9841-17c85f21315d
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 16,027 MB, Power Query 15,904 MB, duration 30 min, CPU 3,486 s, rows 22,085,043, model 185 MB (Backup step in XMLA trace)
- Refresh request de75370c-3589-429b-88bf-007e54cc3aec, 2026-11-20T16:59:31.26 to 2026-11-20T17:30:11.913, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99d-power-query on PPU data-1m-v1: refreshed, peak 16,009 MB (2026-11-20T11:27:11Z).
  - Peak change: +18 MB (+0.1%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 16,027 MB vs 604 MB (+15,423 MB), Power Query 15,904 MB vs 529 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 102,202 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (559%); F16 4,922 MB: OVER (326%); F32 10,042 MB: OVER (160%); F64 25,402 MB: fits (63%); PPU 102,202 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            2fb3d992-aae5-40d4-ac2d-710eb2f49931 TabularSequencePoint       1823.6     0.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1772.9    27.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process       1101.0    27.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData       1100.7    27.3 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        671.7     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        511.5     3.1       0
                   Customer Stats.Customer Stats           ExecuteSql        278.6     0.0       0
                   Customer Stats.Customer Stats              Process        232.9     3.1       0
                   Customer Stats.Customer Stats             ReadData        231.9     2.4  471482
                                            <NA>               Commit         13.2     0.0    <NA>
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.4     8.8       0
                          Sales.Sales Line Label       TabularRefresh          6.2     5.9       0
```

## Log

```
2026-11-20T16:58:55Z run 20261120T165653Z-v99d-f55a: variant=v99d-power-query data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T16:59:00Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T16:59:06Z PPU: v99d-power-query is 2fb3d992-aae5-40d4-ac2d-710eb2f49931, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T16:59:27Z PPU: model size in memory before the refresh: 197.8 MB
2026-11-20T16:59:31Z PPU: trace started (full)
2026-11-20T16:59:31Z PPU: refresh started, request de75370c-3589-429b-88bf-007e54cc3aec
2026-11-20T17:30:16Z PPU: refresh refreshed (Completed) 
2026-11-20T17:30:47Z PPU: trace captured 463 events: ProgressReportEnd 442, ExecutionMetrics 11, CommandEnd 10
2026-11-20T17:30:52Z PPU: model size in memory right after the refresh: 232.6 MB
```
