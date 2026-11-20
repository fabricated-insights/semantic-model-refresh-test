# Harness run 20261120T143159Z-v25-f55a

- Task: refresh
- Variant: v25-many-to-many
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 410996cd-6b49-43b5-961e-6c7ce3333aa2
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 939 MB, Power Query 775 MB, duration 1 min, CPU 120 s, rows 3,611,040, model 79 MB (Backup step in XMLA trace)
- Refresh request 3f00747b-736e-422c-8ff1-63bdc9109f65, 2026-11-20T14:34:44.713 to 2026-11-20T14:36:00.757, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v25-many-to-many on PPU data-1m-v1: refreshed, peak 795 MB (2026-11-20T08:44:53Z).
  - Peak change: +144 MB (+18.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 939 MB vs 604 MB (+335 MB), Power Query 775 MB vs 529 MB, model 79 MB vs 73 MB.
- Model size in memory when the full refresh started: 71 MB. The refresh may use the SKU maximum minus this: 102,329 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,995 MB: fits (31%); F16 5,049 MB: fits (19%); F32 10,169 MB: fits (9%); F64 25,529 MB: fits (4%); PPU 102,329 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                                  8e5f1fe2-bf93-4150-9f31-c99850c8b58c TabularSequencePoint         67.5     0.1       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         66.8    19.2       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         65.2    19.1       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         64.8    19.0 2349091
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.6    11.6       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.4    10.4       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637       TabularRefresh          9.2     4.3       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637              Process          8.2     4.3       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637             ReadData          7.9     4.1 1049900
                                                                  <NA>               Commit          4.8     0.0    <NA>
                Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.7     1.5       0
                Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.8     1.5       0
```

## Log

```
2026-11-20T14:34:09Z run 20261120T143159Z-v25-f55a: variant=v25-many-to-many data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T14:34:15Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:34:18Z PPU: v25-many-to-many is 8e5f1fe2-bf93-4150-9f31-c99850c8b58c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:34:39Z PPU: model size in memory before the refresh: 70.6 MB
2026-11-20T14:34:44Z PPU: trace started (full)
2026-11-20T14:34:44Z PPU: refresh started, request 3f00747b-736e-422c-8ff1-63bdc9109f65
2026-11-20T14:36:25Z PPU: refresh refreshed (Completed) 
2026-11-20T14:36:55Z PPU: trace captured 270 events: ProgressReportEnd 250, ExecutionMetrics 10, CommandEnd 10
2026-11-20T14:36:56Z PPU: model size in memory right after the refresh: 98.1 MB
```
