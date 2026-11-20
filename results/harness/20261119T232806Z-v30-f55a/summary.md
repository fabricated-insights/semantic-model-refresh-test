# Harness run 20261119T232806Z-v30-f55a

- Task: refresh
- Variant: v30-double-instead-of-fixed
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e59aa29e-baa7-4f37-b5c5-3332ef8e40bc
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 758 MB, Power Query 690 MB, duration 1 min, CPU 112 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request e8131f9c-60f1-4638-8680-b5462f911399, 2026-11-19T23:31:11.42 to 2026-11-19T23:32:28.937, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v30-double-instead-of-fixed on PPU data-1m-v1: refreshed, peak 607 MB (2026-11-17T06:53:06Z).
  - Peak change: +151 MB (+24.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 758 MB vs 551 MB (+207 MB), Power Query 690 MB vs 298 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (25%); F16 5,054 MB: fits (15%); F32 10,174 MB: fits (7%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    9e47cacd-824d-4e24-8998-6f639088fddf TabularSequencePoint         68.5     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         67.8    22.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         64.4    22.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         63.8    21.9 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.2    12.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.0    10.9       0
                                                                    <NA>               Commit          5.9     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.8     1.9       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          5.2     0.6       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          4.4     0.0       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          3.6     0.1       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          3.4     0.1       0
```

## Log

```
2026-11-19T23:30:23Z run 20261119T232806Z-v30-f55a: variant=v30-double-instead-of-fixed data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T23:30:29Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:30:34Z PPU: v30-double-instead-of-fixed is 9e47cacd-824d-4e24-8998-6f639088fddf, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:31:07Z PPU: model size in memory before the refresh: 66.4 MB
2026-11-19T23:31:11Z PPU: trace started (full)
2026-11-19T23:31:11Z PPU: refresh started, request e8131f9c-60f1-4638-8680-b5462f911399
2026-11-19T23:32:52Z PPU: refresh refreshed (Completed) 
2026-11-19T23:33:22Z PPU: trace captured 282 events: ProgressReportEnd 237, ExecutionMetrics 34, CommandEnd 11
2026-11-19T23:33:23Z PPU: model size in memory right after the refresh: 92.9 MB
```
