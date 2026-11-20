# Harness run 20261120T145718Z-v30-f55a

- Task: refresh
- Variant: v30-double-instead-of-fixed
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 45033c20-59cf-4d19-9657-7642752c6bb6
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 614 MB, Power Query 334 MB, duration 1 min, CPU 102 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request e303d73a-5c1c-4b3a-b46c-e3370e546c63, 2026-11-20T14:58:22.343 to 2026-11-20T14:59:30.253, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v30-double-instead-of-fixed on PPU data-1m-v1: refreshed, peak 983 MB (2026-11-20T09:12:10Z).
  - Peak change: -369 MB (-37.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 614 MB vs 604 MB (+10 MB), Power Query 334 MB vs 529 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (20%); F16 5,054 MB: fits (12%); F32 10,174 MB: fits (6%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    9e47cacd-824d-4e24-8998-6f639088fddf TabularSequencePoint         59.5     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.7    21.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         56.0    21.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         53.8    21.7 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.9    13.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.6    11.6       0
                                                                    <NA>               Commit          5.0     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.8     1.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.8     0.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.6     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          2.6     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.6     1.9       0
```

## Log

```
2026-11-20T14:57:54Z run 20261120T145718Z-v30-f55a: variant=v30-double-instead-of-fixed data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T14:57:59Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:58:02Z PPU: v30-double-instead-of-fixed is 9e47cacd-824d-4e24-8998-6f639088fddf, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:58:18Z PPU: model size in memory before the refresh: 66.4 MB
2026-11-20T14:58:22Z PPU: trace started (full)
2026-11-20T14:58:22Z PPU: refresh started, request e303d73a-5c1c-4b3a-b46c-e3370e546c63
2026-11-20T14:59:32Z PPU: refresh refreshed (Completed) 
2026-11-20T15:00:03Z PPU: trace captured 256 events: ProgressReportEnd 236, ExecutionMetrics 10, CommandEnd 10
2026-11-20T15:00:04Z PPU: model size in memory right after the refresh: 92.9 MB
```
