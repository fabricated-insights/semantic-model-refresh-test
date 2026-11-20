# Harness run 20261120T130425Z-v99o-f55a

- Task: refresh
- Variant: v99o-sorts
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 49d45c67-fd08-4170-8e2e-4949b2007f6a
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 5,329 MB, Power Query 5,039 MB, duration 15 min, CPU 1,445 s, rows 21,583,972, model 100 MB (Backup step in XMLA trace)
- Refresh request ffeeb62c-8f66-4e9b-81e6-1bc4ede32e92, 2026-11-20T13:05:32.123 to 2026-11-20T13:20:37.9, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99o-sorts on PPU data-1m-v1: refreshed, peak 5,288 MB (2026-11-20T06:54:10Z).
  - Peak change: +41 MB (+0.8%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 5,329 MB vs 666 MB (+4,663 MB), Power Query 5,039 MB vs 591 MB, model 100 MB vs 73 MB.
- Model size in memory when the full refresh started: 99 MB. The refresh may use the SKU maximum minus this: 102,301 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,967 MB: OVER (180%); F16 5,021 MB: OVER (106%); F32 10,141 MB: fits (53%); F64 25,501 MB: fits (21%); PPU 102,301 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  c2000c74-e8cf-4893-9b5e-8f96d7ccd23a TabularSequencePoint        895.6     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        882.1    23.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        686.8    23.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        686.5    23.0 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        195.2     0.0       0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          7.5     0.2       0
        Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          7.3     0.0       0
                                                  <NA>               Commit          7.1     0.0    <NA>
                                Sales.Sales Line Label       TabularRefresh          5.3     5.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.3     7.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.0     5.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.2     1.9       0
```

## Log

```
2026-11-20T13:04:59Z run 20261120T130425Z-v99o-f55a: variant=v99o-sorts data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T13:05:07Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:05:11Z PPU: v99o-sorts is c2000c74-e8cf-4893-9b5e-8f96d7ccd23a, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:05:28Z PPU: model size in memory before the refresh: 99.0 MB
2026-11-20T13:05:32Z PPU: trace started (full)
2026-11-20T13:05:32Z PPU: refresh started, request ffeeb62c-8f66-4e9b-81e6-1bc4ede32e92
2026-11-20T13:20:45Z PPU: refresh refreshed (Completed) 
2026-11-20T13:21:16Z PPU: trace captured 407 events: ProgressReportEnd 387, ExecutionMetrics 10, CommandEnd 10
2026-11-20T13:21:17Z PPU: model size in memory right after the refresh: 133.8 MB
```
