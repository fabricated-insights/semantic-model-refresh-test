# Harness run 20261120T062339Z-v99m-f55a

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 4c1e6d4c-e47a-43ff-932f-834cde36d520
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 829 MB, Power Query 665 MB, duration 1 min, CPU 110 s, rows 21,583,972, model 102 MB (Backup step in XMLA trace)
- Refresh request b85b5745-474e-4707-a1f1-627a040109e3, 2026-11-20T06:27:09.14 to 2026-11-20T06:28:24.247, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99m-baseline-pq on PPU data-1m-v1: refreshed, peak 770 MB (2026-11-17T12:43:34Z).
  - Peak change: +59 MB (+7.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 829 MB vs 551 MB (+278 MB), Power Query 665 MB vs 298 MB, model 102 MB vs 73 MB.
- Model size in memory when the full refresh started: 101 MB. The refresh may use the SKU maximum minus this: 102,299 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,965 MB: fits (28%); F16 5,019 MB: fits (17%); F32 10,139 MB: fits (8%); F64 25,499 MB: fits (3%); PPU 102,299 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  3394eba6-7666-49c7-99a1-cd99723178be TabularSequencePoint         64.8     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         57.2    19.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         54.4    19.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         53.9    19.2 2349091
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          9.8     1.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.0    10.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.7     7.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          7.3     0.0       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          7.3     0.0       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          7.2     0.0       0
                                                  <NA>               Commit          6.6     0.0    <NA>
                                Sales.Sales Line Label       TabularRefresh          5.4     5.2       0
```

## Log

```
2026-11-20T06:26:26Z run 20261120T062339Z-v99m-f55a: variant=v99m-baseline-pq data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T06:26:36Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T06:26:40Z PPU: v99m-baseline-pq is 3394eba6-7666-49c7-99a1-cd99723178be, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T06:27:05Z PPU: model size in memory before the refresh: 101.3 MB
2026-11-20T06:27:09Z PPU: trace started (full)
2026-11-20T06:27:09Z PPU: refresh started, request b85b5745-474e-4707-a1f1-627a040109e3
2026-11-20T06:28:49Z PPU: refresh refreshed (Completed) 
2026-11-20T06:29:20Z PPU: trace captured 433 events: ProgressReportEnd 388, ExecutionMetrics 34, CommandEnd 11
2026-11-20T06:29:21Z PPU: model size in memory right after the refresh: 136.1 MB
```
