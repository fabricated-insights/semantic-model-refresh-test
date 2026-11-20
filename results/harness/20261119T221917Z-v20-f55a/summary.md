# Harness run 20261119T221917Z-v20-f55a

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6f597c82-f16f-4456-a4b0-b4d0f210b5a2
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 5,105 MB, Power Query 4,894 MB, duration 14 min, CPU 1,284 s, rows 2,561,140, model 72 MB (Backup step in XMLA trace)
- Refresh request 8abadb15-f31c-444f-becc-841fd16688c9, 2026-11-19T22:23:13.533 to 2026-11-19T22:37:01.497, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v20-pq-sort on PPU data-1m-v1: refreshed, peak 5,219 MB (2026-11-17T09:03:52Z).
  - Peak change: -114 MB (-2.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 5,105 MB vs 551 MB (+4,554 MB), Power Query 4,894 MB vs 298 MB, model 72 MB vs 73 MB.
- Model size in memory when the full refresh started: 65 MB. The refresh may use the SKU maximum minus this: 102,335 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,001 MB: OVER (170%); F16 5,055 MB: OVER (101%); F32 10,175 MB: fits (50%); F64 25,535 MB: fits (20%); PPU 102,335 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    6507a4e8-9e64-476c-92dd-186299e9d72f TabularSequencePoint        820.7     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        802.3    18.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        614.2    18.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        613.9    18.6 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        188.0     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.0     8.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.8     6.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.6     1.7       0
                                                                    <NA>               Commit          4.5     0.0    <NA>
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.0     0.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.5     1.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.4     1.5  104990
```

## Log

```
2026-11-19T22:22:00Z run 20261119T221917Z-v20-f55a: variant=v20-pq-sort data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T22:22:12Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:22:15Z PPU: v20-pq-sort is 6507a4e8-9e64-476c-92dd-186299e9d72f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:23:09Z PPU: model size in memory before the refresh: 65.3 MB
2026-11-19T22:23:13Z PPU: trace started (full)
2026-11-19T22:23:13Z PPU: refresh started, request 8abadb15-f31c-444f-becc-841fd16688c9
2026-11-19T22:37:26Z PPU: refresh refreshed (Completed) 
2026-11-19T22:37:56Z PPU: trace captured 282 events: ProgressReportEnd 237, ExecutionMetrics 34, CommandEnd 11
2026-11-19T22:37:58Z PPU: model size in memory right after the refresh: 91.9 MB
```
