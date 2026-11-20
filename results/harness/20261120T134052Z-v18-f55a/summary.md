# Harness run 20261120T134052Z-v18-f55a

- Task: refresh
- Variant: v18-pq-10m-summary
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f806a54c-b0f7-422a-961a-1480668bb022
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 2,064 MB, Power Query 1,789 MB, duration 2 min, CPU 214 s, rows 2,561,730, model 73 MB (Backup step in XMLA trace)
- Refresh request ec06935b-7e25-4adf-8b1e-de6bcb9578fb, 2026-11-20T13:41:52.493 to 2026-11-20T13:43:38.94, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v18-pq-10m-summary on PPU data-1m-v1: refreshed, peak 1,920 MB (2026-11-20T07:21:11Z).
  - Peak change: +144 MB (+7.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 2,064 MB vs 604 MB (+1,460 MB), Power Query 1,789 MB vs 529 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (69%); F16 5,054 MB: fits (41%); F32 10,174 MB: fits (20%); F64 25,534 MB: fits (8%); PPU 102,334 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  5f501e01-52ef-4e24-81c1-aa3cafd4c095 TabularSequencePoint         96.1     0.1       0
                 Store Year Summary.Store Year Summary       TabularRefresh         95.5     0.0       0
                 Store Year Summary.Store Year Summary           ExecuteSql         95.3     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         73.0    22.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         70.9    22.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         70.4    21.8 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.1    12.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.9    10.9       0
                                                  <NA>               Commit          5.4     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.1     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.7     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.5     1.8  104990
```

## Log

```
2026-11-20T13:41:22Z run 20261120T134052Z-v18-f55a: variant=v18-pq-10m-summary data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T13:41:27Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:41:31Z PPU: v18-pq-10m-summary is 5f501e01-52ef-4e24-81c1-aa3cafd4c095, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:41:48Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-20T13:41:52Z PPU: trace started (full)
2026-11-20T13:41:52Z PPU: refresh started, request ec06935b-7e25-4adf-8b1e-de6bcb9578fb
2026-11-20T13:44:03Z PPU: refresh refreshed (Completed) 
2026-11-20T13:44:33Z PPU: trace captured 274 events: ProgressReportEnd 254, ExecutionMetrics 10, CommandEnd 10
2026-11-20T13:44:34Z PPU: model size in memory right after the refresh: 92.7 MB
```
