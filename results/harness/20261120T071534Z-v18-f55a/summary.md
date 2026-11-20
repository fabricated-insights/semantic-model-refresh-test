# Harness run 20261120T071534Z-v18-f55a

- Task: refresh
- Variant: v18-pq-10m-summary
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 7ba01fbc-6cf2-4847-a12a-e21ee07d8c07
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,920 MB, Power Query 1,667 MB, duration 2 min, CPU 238 s, rows 2,561,730, model 73 MB (Backup step in XMLA trace)
- Refresh request 1e31800c-03b4-4c3b-9c1b-4cfeddf2b991, 2026-11-20T07:18:29.617 to 2026-11-20T07:20:29.183, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v18-pq-10m-summary on PPU data-1m-v1: refreshed, peak 1,834 MB (2026-11-19T21:59:00Z).
  - Peak change: +86 MB (+4.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 1,920 MB vs 666 MB (+1,254 MB), Power Query 1,667 MB vs 591 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (64%); F16 5,054 MB: fits (38%); F32 10,174 MB: fits (19%); F64 25,534 MB: fits (8%); PPU 102,334 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  5f501e01-52ef-4e24-81c1-aa3cafd4c095 TabularSequencePoint        108.6     0.1       0
                 Store Year Summary.Store Year Summary       TabularRefresh        108.2     0.1       0
                 Store Year Summary.Store Year Summary           ExecuteSql        108.1     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         85.4    23.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         83.3    23.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         82.8    23.6 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.5    12.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.2    11.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.9     2.4       0
                                                  <NA>               Commit          6.7     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.2     2.3       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.1     2.2  104990
```

## Log

```
2026-11-20T07:17:52Z run 20261120T071534Z-v18-f55a: variant=v18-pq-10m-summary data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T07:17:59Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:18:03Z PPU: v18-pq-10m-summary is 5f501e01-52ef-4e24-81c1-aa3cafd4c095, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:18:26Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-20T07:18:29Z PPU: trace started (full)
2026-11-20T07:18:29Z PPU: refresh started, request 1e31800c-03b4-4c3b-9c1b-4cfeddf2b991
2026-11-20T07:20:40Z PPU: refresh refreshed (Completed) 
2026-11-20T07:21:11Z PPU: trace captured 286 events: ProgressReportEnd 254, ExecutionMetrics 22, CommandEnd 10
2026-11-20T07:21:11Z PPU: model size in memory right after the refresh: 92.7 MB
```
