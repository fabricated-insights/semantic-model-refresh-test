# Harness run 20261120T093210Z-v34-f55a

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a3690ff3-694f-4854-aa95-db839f3c36a3
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 668 MB, Power Query 590 MB, duration 2 min, CPU 164 s, rows 2,847,496, model 74 MB (Backup step in XMLA trace)
- Refresh request 78e57f7f-0ce3-492e-99ba-31e97bd5e3bf, 2026-11-20T09:35:01.713 to 2026-11-20T09:36:59.687, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v34-auto-date-time-no-date-table on PPU data-1m-v1: refreshed, peak 547 MB (2026-11-19T23:52:25Z).
  - Peak change: +121 MB (+22.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 668 MB vs 666 MB (+2 MB), Power Query 590 MB vs 591 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 102,330 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (22%); F16 5,050 MB: fits (13%); F32 10,170 MB: fits (7%); F64 25,530 MB: fits (3%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    7023f118-b5f8-4a7b-9811-b16c34d32708 TabularSequencePoint        105.2     0.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        103.9    30.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        101.9    30.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        101.0    30.1 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         13.9    14.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         13.7    13.2       0
                                                                    <NA>               Commit          8.2     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.0     2.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          5.6     2.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          5.4     2.7  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.7     1.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.9     0.0       0
```

## Log

```
2026-11-20T09:34:25Z run 20261120T093210Z-v34-f55a: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T09:34:32Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T09:34:36Z PPU: v34-auto-date-time-no-date-table is 7023f118-b5f8-4a7b-9811-b16c34d32708, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:34:58Z PPU: model size in memory before the refresh: 70.3 MB
2026-11-20T09:35:01Z PPU: trace started (full)
2026-11-20T09:35:02Z PPU: refresh started, request 78e57f7f-0ce3-492e-99ba-31e97bd5e3bf
2026-11-20T09:37:12Z PPU: refresh refreshed (Completed) 
2026-11-20T09:37:43Z PPU: trace captured 435 events: ProgressReportEnd 403, ExecutionMetrics 22, CommandEnd 10
2026-11-20T09:37:44Z PPU: model size in memory right after the refresh: 96.9 MB
```
