# Harness run 20261119T231256Z-v26-f55a

- Task: refresh
- Variant: v26-bad-dax
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f7e4b4ac-2010-43ae-b8d6-e55edb66ff63
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 614 MB, Power Query 523 MB, duration 1 min, CPU 109 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 1e81d93c-b398-48a4-8824-34924e0bd8da, 2026-11-19T23:13:58.723 to 2026-11-19T23:15:09.253, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v26-bad-dax on PPU data-1m-v1: refreshed, peak 614 MB (2026-11-17T06:26:27Z).
  - Peak change: +0 MB (+0.0%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 614 MB vs 551 MB (+63 MB), Power Query 523 MB vs 298 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (20%); F16 5,054 MB: fits (12%); F32 10,174 MB: fits (6%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  2ee61d67-d165-40e2-b3c1-d06e2a600c8e TabularSequencePoint         63.6     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         62.8    20.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         59.8    20.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         59.3    20.1 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.4    12.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.2    11.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.1     2.4       0
                                                  <NA>               Commit          5.0     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     2.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.9     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.8     2.3  104990
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.4     0.1       0
```

## Log

```
2026-11-19T23:13:32Z run 20261119T231256Z-v26-f55a: variant=v26-bad-dax data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T23:13:38Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:13:41Z PPU: v26-bad-dax is 2ee61d67-d165-40e2-b3c1-d06e2a600c8e, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:13:55Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-19T23:13:58Z PPU: trace started (full)
2026-11-19T23:13:58Z PPU: refresh started, request 1e81d93c-b398-48a4-8824-34924e0bd8da
2026-11-19T23:15:39Z PPU: refresh refreshed (Completed) 
2026-11-19T23:16:09Z PPU: trace captured 282 events: ProgressReportEnd 237, ExecutionMetrics 34, CommandEnd 11
2026-11-19T23:16:10Z PPU: model size in memory right after the refresh: 92.7 MB
```
