# Harness run 20261120T141420Z-v24-f55a

- Task: refresh
- Variant: v24-bidirectional
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: af88a980-5783-4d7b-8a4a-855077a202a4
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 760 MB, Power Query 732 MB, duration 1 min, CPU 98 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 73b07401-e6e9-457d-b3ad-8059730ee671, 2026-11-20T14:17:25.4 to 2026-11-20T14:18:32.083, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v24-bidirectional on PPU data-1m-v1: refreshed, peak 614 MB (2026-11-20T08:26:42Z).
  - Peak change: +146 MB (+23.8%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 760 MB vs 604 MB (+156 MB), Power Query 732 MB vs 529 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (25%); F16 5,054 MB: fits (15%); F32 10,174 MB: fits (7%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    396b5678-cec7-4bcd-98dc-b22a8c270567 TabularSequencePoint         57.2     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         56.4    18.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         55.1    18.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         53.3    18.4 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         12.0    13.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.9    11.9       0
                                                                    <NA>               Commit          4.6     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.3     1.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.4     1.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.3     1.7  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.6     0.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.1     0.0       0
```

## Log

```
2026-11-20T14:16:48Z run 20261120T141420Z-v24-f55a: variant=v24-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T14:16:54Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:16:57Z PPU: v24-bidirectional is 396b5678-cec7-4bcd-98dc-b22a8c270567, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:17:21Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-20T14:17:25Z PPU: trace started (full)
2026-11-20T14:17:25Z PPU: refresh started, request 73b07401-e6e9-457d-b3ad-8059730ee671
2026-11-20T14:18:36Z PPU: refresh refreshed (Completed) 
2026-11-20T14:19:06Z PPU: trace captured 256 events: ProgressReportEnd 236, ExecutionMetrics 10, CommandEnd 10
2026-11-20T14:19:07Z PPU: model size in memory right after the refresh: 92.7 MB
```
