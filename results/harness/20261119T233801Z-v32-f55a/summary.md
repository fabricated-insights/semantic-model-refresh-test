# Harness run 20261119T233801Z-v32-f55a

- Task: refresh
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 499057cc-c0c0-4f03-ad60-a71094d358c4
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 850 MB, Power Query 747 MB, duration 1 min, CPU 132 s, rows 24,570,331, model 221 MB (Backup step in XMLA trace)
- Refresh request 909dce2d-928a-43f6-a17e-61f57fcf7520, 2026-11-19T23:39:04.357 to 2026-11-19T23:40:30.827, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v32-calc-columns-aggregate on PPU data-1m-v1: refreshed, peak 928 MB (2026-11-17T08:00:46Z).
  - Peak change: -78 MB (-8.4%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 850 MB vs 551 MB (+299 MB), Power Query 747 MB vs 298 MB, model 221 MB vs 73 MB.
- Model size in memory when the full refresh started: 341 MB. The refresh may use the SKU maximum minus this: 102,059 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,725 MB: fits (31%); F16 4,779 MB: fits (18%); F32 9,899 MB: fits (9%); F64 25,259 MB: fits (3%); PPU 102,059 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    6873b8a8-fea6-4828-b1a1-ee4b78ed0d69 TabularSequencePoint         72.7     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         65.7    21.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         63.9    21.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         63.5    20.9 2349091
                                                                    <NA>               Commit         12.3     0.0    <NA>
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.5    10.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.3     8.3       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          8.2     0.5       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          7.3     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.4     1.8       0
                                            Sales.Line Share Of Customer       TabularRefresh          3.6     2.3       0
                                                       Sales.Order Total       TabularRefresh          2.9     2.0       0
```

## Log

```
2026-11-19T23:38:34Z run 20261119T233801Z-v32-f55a: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T23:38:43Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:38:49Z PPU: v32-calc-columns-aggregate is 6873b8a8-fea6-4828-b1a1-ee4b78ed0d69, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:39:00Z PPU: model size in memory before the refresh: 341.3 MB
2026-11-19T23:39:04Z PPU: trace started (full)
2026-11-19T23:39:04Z PPU: refresh started, request 909dce2d-928a-43f6-a17e-61f57fcf7520
2026-11-19T23:40:44Z PPU: refresh refreshed (Completed) 
2026-11-19T23:41:15Z PPU: trace captured 390 events: ProgressReportEnd 345, ExecutionMetrics 34, CommandEnd 11
2026-11-19T23:41:16Z PPU: model size in memory right after the refresh: 367.9 MB
```
