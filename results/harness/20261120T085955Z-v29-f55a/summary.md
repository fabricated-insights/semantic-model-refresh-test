# Harness run 20261120T085955Z-v29-f55a

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6b262ed1-79fa-4938-831e-538ca618c516
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 729 MB, Power Query 698 MB, duration 2 min, CPU 151 s, rows 2,561,140, model 69 MB (Backup step in XMLA trace)
- Refresh request 3bacdceb-7e91-47da-ac69-f4b60adcde9c, 2026-11-20T09:03:15.093 to 2026-11-20T09:05:15.917, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v29-keys-as-text on PPU data-1m-v1: refreshed, peak 728 MB (2026-11-19T23:27:25Z).
  - Peak change: +1 MB (+0.1%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 729 MB vs 666 MB (+63 MB), Power Query 698 MB vs 591 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 94 MB. The refresh may use the SKU maximum minus this: 102,306 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,972 MB: fits (25%); F16 5,026 MB: fits (15%); F32 10,146 MB: fits (7%); F64 25,506 MB: fits (3%); PPU 102,306 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    b73c5270-73fd-4a15-abcd-c363c7d08602 TabularSequencePoint        111.5     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        106.8    39.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        105.2    39.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        104.6    39.5 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         12.0    10.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.3     3.1       0
                                                                    <NA>               Commit          5.4     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          5.0     3.1       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.6     3.0  104990
                                                      Sales.Order Number       TabularRefresh          4.4     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.6     1.0       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.0     0.1       0
```

## Log

```
2026-11-20T09:02:37Z run 20261120T085955Z-v29-f55a: variant=v29-keys-as-text data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T09:02:45Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T09:02:49Z PPU: v29-keys-as-text is b73c5270-73fd-4a15-abcd-c363c7d08602, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:03:11Z PPU: model size in memory before the refresh: 93.8 MB
2026-11-20T09:03:14Z PPU: trace started (full)
2026-11-20T09:03:15Z PPU: refresh started, request 3bacdceb-7e91-47da-ac69-f4b60adcde9c
2026-11-20T09:05:25Z PPU: refresh refreshed (Completed) 
2026-11-20T09:05:56Z PPU: trace captured 265 events: ProgressReportEnd 233, ExecutionMetrics 22, CommandEnd 10
2026-11-20T09:05:57Z PPU: model size in memory right after the refresh: 141.9 MB
```
