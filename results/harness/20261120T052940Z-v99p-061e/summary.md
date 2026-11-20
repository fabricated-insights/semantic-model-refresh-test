# Harness run 20261120T052940Z-v99p-061e

- Task: refresh
- Variant: v99p-high-cardinality
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 8d624415-544d-41ae-9239-c8ba7c5a9117
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 817 MB, Power Query 404 MB, duration 1 min, CPU 135 s, rows 21,609,543, model 175 MB (Backup step in SemanticModelLogs)
- Refresh request a50b2a7a-3468-42eb-842a-bda4225e6f2f, 2026-11-20T05:30:43.48 to 2026-11-20T05:32:16.297, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99p-high-cardinality on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 817 MB vs 615 MB (+202 MB), Power Query 404 MB vs 335 MB, model 175 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (27%); F16 5,120 MB: fits (16%); F32 10,240 MB: fits (8%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  5369ab57-f76f-43d8-9a2b-7448b05f00d8 TabularSequencePoint         80.4     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         71.8    24.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         69.7    24.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         69.5    24.7 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.3     9.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.0     7.0       0
                                Sales.Sales Line Label       TabularRefresh          5.7     5.5       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.9     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.8     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.7     1.9  104990
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.5     0.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          2.4     0.0       0
```

## Log

```
2026-11-20T05:30:13Z run 20261120T052940Z-v99p-061e: variant=v99p-high-cardinality data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T05:30:24Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T05:30:28Z F64: v99p-high-cardinality is 5369ab57-f76f-43d8-9a2b-7448b05f00d8, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T05:30:43Z F64: model size in memory before the refresh: 0.3 MB
2026-11-20T05:30:43Z F64: refresh started, request a50b2a7a-3468-42eb-842a-bda4225e6f2f
2026-11-20T05:32:24Z F64: refresh refreshed (Completed) 
2026-11-20T05:32:24Z F64: monitoring database Monitoring KQL database
2026-11-20T05:35:01Z F64: ExecutionMetrics event found
2026-11-20T05:35:03Z F64: model size in memory right after the refresh: 209.0 MB
```
