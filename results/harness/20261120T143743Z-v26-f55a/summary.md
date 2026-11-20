# Harness run 20261120T143743Z-v26-f55a

- Task: refresh
- Variant: v26-bad-dax
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3b5ca628-9917-4a93-a3c7-48276c8f17fc
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 694 MB, Power Query 542 MB, duration 1 min, CPU 96 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 415c5a16-6412-4b2b-8ae8-3ee8a018e0c1, 2026-11-20T14:40:40.307 to 2026-11-20T14:41:47.147, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v26-bad-dax on PPU data-1m-v1: refreshed, peak 593 MB (2026-11-20T08:48:36Z).
  - Peak change: +101 MB (+17.0%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 694 MB vs 604 MB (+90 MB), Power Query 542 MB vs 529 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (23%); F16 5,054 MB: fits (14%); F32 10,174 MB: fits (7%); F64 25,534 MB: fits (3%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  2ee61d67-d165-40e2-b3c1-d06e2a600c8e TabularSequencePoint         58.9     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.2    18.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         55.3    18.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         54.2    18.2 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         11.6    13.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.5    11.5       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          7.4     0.1       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          7.3     0.0       0
                                                  <NA>               Commit          4.7     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.8     1.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.7     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.3     1.5       0
```

## Log

```
2026-11-20T14:39:58Z run 20261120T143743Z-v26-f55a: variant=v26-bad-dax data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T14:40:06Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:40:09Z PPU: v26-bad-dax is 2ee61d67-d165-40e2-b3c1-d06e2a600c8e, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:40:36Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-20T14:40:40Z PPU: trace started (full)
2026-11-20T14:40:40Z PPU: refresh started, request 415c5a16-6412-4b2b-8ae8-3ee8a018e0c1
2026-11-20T14:41:50Z PPU: refresh refreshed (Completed) 
2026-11-20T14:42:21Z PPU: trace captured 256 events: ProgressReportEnd 236, ExecutionMetrics 10, CommandEnd 10
2026-11-20T14:42:22Z PPU: model size in memory right after the refresh: 92.7 MB
```
