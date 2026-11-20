# Harness run 20261120T075803Z-v34-061e

- Task: refresh
- Variant: v34-auto-date-time-no-date-table
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 109a45ad-9a73-477d-b7e1-0ae0ca42ca52
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 556 MB, Power Query 270 MB, duration 1 min, CPU 105 s, rows 2,847,496, model 74 MB (Backup step in SemanticModelLogs)
- Refresh request 6e94810c-afb6-4059-9733-a5e67aef7b5b, 2026-11-20T08:01:03.877 to 2026-11-20T08:02:11.407, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v34-auto-date-time-no-date-table on F64 data-1m-v1: refreshed, peak 550 MB (2026-11-19T23:56:59Z).
  - Peak change: +6 MB (+1.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 556 MB vs 716 MB (-160 MB), Power Query 270 MB vs 527 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 25,530 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (19%); F16 5,050 MB: fits (11%); F32 10,170 MB: fits (5%); F64 25,530 MB: fits (2%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  8876d3c4-cd50-45e6-b465-6758c70c6ca0 TabularSequencePoint         59.1     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.4    21.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         55.5    21.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         55.1    20.8 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.3    11.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.1    10.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.9     1.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.7     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.6     1.8       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.5     1.8  104990
        Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          2.4     0.1       0
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          2.3     0.1       0
```

## Log

```
2026-11-20T08:00:19Z run 20261120T075803Z-v34-061e: variant=v34-auto-date-time-no-date-table data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T08:00:29Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:00:34Z F64: v34-auto-date-time-no-date-table is 8876d3c4-cd50-45e6-b465-6758c70c6ca0, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:01:03Z F64: model size in memory before the refresh: 70.3 MB
2026-11-20T08:01:04Z F64: refresh started, request 6e94810c-afb6-4059-9733-a5e67aef7b5b
2026-11-20T08:02:14Z F64: refresh refreshed (Completed) 
2026-11-20T08:02:14Z F64: monitoring database Monitoring KQL database
2026-11-20T08:03:51Z F64: ExecutionMetrics event found
2026-11-20T08:04:26Z F64: model size in memory right after the refresh: 96.9 MB
```
