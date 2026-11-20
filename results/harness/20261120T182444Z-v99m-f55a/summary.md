# Harness run 20261120T182444Z-v99m-f55a

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f73e20c3-275c-453f-a4a1-a37422c0cbde
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 625 MB, Power Query 457 MB, duration 1 min, CPU 130 s, rows 21,583,972, model 102 MB (Backup step in XMLA trace)
- Refresh request 30182926-a36e-4e14-be71-df7cad94b79a, 2026-11-20T18:27:37.813 to 2026-11-20T18:28:59.007, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99m-baseline-pq on PPU data-1m-v1: refreshed, peak 766 MB (2026-11-20T12:52:07Z).
  - Peak change: -141 MB (-18.4%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 625 MB vs 604 MB (+21 MB), Power Query 457 MB vs 529 MB, model 102 MB vs 73 MB.
- Model size in memory when the full refresh started: 101 MB. The refresh may use the SKU maximum minus this: 102,299 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,965 MB: fits (21%); F16 5,019 MB: fits (12%); F32 10,139 MB: fits (6%); F64 25,499 MB: fits (2%); PPU 102,299 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    3394eba6-7666-49c7-99a1-cd99723178be TabularSequencePoint         72.4     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         64.1    24.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         61.2    24.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         60.8    23.9 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.5    10.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.2     8.2       0
                                                                    <NA>               Commit          7.4     0.0    <NA>
                                                  Sales.Sales Line Label       TabularRefresh          6.0     5.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.2     2.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.2     0.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.9     1.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.8     0.0       0
```

## Log

```
2026-11-20T18:27:00Z run 20261120T182444Z-v99m-f55a: variant=v99m-baseline-pq data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T18:27:07Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T18:27:11Z PPU: v99m-baseline-pq is 3394eba6-7666-49c7-99a1-cd99723178be, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T18:27:34Z PPU: model size in memory before the refresh: 101.3 MB
2026-11-20T18:27:37Z PPU: trace started (full)
2026-11-20T18:27:38Z PPU: refresh started, request 30182926-a36e-4e14-be71-df7cad94b79a
2026-11-20T18:29:18Z PPU: refresh refreshed (Completed) 
2026-11-20T18:29:49Z PPU: trace captured 407 events: ProgressReportEnd 387, ExecutionMetrics 10, CommandEnd 10
2026-11-20T18:29:49Z PPU: model size in memory right after the refresh: 136.1 MB
```
