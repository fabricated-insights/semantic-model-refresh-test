# Harness run 20261120T140807Z-v23-f55a

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: bea73ea0-c4b8-4c26-8e33-c68ffea0de6f
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 1,485 MB, Power Query 1,243 MB, duration 1 min, CPU 177 s, rows 16,549,502, model 182 MB (Backup step in XMLA trace)
- Refresh request 12f7f18c-e276-433e-8c87-e85bdcf7f449, 2026-11-20T14:10:54.073 to 2026-11-20T14:12:39.087, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v23-dax-calc-tables on PPU data-1m-v1: refreshed, peak 1,405 MB (2026-11-20T08:22:46Z).
  - Peak change: +80 MB (+5.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 1,485 MB vs 604 MB (+881 MB), Power Query 1,243 MB vs 529 MB, model 182 MB vs 73 MB.
- Model size in memory when the full refresh started: 149 MB. The refresh may use the SKU maximum minus this: 102,251 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,917 MB: fits (51%); F16 4,971 MB: fits (30%); F32 10,091 MB: fits (15%); F64 25,451 MB: fits (6%); PPU 102,251 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  316478cf-dbf2-484e-9234-3f1cb86faffd TabularSequencePoint         87.7     0.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         69.9    21.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         68.4    21.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         65.9    21.2 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         16.8    17.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         16.5    16.2       0
                                 Sales Copy.Sales Copy       TabularRefresh         16.1    12.9       0
                   Product Date Grid.Product Date Grid             VertiPaq         14.6    13.8       0
                                                  <NA>               Commit         13.4     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         11.9     2.7       0
                   Product Date Grid.Product Date Grid       TabularRefresh         11.7    10.1       0
                   Product Date Grid.Product Date Grid              Process         11.6    10.1       0
```

## Log

```
2026-11-20T14:10:15Z run 20261120T140807Z-v23-f55a: variant=v23-dax-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T14:10:22Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:10:28Z PPU: v23-dax-calc-tables is 316478cf-dbf2-484e-9234-3f1cb86faffd, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:10:50Z PPU: model size in memory before the refresh: 148.6 MB
2026-11-20T14:10:53Z PPU: trace started (full)
2026-11-20T14:10:54Z PPU: refresh started, request 12f7f18c-e276-433e-8c87-e85bdcf7f449
2026-11-20T14:13:04Z PPU: refresh refreshed (Completed) 
2026-11-20T14:13:36Z PPU: trace captured 438 events: ProgressReportEnd 418, ExecutionMetrics 10, CommandEnd 10
2026-11-20T14:13:37Z PPU: model size in memory right after the refresh: 184.0 MB
```
