# Harness run 20261120T144244Z-v27-f55a

- Task: refresh
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 144799db-d8d6-4f2b-8bde-eda2ed15f0f4
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 705 MB, Power Query 463 MB, duration 1 min, CPU 101 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request d2dd77bb-c583-44cd-9497-70b91efb7abf, 2026-11-20T14:45:34.64 to 2026-11-20T14:46:44.05, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v27-high-cardinality-visuals on PPU data-1m-v1: refreshed, peak 607 MB (2026-11-20T08:53:52Z).
  - Peak change: +98 MB (+16.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 705 MB vs 604 MB (+101 MB), Power Query 463 MB vs 529 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (24%); F16 5,054 MB: fits (14%); F32 10,174 MB: fits (7%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    c613573e-80fa-4597-8fae-8cbf73e69fa6 TabularSequencePoint         60.0     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         59.2    18.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         58.0    18.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         56.6    18.6 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.9    12.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.8    11.7       0
                                                                    <NA>               Commit          5.1     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.5     1.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.5     1.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.4     1.6  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.6     0.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.2     0.0       0
```

## Log

```
2026-11-20T14:44:59Z run 20261120T144244Z-v27-f55a: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T14:45:05Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:45:08Z PPU: v27-high-cardinality-visuals is c613573e-80fa-4597-8fae-8cbf73e69fa6, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:45:31Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-20T14:45:34Z PPU: trace started (full)
2026-11-20T14:45:34Z PPU: refresh started, request d2dd77bb-c583-44cd-9497-70b91efb7abf
2026-11-20T14:46:45Z PPU: refresh refreshed (Completed) 
2026-11-20T14:47:16Z PPU: trace captured 256 events: ProgressReportEnd 236, ExecutionMetrics 10, CommandEnd 10
2026-11-20T14:47:16Z PPU: model size in memory right after the refresh: 92.7 MB
```
