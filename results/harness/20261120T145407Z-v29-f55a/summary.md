# Harness run 20261120T145407Z-v29-f55a

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e577675b-8881-4a51-b051-70e8b927c75c
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 607 MB, Power Query 336 MB, duration 1 min, CPU 109 s, rows 2,561,140, model 69 MB (Backup step in XMLA trace)
- Refresh request c035cbd0-8ad7-4748-a5c7-9b50ec5d3148, 2026-11-20T14:55:12.2 to 2026-11-20T14:56:16.93, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v29-keys-as-text on PPU data-1m-v1: refreshed, peak 729 MB (2026-11-20T09:05:56Z).
  - Peak change: -122 MB (-16.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 607 MB vs 604 MB (+3 MB), Power Query 336 MB vs 529 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 94 MB. The refresh may use the SKU maximum minus this: 102,306 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,972 MB: fits (20%); F16 5,026 MB: fits (12%); F32 10,146 MB: fits (6%); F64 25,506 MB: fits (2%); PPU 102,306 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    b73c5270-73fd-4a15-abcd-c363c7d08602 TabularSequencePoint         56.5     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         53.1    25.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         50.5    25.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         47.0    25.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         14.8    14.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.0     1.8       0
                                                                    <NA>               Commit          4.4     0.0    <NA>
                                                      Sales.Order Number       TabularRefresh          3.1     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.1     0.6       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.7     0.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.6     1.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.5     1.7  104990
```

## Log

```
2026-11-20T14:54:43Z run 20261120T145407Z-v29-f55a: variant=v29-keys-as-text data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T14:54:49Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:54:52Z PPU: v29-keys-as-text is b73c5270-73fd-4a15-abcd-c363c7d08602, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:55:08Z PPU: model size in memory before the refresh: 93.8 MB
2026-11-20T14:55:12Z PPU: trace started (full)
2026-11-20T14:55:12Z PPU: refresh started, request c035cbd0-8ad7-4748-a5c7-9b50ec5d3148
2026-11-20T14:56:22Z PPU: refresh refreshed (Completed) 
2026-11-20T14:56:53Z PPU: trace captured 253 events: ProgressReportEnd 233, ExecutionMetrics 10, CommandEnd 10
2026-11-20T14:56:54Z PPU: model size in memory right after the refresh: 141.9 MB
```
