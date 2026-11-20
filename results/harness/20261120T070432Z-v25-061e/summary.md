# Harness run 20261120T070432Z-v25-061e

- Task: refresh
- Variant: v25-many-to-many
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 578381ab-3876-4fbc-8083-323ff1f528a3
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,184 MB, Power Query 1,083 MB, duration 1 min, CPU 151 s, rows 3,611,040, model 79 MB (Backup step in SemanticModelLogs)
- Refresh request 91885bbb-93e4-4337-9047-27eb12d7d5cd, 2026-11-20T07:07:29.353 to 2026-11-20T07:09:01.253, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v25-many-to-many on F64 data-1m-v1: refreshed, peak 902 MB (2026-11-19T23:14:11Z).
  - Peak change: +282 MB (+31.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 1,184 MB vs 716 MB (+468 MB), Power Query 1,083 MB vs 527 MB, model 79 MB vs 73 MB.
- Model size in memory when the full refresh started: 71 MB. The refresh may use the SKU maximum minus this: 25,529 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,995 MB: fits (40%); F16 5,049 MB: fits (23%); F32 10,169 MB: fits (12%); F64 25,529 MB: fits (5%); PPU 102,329 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                                  93317245-89ef-4014-abe3-f82efec8ba78 TabularSequencePoint         82.3     0.1       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         79.8    25.4       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         78.7    25.3       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         77.7    25.1 2349091
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         14.7    16.1       0
                      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         14.5    14.4       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637       TabularRefresh         11.6     5.9       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637              Process         10.2     5.9       0
Customer Segment.Customer Segment-dbaeade0-9f07-402d-9d2e-42c32fdcb637             ReadData          9.9     5.7 1049900
                        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          7.8     0.1       0
                        Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          7.5     0.0       0
                Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.0     2.5       0
```

## Log

```
2026-11-20T07:06:52Z run 20261120T070432Z-v25-061e: variant=v25-many-to-many data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T07:07:02Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:07:07Z F64: v25-many-to-many is 93317245-89ef-4014-abe3-f82efec8ba78, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:07:29Z F64: model size in memory before the refresh: 70.6 MB
2026-11-20T07:07:29Z F64: refresh started, request 91885bbb-93e4-4337-9047-27eb12d7d5cd
2026-11-20T07:09:10Z F64: refresh refreshed (Completed) 
2026-11-20T07:09:10Z F64: monitoring database Monitoring KQL database
2026-11-20T07:10:45Z F64: ExecutionMetrics event found
2026-11-20T07:11:20Z F64: model size in memory right after the refresh: 98.1 MB
```
