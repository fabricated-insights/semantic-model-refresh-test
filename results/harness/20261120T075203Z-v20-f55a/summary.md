# Harness run 20261120T075203Z-v20-f55a

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 28ba8bb2-0483-4d02-a26b-310dc0ebfd41
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 4,951 MB, Power Query 4,763 MB, duration 6 min, CPU 421 s, rows 2,561,140, model 72 MB (Backup step in XMLA trace)
- Refresh request a3bbe318-ffe6-4b2a-9125-02aaf4ec2757, 2026-11-20T07:54:59.363 to 2026-11-20T08:01:08.027, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v20-pq-sort on PPU data-1m-v1: refreshed, peak 5,105 MB (2026-11-19T22:37:57Z).
  - Peak change: -154 MB (-3.0%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 4,951 MB vs 666 MB (+4,285 MB), Power Query 4,763 MB vs 591 MB, model 72 MB vs 73 MB.
- Model size in memory when the full refresh started: 65 MB. The refresh may use the SKU maximum minus this: 102,335 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,001 MB: OVER (165%); F16 5,055 MB: fits (98%); F32 10,175 MB: fits (49%); F64 25,535 MB: fits (19%); PPU 102,335 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    6507a4e8-9e64-476c-92dd-186299e9d72f TabularSequencePoint        360.0     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        358.2    25.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        242.6    25.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        242.2    25.4 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        115.5     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.0    10.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.8     8.8       0
                                                                    <NA>               Commit          5.4     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.9     1.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.8     0.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.6     1.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.5     1.8  104990
```

## Log

```
2026-11-20T07:54:20Z run 20261120T075203Z-v20-f55a: variant=v20-pq-sort data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T07:54:29Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:54:33Z PPU: v20-pq-sort is 6507a4e8-9e64-476c-92dd-186299e9d72f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:54:55Z PPU: model size in memory before the refresh: 65.3 MB
2026-11-20T07:54:59Z PPU: trace started (full)
2026-11-20T07:54:59Z PPU: refresh started, request a3bbe318-ffe6-4b2a-9125-02aaf4ec2757
2026-11-20T08:01:10Z PPU: refresh refreshed (Completed) 
2026-11-20T08:01:41Z PPU: trace captured 268 events: ProgressReportEnd 236, ExecutionMetrics 22, CommandEnd 10
2026-11-20T08:01:42Z PPU: model size in memory right after the refresh: 91.9 MB
```
