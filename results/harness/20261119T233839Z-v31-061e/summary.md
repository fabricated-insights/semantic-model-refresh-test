# Harness run 20261119T233839Z-v31-061e

- Task: refresh
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 44f677ea-51fa-408a-ba86-e982907a5a7b
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 890 MB, Power Query 334 MB, duration 1 min, CPU 91 s, rows 77,732,052, model 223 MB (Backup step in SemanticModelLogs)
- Refresh request c9f6b1a6-760a-420a-bb52-8cabf1519b6d, 2026-11-19T23:39:36.983 to 2026-11-19T23:40:33.823, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v31-calc-columns-row on F64 data-1m-v1: refreshed, peak 913 MB (2026-11-12T08:34:24Z).
  - Peak change: -23 MB (-2.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 890 MB vs 615 MB (+275 MB), Power Query 334 MB vs 335 MB, model 223 MB vs 73 MB.
- Model size in memory when the full refresh started: 234 MB. The refresh may use the SKU maximum minus this: 25,366 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,832 MB: fits (31%); F16 4,886 MB: fits (18%); F32 10,006 MB: fits (9%); F64 25,366 MB: fits (4%); PPU 102,166 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  3c4e1e09-8d9a-4ac4-b01e-178c2d6bae18 TabularSequencePoint         47.6     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         37.1    12.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         35.6    12.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         35.3    12.3 2349091
                                  Sales.Order Line Key       TabularRefresh          7.0     2.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.1     6.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          3.9     3.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.5     0.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      CompressSegment          1.8     3.2       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     0.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.4     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.3     0.8  104990
```

## Log

```
2026-11-19T23:39:12Z run 20261119T233839Z-v31-061e: variant=v31-calc-columns-row data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T23:39:20Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:39:25Z F64: v31-calc-columns-row is 3c4e1e09-8d9a-4ac4-b01e-178c2d6bae18, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:39:36Z F64: model size in memory before the refresh: 233.5 MB
2026-11-19T23:39:37Z F64: refresh started, request c9f6b1a6-760a-420a-bb52-8cabf1519b6d
2026-11-19T23:40:47Z F64: refresh refreshed (Completed) 
2026-11-19T23:40:47Z F64: monitoring database Monitoring KQL database
2026-11-19T23:42:22Z F64: ExecutionMetrics event found
2026-11-19T23:42:24Z F64: model size in memory right after the refresh: 316.8 MB
```
