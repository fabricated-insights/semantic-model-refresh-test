# Harness run 20261119T230750Z-v25-061e

- Task: refresh
- Variant: v25-many-to-many
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: b53d5877-15db-442a-b901-adc702960892
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 902 MB, Power Query 821 MB, duration 1 min, CPU 109 s, rows 3,611,040, model 79 MB (Backup step in SemanticModelLogs)
- Refresh request ff2660bc-d323-40ab-ae63-8e9bda938dcc, 2026-11-19T23:10:52.057 to 2026-11-19T23:11:56.9, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v25-many-to-many on F64 data-1m-v1: refreshed, peak 614 MB (2026-11-11T19:55:26Z).
  - Peak change: +288 MB (+46.9%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 902 MB vs 615 MB (+287 MB), Power Query 821 MB vs 335 MB, model 79 MB vs 73 MB.
- Model size in memory when the full refresh started: 71 MB. The refresh may use the SKU maximum minus this: 25,529 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,995 MB: fits (30%); F16 5,049 MB: fits (18%); F32 10,169 MB: fits (9%); F64 25,529 MB: fits (4%); PPU 102,329 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                                  93317245-89ef-4014-abe3-f82efec8ba78 TabularSequencePoint         56.5     0.1       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         55.8    18.1       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         53.2    18.1       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         52.8    17.9 2349091
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637       TabularRefresh          9.5     4.5       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.5    10.6       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.3     9.3       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637              Process          7.3     4.5       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637             ReadData          7.1     4.4 1049900
                Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.3     1.9       0
                Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     1.9       0
                Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.9     1.9  104990
```

## Log

```
2026-11-19T23:10:16Z run 20261119T230750Z-v25-061e: variant=v25-many-to-many data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T23:10:25Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:10:29Z F64: v25-many-to-many is 93317245-89ef-4014-abe3-f82efec8ba78, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:10:51Z F64: model size in memory before the refresh: 70.6 MB
2026-11-19T23:10:52Z F64: refresh started, request ff2660bc-d323-40ab-ae63-8e9bda938dcc
2026-11-19T23:12:02Z F64: refresh refreshed (Completed) 
2026-11-19T23:12:02Z F64: monitoring database Monitoring KQL database
2026-11-19T23:13:38Z F64: ExecutionMetrics event found
2026-11-19T23:14:12Z F64: model size in memory right after the refresh: 98.1 MB
```
