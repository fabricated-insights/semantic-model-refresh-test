# Harness run 20261119T234723Z-v34-f55a

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a4137ddf-d49e-4d44-9922-39c9c587e053
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 547 MB, Power Query 457 MB, duration 1 min, CPU 104 s, rows 2,847,496, model 74 MB (Backup step in XMLA trace)
- Refresh request 48c46a60-94ee-44f9-94d1-c04af6c3c48d, 2026-11-19T23:50:13.903 to 2026-11-19T23:51:24.46, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v34-auto-date-time-no-date-table on PPU data-1m-v1: refreshed, peak 620 MB (2026-11-17T08:53:09Z).
  - Peak change: -73 MB (-11.8%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 547 MB vs 551 MB (-4 MB), Power Query 457 MB vs 298 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 102,330 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (18%); F16 5,050 MB: fits (11%); F32 10,170 MB: fits (5%); F64 25,530 MB: fits (2%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    7023f118-b5f8-4a7b-9811-b16c34d32708 TabularSequencePoint         60.4     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         59.6    17.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         57.0    17.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         52.4    17.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         16.8    18.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         16.6    16.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.5     1.7       0
                                                                    <NA>               Commit          5.4     0.0    <NA>
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.6     0.6       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          2.8     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          2.8     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          2.8     0.0       0
```

## Log

```
2026-11-19T23:49:39Z run 20261119T234723Z-v34-f55a: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T23:49:46Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:49:49Z PPU: v34-auto-date-time-no-date-table is 7023f118-b5f8-4a7b-9811-b16c34d32708, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:50:10Z PPU: model size in memory before the refresh: 70.3 MB
2026-11-19T23:50:13Z PPU: trace started (full)
2026-11-19T23:50:14Z PPU: refresh started, request 48c46a60-94ee-44f9-94d1-c04af6c3c48d
2026-11-19T23:51:54Z PPU: refresh refreshed (Completed) 
2026-11-19T23:52:25Z PPU: trace captured 449 events: ProgressReportEnd 404, ExecutionMetrics 34, CommandEnd 11
2026-11-19T23:52:25Z PPU: model size in memory right after the refresh: 96.9 MB
```
