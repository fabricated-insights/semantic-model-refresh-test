# Harness run 20261120T124700Z-v99m-f55a

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6cb86786-1140-4905-86a5-dfa9f56fa065
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 766 MB, Power Query 411 MB, duration 1 min, CPU 125 s, rows 21,583,972, model 102 MB (Backup step in XMLA trace)
- Refresh request 55d47426-2c6f-4248-bae3-a8eafb439405, 2026-11-20T12:49:55.71 to 2026-11-20T12:51:16.93, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99m-baseline-pq on PPU data-1m-v1: refreshed, peak 829 MB (2026-11-20T06:29:20Z).
  - Peak change: -63 MB (-7.6%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 766 MB vs 666 MB (+100 MB), Power Query 411 MB vs 591 MB, model 102 MB vs 73 MB.
- Model size in memory when the full refresh started: 101 MB. The refresh may use the SKU maximum minus this: 102,299 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,965 MB: fits (26%); F16 5,019 MB: fits (15%); F32 10,139 MB: fits (8%); F64 25,499 MB: fits (3%); PPU 102,299 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  3394eba6-7666-49c7-99a1-cd99723178be TabularSequencePoint         70.7     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         62.0    22.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         60.3    22.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         59.8    22.5 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.1    10.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.9     7.9       0
                                                  <NA>               Commit          7.0     0.0    <NA>
                                Sales.Sales Line Label       TabularRefresh          6.5     6.2       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.9     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.8     1.8  104990
                                   Sales.Customer Name       TabularRefresh          2.5     2.0       0
```

## Log

```
2026-11-20T12:49:15Z run 20261120T124700Z-v99m-f55a: variant=v99m-baseline-pq data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T12:49:24Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:49:28Z PPU: v99m-baseline-pq is 3394eba6-7666-49c7-99a1-cd99723178be, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:49:52Z PPU: model size in memory before the refresh: 101.3 MB
2026-11-20T12:49:55Z PPU: trace started (full)
2026-11-20T12:49:55Z PPU: refresh started, request 55d47426-2c6f-4248-bae3-a8eafb439405
2026-11-20T12:51:36Z PPU: refresh refreshed (Completed) 
2026-11-20T12:52:07Z PPU: trace captured 407 events: ProgressReportEnd 387, ExecutionMetrics 10, CommandEnd 10
2026-11-20T12:52:07Z PPU: model size in memory right after the refresh: 136.1 MB
```
