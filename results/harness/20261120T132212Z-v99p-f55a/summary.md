# Harness run 20261120T132212Z-v99p-f55a

- Task: refresh
- Variant: v99p-high-cardinality
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: b2089bc0-30b0-4358-b653-404d7ad7ccec
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 685 MB, Power Query 529 MB, duration 2 min, CPU 160 s, rows 21,609,543, model 175 MB (Backup step in XMLA trace)
- Refresh request e57e73ec-0866-4643-9821-29f0ee5909c8, 2026-11-20T13:24:59.363 to 2026-11-20T13:26:47.38, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99p-high-cardinality on PPU data-1m-v1: refreshed, peak 686 MB (2026-11-20T07:00:18Z).
  - Peak change: -1 MB (-0.1%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 685 MB vs 666 MB (+19 MB), Power Query 529 MB vs 591 MB, model 175 MB vs 73 MB.
- Model size in memory when the full refresh started: 174 MB. The refresh may use the SKU maximum minus this: 102,226 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,892 MB: fits (24%); F16 4,946 MB: fits (14%); F32 10,066 MB: fits (7%); F64 25,426 MB: fits (3%); PPU 102,226 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    7bc682e3-1008-458e-bb4b-0c0ce9e874f9 TabularSequencePoint         92.7     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         82.6    28.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         79.2    28.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         78.9    28.6 2349091
                                                                    <NA>               Commit         11.8     0.0    <NA>
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.5    10.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.2     7.2       0
                                                  Sales.Sales Line Label       TabularRefresh          7.0     6.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.0     3.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.1     3.2       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          4.0     1.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.0     3.2  104990
```

## Log

```
2026-11-20T13:24:20Z run 20261120T132212Z-v99p-f55a: variant=v99p-high-cardinality data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T13:24:28Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:24:33Z PPU: v99p-high-cardinality is 7bc682e3-1008-458e-bb4b-0c0ce9e874f9, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:24:55Z PPU: model size in memory before the refresh: 174.2 MB
2026-11-20T13:24:59Z PPU: trace started (full)
2026-11-20T13:24:59Z PPU: refresh started, request e57e73ec-0866-4643-9821-29f0ee5909c8
2026-11-20T13:27:10Z PPU: refresh refreshed (Completed) 
2026-11-20T13:27:41Z PPU: trace captured 443 events: ProgressReportEnd 423, ExecutionMetrics 10, CommandEnd 10
2026-11-20T13:27:41Z PPU: model size in memory right after the refresh: 209.0 MB
```
