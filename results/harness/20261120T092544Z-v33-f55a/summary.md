# Harness run 20261120T092544Z-v33-f55a

- Task: refresh
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 08394a09-df83-48cd-a80d-3d5e402de6fe
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 554 MB, Power Query 271 MB, duration 1 min, CPU 94 s, rows 2,791,244, model 74 MB (Backup step in XMLA trace)
- Refresh request 4ea44741-a9a2-47fb-80b5-e8e58cb8a204, 2026-11-20T09:29:16.91 to 2026-11-20T09:30:18.98, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v33-auto-date-time on PPU data-1m-v1: refreshed, peak 554 MB (2026-11-19T23:46:28Z).
  - Peak change: +0 MB (+0.0%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 554 MB vs 666 MB (-112 MB), Power Query 271 MB vs 591 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 102,330 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (18%); F16 5,050 MB: fits (11%); F32 10,170 MB: fits (5%); F64 25,530 MB: fits (2%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    fbb53e0d-05a8-434a-9ad9-ec2dac2730d7 TabularSequencePoint         53.9     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         53.2    17.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         50.0    17.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         49.6    17.8 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.1    10.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.9     8.9       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.6     1.6       0
                                                                    <NA>               Commit          4.2     0.0    <NA>
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          3.2     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.0     0.6       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.3     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          2.3     0.0       0
```

## Log

```
2026-11-20T09:28:41Z run 20261120T092544Z-v33-f55a: variant=v33-auto-date-time data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T09:28:48Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T09:28:51Z PPU: v33-auto-date-time is fbb53e0d-05a8-434a-9ad9-ec2dac2730d7, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:29:13Z PPU: model size in memory before the refresh: 69.7 MB
2026-11-20T09:29:16Z PPU: trace started (full)
2026-11-20T09:29:17Z PPU: refresh started, request 4ea44741-a9a2-47fb-80b5-e8e58cb8a204
2026-11-20T09:30:27Z PPU: refresh refreshed (Completed) 
2026-11-20T09:30:58Z PPU: trace captured 379 events: ProgressReportEnd 347, ExecutionMetrics 22, CommandEnd 10
2026-11-20T09:30:58Z PPU: model size in memory right after the refresh: 96.2 MB
```
