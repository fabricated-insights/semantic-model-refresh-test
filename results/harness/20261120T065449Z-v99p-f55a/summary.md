# Harness run 20261120T065449Z-v99p-f55a

- Task: refresh
- Variant: v99p-high-cardinality
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3576455a-1387-4534-a8ec-8f7771660fbf
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 686 MB, Power Query 273 MB, duration 1 min, CPU 138 s, rows 21,609,543, model 175 MB (Backup step in XMLA trace)
- Refresh request ff599148-9c5c-4213-9c48-c9308bc568a8, 2026-11-20T06:58:07.22 to 2026-11-20T06:59:43.117, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99p-high-cardinality on PPU data-1m-v1: refreshed, peak 1,284 MB (2026-11-17T15:31:48Z).
  - Peak change: -598 MB (-46.6%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 686 MB vs 551 MB (+135 MB), Power Query 273 MB vs 298 MB, model 175 MB vs 73 MB.
- Model size in memory when the full refresh started: 174 MB. The refresh may use the SKU maximum minus this: 102,226 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,892 MB: fits (24%); F16 4,946 MB: fits (14%); F32 10,066 MB: fits (7%); F64 25,426 MB: fits (3%); PPU 102,226 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  7bc682e3-1008-458e-bb4b-0c0ce9e874f9 TabularSequencePoint         83.3     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         74.5    24.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         72.0    24.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         71.7    24.4 2349091
                                                  <NA>               Commit         10.2     0.0    <NA>
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.7     8.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.4     6.4       0
                                Sales.Sales Line Label       TabularRefresh          6.0     5.6       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.7     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.6     1.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.5     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.5     1.8  104990
```

## Log

```
2026-11-20T06:57:25Z run 20261120T065449Z-v99p-f55a: variant=v99p-high-cardinality data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T06:57:35Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T06:57:39Z PPU: v99p-high-cardinality is 7bc682e3-1008-458e-bb4b-0c0ce9e874f9, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T06:58:03Z PPU: model size in memory before the refresh: 174.2 MB
2026-11-20T06:58:07Z PPU: trace started (full)
2026-11-20T06:58:07Z PPU: refresh started, request ff599148-9c5c-4213-9c48-c9308bc568a8
2026-11-20T06:59:47Z PPU: refresh refreshed (Completed) 
2026-11-20T07:00:18Z PPU: trace captured 469 events: ProgressReportEnd 424, ExecutionMetrics 34, CommandEnd 11
2026-11-20T07:00:19Z PPU: model size in memory right after the refresh: 209.0 MB
```
