# Harness run 20261119T224213Z-v22-f55a

- Task: refresh
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1d4c4d81-938d-4d20-952d-59cd1df49da6
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 620 MB, Power Query 340 MB, duration 1 min, CPU 125 s, rows 21,353,868, model 101 MB (Backup step in XMLA trace)
- Refresh request e9b63968-cd44-4160-ba4b-c750ad9b3ca0, 2026-11-19T22:45:01.613 to 2026-11-19T22:46:23.527, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v22-dax-calc-columns on PPU data-1m-v1: refreshed, peak 621 MB (2026-11-16T23:00:41Z).
  - Peak change: -1 MB (-0.2%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 620 MB vs 551 MB (+69 MB), Power Query 340 MB vs 298 MB, model 101 MB vs 73 MB.
- Model size in memory when the full refresh started: 98 MB. The refresh may use the SKU maximum minus this: 102,302 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,968 MB: fits (21%); F16 5,022 MB: fits (12%); F32 10,142 MB: fits (6%); F64 25,502 MB: fits (2%); PPU 102,302 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  f04681eb-fd6e-44c2-902a-dad6c2273007 TabularSequencePoint         68.9     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         61.0    24.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         58.4    24.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         57.8    23.9 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.8    11.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.5     8.5       0
                                                  <NA>               Commit          8.2     0.0    <NA>
                                Sales.Sales Line Label       TabularRefresh          5.9     5.6       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.4     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.8     1.9  104990
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.7     0.1       0
```

## Log

```
2026-11-19T22:44:28Z run 20261119T224213Z-v22-f55a: variant=v22-dax-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T22:44:34Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:44:38Z PPU: v22-dax-calc-columns is f04681eb-fd6e-44c2-902a-dad6c2273007, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:44:58Z PPU: model size in memory before the refresh: 97.8 MB
2026-11-19T22:45:01Z PPU: trace started (full)
2026-11-19T22:45:01Z PPU: refresh started, request e9b63968-cd44-4160-ba4b-c750ad9b3ca0
2026-11-19T22:46:42Z PPU: refresh refreshed (Completed) 
2026-11-19T22:47:13Z PPU: trace captured 322 events: ProgressReportEnd 277, ExecutionMetrics 34, CommandEnd 11
2026-11-19T22:47:14Z PPU: model size in memory right after the refresh: 132.6 MB
```
