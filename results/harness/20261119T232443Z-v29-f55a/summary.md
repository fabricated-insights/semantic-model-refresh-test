# Harness run 20261119T232443Z-v29-f55a

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a654315c-5eb8-4b61-9587-2ad549e36bc1
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 728 MB, Power Query 574 MB, duration 1 min, CPU 108 s, rows 2,561,140, model 69 MB (Backup step in XMLA trace)
- Refresh request 4cdbf82a-bca4-4fb9-bcbd-e86d2f85f18a, 2026-11-19T23:25:44.45 to 2026-11-19T23:26:49.017, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v29-keys-as-text on PPU data-1m-v1: refreshed, peak 642 MB (2026-11-17T06:46:34Z).
  - Peak change: +86 MB (+13.4%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 728 MB vs 551 MB (+177 MB), Power Query 574 MB vs 298 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 94 MB. The refresh may use the SKU maximum minus this: 102,306 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,972 MB: fits (24%); F16 5,026 MB: fits (14%); F32 10,146 MB: fits (7%); F64 25,506 MB: fits (3%); PPU 102,306 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  b73c5270-73fd-4a15-abcd-c363c7d08602 TabularSequencePoint         57.6     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         54.4    27.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         52.5    27.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         51.4    27.3 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.1    11.0       0
                                                  <NA>               Commit          4.8     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.5     2.0       0
                                    Sales.Order Number       TabularRefresh          2.9     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.7     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.6     2.0  104990
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          2.4     0.0       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          2.3     0.0       0
```

## Log

```
2026-11-19T23:25:13Z run 20261119T232443Z-v29-f55a: variant=v29-keys-as-text data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T23:25:21Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:25:26Z PPU: v29-keys-as-text is b73c5270-73fd-4a15-abcd-c363c7d08602, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:25:40Z PPU: model size in memory before the refresh: 93.8 MB
2026-11-19T23:25:44Z PPU: trace started (full)
2026-11-19T23:25:44Z PPU: refresh started, request 4cdbf82a-bca4-4fb9-bcbd-e86d2f85f18a
2026-11-19T23:26:54Z PPU: refresh refreshed (Completed) 
2026-11-19T23:27:25Z PPU: trace captured 279 events: ProgressReportEnd 234, ExecutionMetrics 34, CommandEnd 11
2026-11-19T23:27:26Z PPU: model size in memory right after the refresh: 141.9 MB
```
