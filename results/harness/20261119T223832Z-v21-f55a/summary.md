# Harness run 20261119T223832Z-v21-f55a

- Task: refresh
- Variant: v21-pq-group-by
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: bbbf91c8-92a9-45d4-95c7-09313898a94f
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 3,500 MB, Power Query 3,315 MB, duration 1 min, CPU 170 s, rows 3,032,622, model 85 MB (Backup step in XMLA trace)
- Refresh request 9e6f2892-6060-4093-a9ce-e3248839faae, 2026-11-19T22:39:40.223 to 2026-11-19T22:41:08.837, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v21-pq-group-by on PPU data-1m-v1: refreshed, peak 3,582 MB (2026-11-17T09:18:48Z).
  - Peak change: -82 MB (-2.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 3,500 MB vs 551 MB (+2,949 MB), Power Query 3,315 MB vs 298 MB, model 85 MB vs 73 MB.
- Model size in memory when the full refresh started: 92 MB. The refresh may use the SKU maximum minus this: 102,308 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,974 MB: OVER (118%); F16 5,028 MB: fits (70%); F32 10,148 MB: fits (34%); F64 25,508 MB: fits (14%); PPU 102,308 MB: fits (3%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  b551b92f-7694-4efc-9e6f-4c13eaec6dcf TabularSequencePoint         78.3     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh         76.8     2.1       0
                         Customer Stats.Customer Stats           ExecuteSql         66.2     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         56.7    18.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         55.2    18.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         54.8    18.5 2349091
                         Customer Stats.Customer Stats              Process         10.6     2.1       0
                         Customer Stats.Customer Stats             ReadData         10.1     1.7  471482
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.7    11.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.6     9.6       0
                                                  <NA>               Commit          5.8     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.0     1.8       0
```

## Log

```
2026-11-19T22:39:05Z run 20261119T223832Z-v21-f55a: variant=v21-pq-group-by data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T22:39:15Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:39:20Z PPU: v21-pq-group-by is b551b92f-7694-4efc-9e6f-4c13eaec6dcf, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:39:36Z PPU: model size in memory before the refresh: 92.1 MB
2026-11-19T22:39:40Z PPU: trace started (full)
2026-11-19T22:39:40Z PPU: refresh started, request 9e6f2892-6060-4093-a9ce-e3248839faae
2026-11-19T22:41:20Z PPU: refresh refreshed (Completed) 
2026-11-19T22:41:51Z PPU: trace captured 300 events: ProgressReportEnd 255, ExecutionMetrics 34, CommandEnd 11
2026-11-19T22:41:52Z PPU: model size in memory right after the refresh: 118.6 MB
```
