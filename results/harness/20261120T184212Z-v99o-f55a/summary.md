# Harness run 20261120T184212Z-v99o-f55a

- Task: refresh
- Variant: v99o-sorts
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1b565e6a-8f3b-49f2-83da-5daf8859b6d8
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 5,290 MB, Power Query 4,945 MB, duration 7 min, CPU 595 s, rows 21,583,972, model 100 MB (Backup step in XMLA trace)
- Refresh request dcc18c9c-a53a-44bb-bb69-ca1ec717f63f, 2026-11-20T18:43:12.247 to 2026-11-20T18:50:21.347, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99o-sorts on PPU data-1m-v1: refreshed, peak 5,329 MB (2026-11-20T13:21:16Z).
  - Peak change: -39 MB (-0.7%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 5,290 MB vs 604 MB (+4,686 MB), Power Query 4,945 MB vs 529 MB, model 100 MB vs 73 MB.
- Model size in memory when the full refresh started: 99 MB. The refresh may use the SKU maximum minus this: 102,301 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,967 MB: OVER (178%); F16 5,021 MB: OVER (105%); F32 10,141 MB: fits (52%); F64 25,501 MB: fits (21%); PPU 102,301 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  c2000c74-e8cf-4893-9b5e-8f96d7ccd23a TabularSequencePoint        418.5     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        408.1    21.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        297.5    21.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        297.1    21.1 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        110.5     0.0       0
                                                  <NA>               Commit          6.4     0.0    <NA>
                                Sales.Sales Line Label       TabularRefresh          5.7     5.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.6     7.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.3     5.3       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.4     1.5       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.7     1.5       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.6     1.5  104990
```

## Log

```
2026-11-20T18:42:39Z run 20261120T184212Z-v99o-f55a: variant=v99o-sorts data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T18:42:47Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T18:42:50Z PPU: v99o-sorts is c2000c74-e8cf-4893-9b5e-8f96d7ccd23a, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T18:43:08Z PPU: model size in memory before the refresh: 99.0 MB
2026-11-20T18:43:12Z PPU: trace started (full)
2026-11-20T18:43:12Z PPU: refresh started, request dcc18c9c-a53a-44bb-bb69-ca1ec717f63f
2026-11-20T18:50:23Z PPU: refresh refreshed (Completed) 
2026-11-20T18:50:54Z PPU: trace captured 407 events: ProgressReportEnd 387, ExecutionMetrics 10, CommandEnd 10
2026-11-20T18:50:55Z PPU: model size in memory right after the refresh: 133.8 MB
```
