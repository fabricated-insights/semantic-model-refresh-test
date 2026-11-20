# Harness run 20261119T230711Z-v25-f55a

- Task: refresh
- Variant: v25-many-to-many
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 43ed7a29-829c-4a49-b038-8b9f94140571
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 943 MB, Power Query 831 MB, duration 1 min, CPU 121 s, rows 3,611,040, model 79 MB (Backup step in XMLA trace)
- Refresh request 376fdd73-b115-4211-9f93-d06c7c31976f, 2026-11-19T23:10:18.743 to 2026-11-19T23:11:33.493, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v25-many-to-many on PPU data-1m-v1: refreshed, peak 695 MB (2026-11-17T06:21:03Z).
  - Peak change: +248 MB (+35.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 943 MB vs 551 MB (+392 MB), Power Query 831 MB vs 298 MB, model 79 MB vs 73 MB.
- Model size in memory when the full refresh started: 71 MB. The refresh may use the SKU maximum minus this: 102,329 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,995 MB: fits (31%); F16 5,049 MB: fits (19%); F32 10,169 MB: fits (9%); F64 25,529 MB: fits (4%); PPU 102,329 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                                  8e5f1fe2-bf93-4150-9f31-c99850c8b58c TabularSequencePoint         66.6     0.1       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         65.8    19.5       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         63.8    19.5       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         62.8    19.3 2349091
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637       TabularRefresh         13.1     5.8       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637              Process         12.9     5.7       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637             ReadData         12.5     5.5 1049900
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.6    12.8       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.4    11.4       0
                      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          7.5     0.1       0
                      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          7.4     0.0       0
                                                                  <NA>               Commit          5.2     0.0    <NA>
```

## Log

```
2026-11-19T23:09:41Z run 20261119T230711Z-v25-f55a: variant=v25-many-to-many data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T23:09:47Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:09:52Z PPU: v25-many-to-many is 8e5f1fe2-bf93-4150-9f31-c99850c8b58c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:10:15Z PPU: model size in memory before the refresh: 70.6 MB
2026-11-19T23:10:18Z PPU: trace started (full)
2026-11-19T23:10:18Z PPU: refresh started, request 376fdd73-b115-4211-9f93-d06c7c31976f
2026-11-19T23:11:59Z PPU: refresh refreshed (Completed) 
2026-11-19T23:12:29Z PPU: trace captured 296 events: ProgressReportEnd 251, ExecutionMetrics 34, CommandEnd 11
2026-11-19T23:12:30Z PPU: model size in memory right after the refresh: 98.1 MB
```
