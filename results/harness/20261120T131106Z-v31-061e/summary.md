# Harness run 20261120T131106Z-v31-061e

- Task: refresh
- Variant: v31-calc-columns-row
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e2268d08-d96c-4772-bc18-8dee637b2576
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,239 MB, Power Query 1,199 MB, duration 1 min, CPU 151 s, rows 77,732,052, model 223 MB (Backup step in SemanticModelLogs)
- Refresh request 1af5b972-ed90-4b8e-ade4-d84da6e13fa1, 2026-11-20T13:12:32.98 to 2026-11-20T13:14:03.033, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v31-calc-columns-row on F64 data-1m-v1: refreshed, peak 990 MB (2026-11-20T07:47:59Z).
  - Peak change: +249 MB (+25.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 1,239 MB vs 667 MB (+572 MB), Power Query 1,199 MB vs 592 MB, model 223 MB vs 73 MB.
- Model size in memory when the full refresh started: 234 MB. The refresh may use the SKU maximum minus this: 25,366 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,832 MB: fits (44%); F16 4,886 MB: fits (25%); F32 10,006 MB: fits (12%); F64 25,366 MB: fits (5%); PPU 102,166 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  3c4e1e09-8d9a-4ac4-b01e-178c2d6bae18 TabularSequencePoint         76.0     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         57.4    23.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         56.1    23.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         55.2    23.3 2349091
                                  Sales.Order Line Key       TabularRefresh         13.4     3.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.1    14.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.7     9.7       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.6     1.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba      CompressSegment          2.9     5.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.7     1.5       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.6     1.5  104990
                                   Sales.Customer Name       TabularRefresh          1.9     1.6       0
```

## Log

```
2026-11-20T13:12:04Z run 20261120T131106Z-v31-061e: variant=v31-calc-columns-row data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T13:12:11Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:12:17Z F64: v31-calc-columns-row is 3c4e1e09-8d9a-4ac4-b01e-178c2d6bae18, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:12:32Z F64: model size in memory before the refresh: 233.5 MB
2026-11-20T13:12:33Z F64: refresh started, request 1af5b972-ed90-4b8e-ade4-d84da6e13fa1
2026-11-20T13:14:13Z F64: refresh refreshed (Completed) 
2026-11-20T13:14:14Z F64: monitoring database Monitoring KQL database
2026-11-20T13:15:49Z F64: ExecutionMetrics event found
2026-11-20T13:15:51Z F64: model size in memory right after the refresh: 316.8 MB
```
