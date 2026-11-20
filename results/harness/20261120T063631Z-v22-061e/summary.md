# Harness run 20261120T063631Z-v22-061e

- Task: refresh
- Variant: v22-dax-calc-columns
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: dfbb0709-e730-4b7e-8279-d0ebc948b34f
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 755 MB, Power Query 699 MB, duration 1 min, CPU 68 s, rows 21,353,868, model 101 MB (Backup step in SemanticModelLogs)
- Refresh request cd781067-dc39-4c00-9f61-20ebcb992f8e, 2026-11-20T06:37:34.817 to 2026-11-20T06:38:22.687, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v22-dax-calc-columns on F64 data-1m-v1: refreshed, peak 622 MB (2026-11-19T22:45:04Z).
  - Peak change: +133 MB (+21.4%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 755 MB vs 716 MB (+39 MB), Power Query 699 MB vs 527 MB, model 101 MB vs 73 MB.
- Model size in memory when the full refresh started: 98 MB. The refresh may use the SKU maximum minus this: 25,502 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,968 MB: fits (25%); F16 5,022 MB: fits (15%); F32 10,142 MB: fits (7%); F64 25,502 MB: fits (3%); PPU 102,302 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  683e80a5-7d57-493c-a708-3a0b8ce5350c TabularSequencePoint         41.1     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         36.6    11.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         35.7    11.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         35.5    11.8 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          3.9     5.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          3.8     3.8       0
                                                                     Commit          3.3     0.0       0
                                Sales.Sales Line Label       TabularRefresh          3.2     3.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.3     0.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.7     0.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.7     0.9  104990
                                   Sales.Customer Name       TabularRefresh          1.1     0.9       0
```

## Log

```
2026-11-20T06:37:08Z run 20261120T063631Z-v22-061e: variant=v22-dax-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T06:37:17Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T06:37:20Z F64: v22-dax-calc-columns is 683e80a5-7d57-493c-a708-3a0b8ce5350c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T06:37:34Z F64: model size in memory before the refresh: 97.8 MB
2026-11-20T06:37:35Z F64: refresh started, request cd781067-dc39-4c00-9f61-20ebcb992f8e
2026-11-20T06:38:45Z F64: refresh refreshed (Completed) 
2026-11-20T06:38:45Z F64: monitoring database Monitoring KQL database
2026-11-20T06:39:34Z F64: ExecutionMetrics event found
2026-11-20T06:39:36Z F64: model size in memory right after the refresh: 132.6 MB
```
