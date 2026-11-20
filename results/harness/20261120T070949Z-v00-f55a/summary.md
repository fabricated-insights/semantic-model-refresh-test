# Harness run 20261120T070949Z-v00-f55a

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 468048c8-fb8d-4790-836e-9f513f644647
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 666 MB, Power Query 591 MB, duration 1 min, CPU 123 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 7ffc0f2a-14a4-4e51-bc31-df58b24c8399, 2026-11-20T07:12:53.523 to 2026-11-20T07:14:18.197, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v00-baseline on PPU data-1m-v1: refreshed, peak 551 MB (2026-11-19T21:55:23Z).
  - Peak change: +115 MB (+20.9%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (22%); F16 5,054 MB: fits (13%); F32 10,174 MB: fits (7%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    0eee6936-1906-41cc-ae01-289b0589e4e1 TabularSequencePoint         76.3     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         75.4    22.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         72.1    22.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         71.7    22.3 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.5    11.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.3    10.2       0
                                                                    <NA>               Commit          6.4     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.2     2.1       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.6     0.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.5     2.1       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.4     2.0  104990
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          3.2     0.0       0
```

## Log

```
2026-11-20T07:12:17Z run 20261120T070949Z-v00-f55a: variant=v00-baseline data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T07:12:25Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:12:28Z PPU: v00-baseline is 0eee6936-1906-41cc-ae01-289b0589e4e1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:12:49Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-20T07:12:53Z PPU: trace started (full)
2026-11-20T07:12:53Z PPU: refresh started, request 7ffc0f2a-14a4-4e51-bc31-df58b24c8399
2026-11-20T07:14:34Z PPU: refresh refreshed (Completed) 
2026-11-20T07:15:05Z PPU: trace captured 282 events: ProgressReportEnd 237, ExecutionMetrics 34, CommandEnd 11
2026-11-20T07:15:05Z PPU: model size in memory right after the refresh: 92.7 MB
```
