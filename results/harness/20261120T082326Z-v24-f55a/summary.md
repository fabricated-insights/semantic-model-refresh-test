# Harness run 20261120T082326Z-v24-f55a

- Task: refresh
- Variant: v24-bidirectional
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: fef9f31b-83cb-47c9-98f8-62b7ce2d7b67
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 614 MB, Power Query 404 MB, duration 1 min, CPU 107 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 71e4c9b0-9514-496d-8384-eeba41d0ca71, 2026-11-20T08:24:31.12 to 2026-11-20T08:25:47.3, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v24-bidirectional on PPU data-1m-v1: refreshed, peak 677 MB (2026-11-19T22:56:23Z).
  - Peak change: -63 MB (-9.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 614 MB vs 666 MB (-52 MB), Power Query 404 MB vs 591 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (20%); F16 5,054 MB: fits (12%); F32 10,174 MB: fits (6%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  396b5678-cec7-4bcd-98dc-b22a8c270567 TabularSequencePoint         66.2     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         65.3    20.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         62.5    20.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         62.2    20.1 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.8    12.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.6    10.4       0
                                                  <NA>               Commit          5.4     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.7     1.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.7     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.5     1.7       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.4     1.6  104990
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          2.1     0.0       0
```

## Log

```
2026-11-20T08:24:02Z run 20261120T082326Z-v24-f55a: variant=v24-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T08:24:09Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:24:12Z PPU: v24-bidirectional is 396b5678-cec7-4bcd-98dc-b22a8c270567, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:24:27Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-20T08:24:31Z PPU: trace started (full)
2026-11-20T08:24:31Z PPU: refresh started, request 71e4c9b0-9514-496d-8384-eeba41d0ca71
2026-11-20T08:26:11Z PPU: refresh refreshed (Completed) 
2026-11-20T08:26:42Z PPU: trace captured 268 events: ProgressReportEnd 236, ExecutionMetrics 22, CommandEnd 10
2026-11-20T08:26:43Z PPU: model size in memory right after the refresh: 92.7 MB
```
