# Harness run 20261120T064407Z-v99o-f55a

- Task: refresh
- Variant: v99o-sorts
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: dbca92bc-4c5b-4420-8568-422cf119a95c
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 5,288 MB, Power Query 4,986 MB, duration 6 min, CPU 514 s, rows 21,583,972, model 100 MB (Backup step in XMLA trace)
- Refresh request 11595ad5-ca11-47d8-a864-d8936992bc22, 2026-11-20T06:46:58.033 to 2026-11-20T06:53:33.597, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99o-sorts on PPU data-1m-v1: refreshed, peak 5,182 MB (2026-11-17T15:19:54Z).
  - Peak change: +106 MB (+2.0%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 5,288 MB vs 551 MB (+4,737 MB), Power Query 4,986 MB vs 298 MB, model 100 MB vs 73 MB.
- Model size in memory when the full refresh started: 99 MB. The refresh may use the SKU maximum minus this: 102,301 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,967 MB: OVER (178%); F16 5,021 MB: OVER (105%); F32 10,141 MB: fits (52%); F64 25,501 MB: fits (21%); PPU 102,301 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  c2000c74-e8cf-4893-9b5e-8f96d7ccd23a TabularSequencePoint        385.7     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        375.4    20.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        245.2    20.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        244.9    20.7 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        130.1     0.0       0
                                                  <NA>               Commit          6.3     0.0    <NA>
                                Sales.Sales Line Label       TabularRefresh          5.9     5.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.9     6.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.6     4.6       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.0     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.1     1.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.0     1.8  104990
```

## Log

```
2026-11-20T06:46:22Z run 20261120T064407Z-v99o-f55a: variant=v99o-sorts data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T06:46:33Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T06:46:36Z PPU: v99o-sorts is c2000c74-e8cf-4893-9b5e-8f96d7ccd23a, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T06:46:54Z PPU: model size in memory before the refresh: 99.0 MB
2026-11-20T06:46:57Z PPU: trace started (full)
2026-11-20T06:46:58Z PPU: refresh started, request 11595ad5-ca11-47d8-a864-d8936992bc22
2026-11-20T06:53:39Z PPU: refresh refreshed (Completed) 
2026-11-20T06:54:10Z PPU: trace captured 433 events: ProgressReportEnd 388, ExecutionMetrics 34, CommandEnd 11
2026-11-20T06:54:11Z PPU: model size in memory right after the refresh: 133.8 MB
```
