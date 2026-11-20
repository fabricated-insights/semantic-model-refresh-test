# Harness run 20261120T140122Z-v22-f55a

- Task: refresh
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 031b31a1-42cc-4b6d-a551-60f4f3269dea
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 978 MB, Power Query 939 MB, duration 2 min, CPU 150 s, rows 21,353,868, model 101 MB (Backup step in XMLA trace)
- Refresh request 425ce927-9411-4d6e-a1ec-533b9039f024, 2026-11-20T14:04:41.077 to 2026-11-20T14:06:27.137, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v22-dax-calc-columns on PPU data-1m-v1: refreshed, peak 815 MB (2026-11-20T08:15:37Z).
  - Peak change: +163 MB (+20.0%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 978 MB vs 604 MB (+374 MB), Power Query 939 MB vs 529 MB, model 101 MB vs 73 MB.
- Model size in memory when the full refresh started: 98 MB. The refresh may use the SKU maximum minus this: 102,302 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,968 MB: fits (33%); F16 5,022 MB: fits (19%); F32 10,142 MB: fits (10%); F64 25,502 MB: fits (4%); PPU 102,302 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    f04681eb-fd6e-44c2-902a-dad6c2273007 TabularSequencePoint         94.6     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         85.4    27.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         83.9    27.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         83.5    27.3 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.0     9.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.7     6.7       0
                                                                    <NA>               Commit          6.7     0.0    <NA>
                                                  Sales.Sales Line Label       TabularRefresh          6.2     6.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.4     2.5       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.1     2.4       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          3.9     2.3  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.6     0.9       0
```

## Log

```
2026-11-20T14:04:00Z run 20261120T140122Z-v22-f55a: variant=v22-dax-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T14:04:09Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:04:12Z PPU: v22-dax-calc-columns is f04681eb-fd6e-44c2-902a-dad6c2273007, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:04:37Z PPU: model size in memory before the refresh: 97.8 MB
2026-11-20T14:04:40Z PPU: trace started (full)
2026-11-20T14:04:41Z PPU: refresh started, request 425ce927-9411-4d6e-a1ec-533b9039f024
2026-11-20T14:06:51Z PPU: refresh refreshed (Completed) 
2026-11-20T14:07:22Z PPU: trace captured 296 events: ProgressReportEnd 276, ExecutionMetrics 10, CommandEnd 10
2026-11-20T14:07:23Z PPU: model size in memory right after the refresh: 132.6 MB
```
