# Harness run 20261120T091908Z-v32-f55a

- Task: refresh
- Variant: v32-calc-columns-aggregate
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 5df48d10-8ec8-43d6-9f74-e9c6e32884a0
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 868 MB, Power Query 766 MB, duration 2 min, CPU 188 s, rows 24,570,331, model 221 MB (Backup step in XMLA trace)
- Refresh request 1bb6f6b4-daa2-48d8-a39a-402515e6ce9a, 2026-11-20T09:22:11.083 to 2026-11-20T09:23:59.263, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v32-calc-columns-aggregate on PPU data-1m-v1: refreshed, peak 850 MB (2026-11-19T23:41:15Z).
  - Peak change: +18 MB (+2.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 868 MB vs 666 MB (+202 MB), Power Query 766 MB vs 591 MB, model 221 MB vs 73 MB.
- Model size in memory when the full refresh started: 341 MB. The refresh may use the SKU maximum minus this: 102,059 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,725 MB: fits (32%); F16 4,779 MB: fits (18%); F32 9,899 MB: fits (9%); F64 25,259 MB: fits (3%); PPU 102,059 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    6873b8a8-fea6-4828-b1a1-ee4b78ed0d69 TabularSequencePoint         91.5     0.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         83.1    48.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         81.0    48.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         80.5    47.9 2349091
                                                                    <NA>               Commit         14.1     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          8.7     6.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.1    10.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.8     7.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          7.3     6.1       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          6.8     5.9  104990
                                            Sales.Line Share Of Customer       TabularRefresh          4.2     2.7       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.4     1.8       0
```

## Log

```
2026-11-20T09:21:33Z run 20261120T091908Z-v32-f55a: variant=v32-calc-columns-aggregate data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T09:21:39Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T09:21:46Z PPU: v32-calc-columns-aggregate is 6873b8a8-fea6-4828-b1a1-ee4b78ed0d69, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:22:07Z PPU: model size in memory before the refresh: 341.3 MB
2026-11-20T09:22:10Z PPU: trace started (full)
2026-11-20T09:22:11Z PPU: refresh started, request 1bb6f6b4-daa2-48d8-a39a-402515e6ce9a
2026-11-20T09:24:21Z PPU: refresh refreshed (Completed) 
2026-11-20T09:24:52Z PPU: trace captured 376 events: ProgressReportEnd 344, ExecutionMetrics 22, CommandEnd 10
2026-11-20T09:24:53Z PPU: model size in memory right after the refresh: 367.9 MB
```
