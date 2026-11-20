# Harness run 20261119T232946Z-v29-061e

- Task: refresh
- Variant: v29-keys-as-text
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 8ca9b567-e4ed-4ecb-8edb-f8a16f022501
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 766 MB, Power Query 698 MB, duration 1 min, CPU 107 s, rows 2,561,140, model 69 MB (Backup step in SemanticModelLogs)
- Refresh request 16d41044-c82f-4228-ac7e-be47fe07028e, 2026-11-19T23:30:48.637 to 2026-11-19T23:31:57.433, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v29-keys-as-text on F64 data-1m-v1: refreshed, peak 1,735 MB (2026-11-13T09:45:53Z).
  - Peak change: -969 MB (-55.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 766 MB vs 615 MB (+151 MB), Power Query 698 MB vs 335 MB, model 69 MB vs 73 MB.
- Model size in memory when the full refresh started: 94 MB. The refresh may use the SKU maximum minus this: 25,506 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,972 MB: fits (26%); F16 5,026 MB: fits (15%); F32 10,146 MB: fits (8%); F64 25,506 MB: fits (3%); PPU 102,306 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    8a2beb05-98b9-4e44-92de-799777abce23 TabularSequencePoint         59.1     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         55.7    25.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         50.7    25.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         49.4    25.5 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.5    10.5       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh         10.2     0.6       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          9.5     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          9.3     0.0       0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          9.3     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.0     1.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          4.8     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          3.4     0.0       0
```

## Log

```
2026-11-19T23:30:20Z run 20261119T232946Z-v29-061e: variant=v29-keys-as-text data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T23:30:30Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:30:34Z F64: v29-keys-as-text is 8a2beb05-98b9-4e44-92de-799777abce23, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:30:48Z F64: model size in memory before the refresh: 93.8 MB
2026-11-19T23:30:48Z F64: refresh started, request 16d41044-c82f-4228-ac7e-be47fe07028e
2026-11-19T23:31:59Z F64: refresh refreshed (Completed) 
2026-11-19T23:31:59Z F64: monitoring database Monitoring KQL database
2026-11-19T23:33:34Z F64: ExecutionMetrics event found
2026-11-19T23:33:36Z F64: model size in memory right after the refresh: 141.9 MB
```
