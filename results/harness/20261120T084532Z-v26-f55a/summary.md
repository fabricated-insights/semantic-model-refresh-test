# Harness run 20261120T084532Z-v26-f55a

- Task: refresh
- Variant: v26-bad-dax
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 46302613-2221-431a-b13f-ffdfc141c5fa
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 593 MB, Power Query 392 MB, duration 1 min, CPU 103 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request de17440e-edb1-4c6c-8c3f-c8a75f432c95, 2026-11-20T08:46:55.073 to 2026-11-20T08:48:04.01, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v26-bad-dax on PPU data-1m-v1: refreshed, peak 614 MB (2026-11-19T23:16:09Z).
  - Peak change: -21 MB (-3.4%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 593 MB vs 666 MB (-73 MB), Power Query 392 MB vs 591 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (20%); F16 5,054 MB: fits (12%); F32 10,174 MB: fits (6%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    2ee61d67-d165-40e2-b3c1-d06e2a600c8e TabularSequencePoint         61.6     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         60.9    19.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         58.9    19.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         58.5    19.7 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.1    11.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.9     9.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.7     1.8       0
                                                                    <NA>               Commit          4.6     0.0    <NA>
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.9     0.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.6     1.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.5     1.7  104990
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.1     0.1       0
```

## Log

```
2026-11-20T08:46:25Z run 20261120T084532Z-v26-f55a: variant=v26-bad-dax data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T08:46:32Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:46:35Z PPU: v26-bad-dax is 2ee61d67-d165-40e2-b3c1-d06e2a600c8e, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:46:51Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-20T08:46:54Z PPU: trace started (full)
2026-11-20T08:46:55Z PPU: refresh started, request de17440e-edb1-4c6c-8c3f-c8a75f432c95
2026-11-20T08:48:05Z PPU: refresh refreshed (Completed) 
2026-11-20T08:48:36Z PPU: trace captured 268 events: ProgressReportEnd 236, ExecutionMetrics 22, CommandEnd 10
2026-11-20T08:48:36Z PPU: model size in memory right after the refresh: 92.7 MB
```
