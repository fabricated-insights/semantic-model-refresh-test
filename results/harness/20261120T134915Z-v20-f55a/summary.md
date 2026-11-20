# Harness run 20261120T134915Z-v20-f55a

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 277e885d-a99a-4591-8396-ed810a1d28f0
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 5,156 MB, Power Query 4,918 MB, duration 5 min, CPU 408 s, rows 2,561,140, model 72 MB (Backup step in XMLA trace)
- Refresh request 4697a471-d0df-4c70-9ec5-4d8b4ebc2ee0, 2026-11-20T13:50:18.497 to 2026-11-20T13:55:46.27, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v20-pq-sort on PPU data-1m-v1: refreshed, peak 4,951 MB (2026-11-20T08:01:41Z).
  - Peak change: +205 MB (+4.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 5,156 MB vs 604 MB (+4,552 MB), Power Query 4,918 MB vs 529 MB, model 72 MB vs 73 MB.
- Model size in memory when the full refresh started: 65 MB. The refresh may use the SKU maximum minus this: 102,335 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,001 MB: OVER (172%); F16 5,055 MB: OVER (102%); F32 10,175 MB: fits (51%); F64 25,535 MB: fits (20%); PPU 102,335 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  6507a4e8-9e64-476c-92dd-186299e9d72f TabularSequencePoint        319.7     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        315.5    20.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        209.3    20.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        208.9    20.1 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        106.1     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.6    10.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.4     9.1       0
                                                  <NA>               Commit          5.2     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.3     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.2     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.0     1.9  104990
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.3     0.1       0
```

## Log

```
2026-11-20T13:49:47Z run 20261120T134915Z-v20-f55a: variant=v20-pq-sort data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T13:49:55Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:50:00Z PPU: v20-pq-sort is 6507a4e8-9e64-476c-92dd-186299e9d72f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:50:14Z PPU: model size in memory before the refresh: 65.3 MB
2026-11-20T13:50:18Z PPU: trace started (full)
2026-11-20T13:50:18Z PPU: refresh started, request 4697a471-d0df-4c70-9ec5-4d8b4ebc2ee0
2026-11-20T13:55:59Z PPU: refresh refreshed (Completed) 
2026-11-20T13:56:33Z PPU: trace captured 256 events: ProgressReportEnd 236, ExecutionMetrics 10, CommandEnd 10
2026-11-20T13:56:34Z PPU: model size in memory right after the refresh: 91.9 MB
```
