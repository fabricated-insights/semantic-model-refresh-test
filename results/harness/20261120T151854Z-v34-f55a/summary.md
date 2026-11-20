# Harness run 20261120T151854Z-v34-f55a

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 93fbbb1d-d695-477f-9700-9520d289ce9f
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 921 MB, Power Query 904 MB, duration 1 min, CPU 106 s, rows 2,847,496, model 74 MB (Backup step in XMLA trace)
- Refresh request 74cd41ed-52b5-4c8a-8501-2cc345251092, 2026-11-20T15:19:55.753 to 2026-11-20T15:21:08.53, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v34-auto-date-time-no-date-table on PPU data-1m-v1: refreshed, peak 668 MB (2026-11-20T09:37:43Z).
  - Peak change: +253 MB (+37.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 921 MB vs 604 MB (+317 MB), Power Query 904 MB vs 529 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 102,330 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (31%); F16 5,050 MB: fits (18%); F32 10,170 MB: fits (9%); F64 25,530 MB: fits (4%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    7023f118-b5f8-4a7b-9811-b16c34d32708 TabularSequencePoint         62.6     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         61.6    20.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         59.7    20.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         59.2    20.7 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.9    12.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.7    10.7       0
                                                                    <NA>               Commit          5.5     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.4     1.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.8     1.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.6     1.8  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.9     0.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.8     0.0       0
```

## Log

```
2026-11-20T15:19:27Z run 20261120T151854Z-v34-f55a: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T15:19:32Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T15:19:36Z PPU: v34-auto-date-time-no-date-table is 7023f118-b5f8-4a7b-9811-b16c34d32708, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T15:19:52Z PPU: model size in memory before the refresh: 70.3 MB
2026-11-20T15:19:55Z PPU: trace started (full)
2026-11-20T15:19:55Z PPU: refresh started, request 74cd41ed-52b5-4c8a-8501-2cc345251092
2026-11-20T15:21:36Z PPU: refresh refreshed (Completed) 
2026-11-20T15:22:06Z PPU: trace captured 423 events: ProgressReportEnd 403, ExecutionMetrics 10, CommandEnd 10
2026-11-20T15:22:07Z PPU: model size in memory right after the refresh: 96.9 MB
```
