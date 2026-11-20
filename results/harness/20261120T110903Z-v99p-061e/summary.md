# Harness run 20261120T110903Z-v99p-061e

- Task: refresh
- Variant: v99p-high-cardinality
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 8a0082fe-cf87-43c2-b7cb-7e4131a401d6
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,179 MB, Power Query 1,147 MB, duration 1 min, CPU 74 s, rows 21,609,543, model 175 MB (Backup step in SemanticModelLogs)
- Refresh request 9928bf49-32d8-4b2a-8dcd-e0023cd532e9, 2026-11-20T11:12:21.273 to 2026-11-20T11:13:15.013, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99p-high-cardinality on F64 data-1m-v1: refreshed, peak 817 MB (2026-11-20T05:35:02Z).
  - Peak change: +362 MB (+44.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 1,179 MB vs 716 MB (+463 MB), Power Query 1,147 MB vs 527 MB, model 175 MB vs 73 MB.
- Model size in memory when the full refresh started: 174 MB. The refresh may use the SKU maximum minus this: 25,426 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,892 MB: fits (41%); F16 4,946 MB: fits (24%); F32 10,066 MB: fits (12%); F64 25,426 MB: fits (5%); PPU 102,226 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  5369ab57-f76f-43d8-9a2b-7448b05f00d8 TabularSequencePoint         46.8     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         41.8    13.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         40.4    13.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         40.2    13.3 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          3.6     4.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          3.4     3.4       0
                                Sales.Sales Line Label       TabularRefresh          3.3     3.2       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.8     0.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.5     0.8  104990
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.5     0.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.3     0.0       0
                                   Sales.Customer Name       TabularRefresh          1.3     1.0       0
```

## Log

```
2026-11-20T11:11:40Z run 20261120T110903Z-v99p-061e: variant=v99p-high-cardinality data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T11:11:49Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:11:53Z F64: v99p-high-cardinality is 5369ab57-f76f-43d8-9a2b-7448b05f00d8, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:12:21Z F64: model size in memory before the refresh: 174.2 MB
2026-11-20T11:12:21Z F64: refresh started, request 9928bf49-32d8-4b2a-8dcd-e0023cd532e9
2026-11-20T11:13:32Z F64: refresh refreshed (Completed) 
2026-11-20T11:13:32Z F64: monitoring database Monitoring KQL database
2026-11-20T11:15:08Z F64: ExecutionMetrics event found
2026-11-20T11:15:26Z F64: model size in memory right after the refresh: 209.0 MB
```
