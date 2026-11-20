# Harness run 20261120T091255Z-v31-f55a

- Task: refresh
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 004ce5db-e656-41e1-9a12-6a64518f3107
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,001 MB, Power Query 857 MB, duration 1 min, CPU 170 s, rows 77,732,052, model 223 MB (Backup step in XMLA trace)
- Refresh request 2b2a5dbc-641d-46bb-b2d4-05f5a05eca4e, 2026-11-20T09:15:56.767 to 2026-11-20T09:17:40.953, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v31-calc-columns-row on PPU data-1m-v1: refreshed, peak 938 MB (2026-11-19T23:37:34Z).
  - Peak change: +63 MB (+6.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 1,001 MB vs 666 MB (+335 MB), Power Query 857 MB vs 591 MB, model 223 MB vs 73 MB.
- Model size in memory when the full refresh started: 234 MB. The refresh may use the SKU maximum minus this: 102,166 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,832 MB: fits (35%); F16 4,886 MB: fits (20%); F32 10,006 MB: fits (10%); F64 25,366 MB: fits (4%); PPU 102,166 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  ac3ebe29-9abb-4067-9007-e7d601187a3c TabularSequencePoint         87.6     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         67.4    27.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         64.5    26.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         63.5    26.8 2349091
                                                  <NA>               Commit         14.4     0.0    <NA>
                                  Sales.Order Line Key       TabularRefresh         13.7     4.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.3    15.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.9    10.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.2     1.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      CompressSegment          3.0     4.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.7     1.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.7     0.0       0
```

## Log

```
2026-11-20T09:15:20Z run 20261120T091255Z-v31-f55a: variant=v31-calc-columns-row data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T09:15:25Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T09:15:30Z PPU: v31-calc-columns-row is ac3ebe29-9abb-4067-9007-e7d601187a3c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:15:53Z PPU: model size in memory before the refresh: 233.5 MB
2026-11-20T09:15:56Z PPU: trace started (full)
2026-11-20T09:15:57Z PPU: refresh started, request 2b2a5dbc-641d-46bb-b2d4-05f5a05eca4e
2026-11-20T09:18:07Z PPU: refresh refreshed (Completed) 
2026-11-20T09:18:38Z PPU: trace captured 428 events: ProgressReportEnd 396, ExecutionMetrics 22, CommandEnd 10
2026-11-20T09:18:39Z PPU: model size in memory right after the refresh: 316.8 MB
```
