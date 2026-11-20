# Harness run 20261119T231651Z-v27-f55a

- Task: refresh
- Variant: v27-high-cardinality-visuals
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 0352fffc-078b-4175-8402-51f6764c019f
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 550 MB, Power Query 270 MB, duration 1 min, CPU 101 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request eb330020-0519-4919-a188-b411a5c9b0bb, 2026-11-19T23:19:38.883 to 2026-11-19T23:20:47.077, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v27-high-cardinality-visuals on PPU data-1m-v1: refreshed, peak 747 MB (2026-11-17T06:32:50Z).
  - Peak change: -197 MB (-26.4%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 550 MB vs 551 MB (-1 MB), Power Query 270 MB vs 298 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (18%); F16 5,054 MB: fits (11%); F32 10,174 MB: fits (5%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  c613573e-80fa-4597-8fae-8cbf73e69fa6 TabularSequencePoint         60.0     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         59.2    17.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         56.7    17.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         55.5    17.5 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.5    12.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.3    11.3       0
                                                  <NA>               Commit          5.0     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.6     1.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.4     1.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.4     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.3     1.6  104990
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.2     0.1       0
```

## Log

```
2026-11-19T23:19:04Z run 20261119T231651Z-v27-f55a: variant=v27-high-cardinality-visuals data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T23:19:11Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:19:15Z PPU: v27-high-cardinality-visuals is c613573e-80fa-4597-8fae-8cbf73e69fa6, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:19:35Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-19T23:19:38Z PPU: trace started (full)
2026-11-19T23:19:39Z PPU: refresh started, request eb330020-0519-4919-a188-b411a5c9b0bb
2026-11-19T23:20:49Z PPU: refresh refreshed (Completed) 
2026-11-19T23:21:19Z PPU: trace captured 282 events: ProgressReportEnd 237, ExecutionMetrics 34, CommandEnd 11
2026-11-19T23:21:20Z PPU: model size in memory right after the refresh: 92.7 MB
```
