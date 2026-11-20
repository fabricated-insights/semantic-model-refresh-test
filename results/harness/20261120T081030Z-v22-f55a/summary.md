# Harness run 20261120T081030Z-v22-f55a

- Task: refresh
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 7185016b-3ed4-4486-ba70-cef17e4f1ff6
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 815 MB, Power Query 773 MB, duration 1 min, CPU 148 s, rows 21,353,868, model 101 MB (Backup step in XMLA trace)
- Refresh request f5a40d55-caa1-4c71-9639-d8bbf16b6db8, 2026-11-20T08:13:25.82 to 2026-11-20T08:15:04.58, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v22-dax-calc-columns on PPU data-1m-v1: refreshed, peak 620 MB (2026-11-19T22:47:13Z).
  - Peak change: +195 MB (+31.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 815 MB vs 666 MB (+149 MB), Power Query 773 MB vs 591 MB, model 101 MB vs 73 MB.
- Model size in memory when the full refresh started: 98 MB. The refresh may use the SKU maximum minus this: 102,302 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,968 MB: fits (27%); F16 5,022 MB: fits (16%); F32 10,142 MB: fits (8%); F64 25,502 MB: fits (3%); PPU 102,302 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  f04681eb-fd6e-44c2-902a-dad6c2273007 TabularSequencePoint         87.9     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         78.6    27.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         76.6    27.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         76.1    27.5 2349091
                                                  <NA>               Commit          8.2     0.0    <NA>
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.9    10.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.6     7.6       0
                                Sales.Sales Line Label       TabularRefresh          6.8     6.5       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.7     2.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.9     2.7       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.8     2.6  104990
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.9     0.2       0
```

## Log

```
2026-11-20T08:12:47Z run 20261120T081030Z-v22-f55a: variant=v22-dax-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T08:12:54Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:12:58Z PPU: v22-dax-calc-columns is f04681eb-fd6e-44c2-902a-dad6c2273007, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:13:22Z PPU: model size in memory before the refresh: 97.8 MB
2026-11-20T08:13:25Z PPU: trace started (full)
2026-11-20T08:13:25Z PPU: refresh started, request f5a40d55-caa1-4c71-9639-d8bbf16b6db8
2026-11-20T08:15:06Z PPU: refresh refreshed (Completed) 
2026-11-20T08:15:36Z PPU: trace captured 308 events: ProgressReportEnd 276, ExecutionMetrics 22, CommandEnd 10
2026-11-20T08:15:37Z PPU: model size in memory right after the refresh: 132.6 MB
```
