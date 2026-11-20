# Harness run 20261120T133509Z-v00-f55a

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f521fdec-b9c3-4165-9a9a-2e1f386a4036
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 604 MB, Power Query 529 MB, duration 1 min, CPU 120 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request bb96a4d0-59c8-4522-acc3-5e09cad48175, 2026-11-20T13:37:59.843 to 2026-11-20T13:39:24.403, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v00-baseline on PPU data-1m-v1: refreshed, peak 666 MB (2026-11-20T07:15:05Z).
  - Peak change: -62 MB (-9.3%). **FLAG: peak changed by more than 1%**
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (20%); F16 5,054 MB: fits (12%); F32 10,174 MB: fits (6%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    0eee6936-1906-41cc-ae01-289b0589e4e1 TabularSequencePoint         75.0     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         74.3    23.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         71.4    23.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         71.0    23.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.4    11.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.2    10.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.8     2.2       0
                                                                    <NA>               Commit          4.7     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.3     2.1       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.3     0.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.1     2.1  104990
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.9     0.0       0
```

## Log

```
2026-11-20T13:37:23Z run 20261120T133509Z-v00-f55a: variant=v00-baseline data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T13:37:29Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:37:33Z PPU: v00-baseline is 0eee6936-1906-41cc-ae01-289b0589e4e1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:37:56Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-20T13:37:59Z PPU: trace started (full)
2026-11-20T13:38:00Z PPU: refresh started, request bb96a4d0-59c8-4522-acc3-5e09cad48175
2026-11-20T13:39:40Z PPU: refresh refreshed (Completed) 
2026-11-20T13:40:11Z PPU: trace captured 256 events: ProgressReportEnd 236, ExecutionMetrics 10, CommandEnd 10
2026-11-20T13:40:12Z PPU: model size in memory right after the refresh: 92.7 MB
```
