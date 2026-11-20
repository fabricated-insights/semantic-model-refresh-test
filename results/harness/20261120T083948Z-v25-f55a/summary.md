# Harness run 20261120T083948Z-v25-f55a

- Task: refresh
- Variant: v25-many-to-many
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: bad6fbdc-f580-4c87-b5f1-2217211c17e5
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 795 MB, Power Query 728 MB, duration 1 min, CPU 143 s, rows 3,611,040, model 79 MB (Backup step in XMLA trace)
- Refresh request 4db58368-1f1d-4247-bde4-4c9b0c3454bb, 2026-11-20T08:42:41.86 to 2026-11-20T08:44:15.247, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v25-many-to-many on PPU data-1m-v1: refreshed, peak 943 MB (2026-11-19T23:12:29Z).
  - Peak change: -148 MB (-15.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 795 MB vs 666 MB (+129 MB), Power Query 728 MB vs 591 MB, model 79 MB vs 73 MB.
- Model size in memory when the full refresh started: 71 MB. The refresh may use the SKU maximum minus this: 102,329 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,995 MB: fits (27%); F16 5,049 MB: fits (16%); F32 10,169 MB: fits (8%); F64 25,529 MB: fits (3%); PPU 102,329 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                                  8e5f1fe2-bf93-4150-9f31-c99850c8b58c TabularSequencePoint         82.0     0.1       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         81.0    24.7       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         79.4    24.7       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         78.6    24.5 2349091
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.4    12.5       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637       TabularRefresh         11.2     5.8       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.2    11.1       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637              Process         10.2     5.7       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637             ReadData          9.6     5.5 1049900
                                                                  <NA>               Commit          8.1     0.0    <NA>
                Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.3     2.3       0
                Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.0     2.3       0
```

## Log

```
2026-11-20T08:42:04Z run 20261120T083948Z-v25-f55a: variant=v25-many-to-many data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T08:42:11Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:42:14Z PPU: v25-many-to-many is 8e5f1fe2-bf93-4150-9f31-c99850c8b58c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:42:38Z PPU: model size in memory before the refresh: 70.6 MB
2026-11-20T08:42:41Z PPU: trace started (full)
2026-11-20T08:42:42Z PPU: refresh started, request 4db58368-1f1d-4247-bde4-4c9b0c3454bb
2026-11-20T08:44:22Z PPU: refresh refreshed (Completed) 
2026-11-20T08:44:53Z PPU: trace captured 282 events: ProgressReportEnd 250, ExecutionMetrics 22, CommandEnd 10
2026-11-20T08:44:54Z PPU: model size in memory right after the refresh: 98.1 MB
```
