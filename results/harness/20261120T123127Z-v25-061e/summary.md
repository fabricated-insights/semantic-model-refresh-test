# Harness run 20261120T123127Z-v25-061e

- Task: refresh
- Variant: v25-many-to-many
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6a3e379a-1604-4ae7-9ecd-6fe1869f22e7
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 798 MB, Power Query 713 MB, duration 1 min, CPU 118 s, rows 3,611,040, model 79 MB (Backup step in SemanticModelLogs)
- Refresh request 7b5145cd-a940-4025-8521-0abadc8b799e, 2026-11-20T12:34:16.913 to 2026-11-20T12:35:23.06, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v25-many-to-many on F64 data-1m-v1: refreshed, peak 1,184 MB (2026-11-20T07:11:19Z).
  - Peak change: -386 MB (-32.6%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 798 MB vs 667 MB (+131 MB), Power Query 713 MB vs 592 MB, model 79 MB vs 73 MB.
- Model size in memory when the full refresh started: 71 MB. The refresh may use the SKU maximum minus this: 25,529 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,995 MB: fits (27%); F16 5,049 MB: fits (16%); F32 10,169 MB: fits (8%); F64 25,529 MB: fits (3%); PPU 102,329 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                                  93317245-89ef-4014-abe3-f82efec8ba78 TabularSequencePoint         59.5     0.1       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.9    22.0       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         55.6    21.9       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         55.2    21.8 2349091
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637       TabularRefresh         10.7     5.7       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.6    10.8       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.5     9.5       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637              Process          7.6     5.7       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637             ReadData          7.3     5.5 1049900
                Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.7     1.8       0
                        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          4.2     0.1       0
                        Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          3.9     0.0       0
```

## Log

```
2026-11-20T12:33:45Z run 20261120T123127Z-v25-061e: variant=v25-many-to-many data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T12:33:51Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:33:55Z F64: v25-many-to-many is 93317245-89ef-4014-abe3-f82efec8ba78, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:34:16Z F64: model size in memory before the refresh: 70.6 MB
2026-11-20T12:34:17Z F64: refresh started, request 7b5145cd-a940-4025-8521-0abadc8b799e
2026-11-20T12:35:27Z F64: refresh refreshed (Completed) 
2026-11-20T12:35:27Z F64: monitoring database Monitoring KQL database
2026-11-20T12:38:04Z F64: ExecutionMetrics event found
2026-11-20T12:38:06Z F64: model size in memory right after the refresh: 98.1 MB
```
