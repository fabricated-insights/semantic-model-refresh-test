# Harness run 20261120T102555Z-v99l-061e

- Task: refresh
- Variant: v99l-no-calc-columns
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: df262d68-1ebb-4d72-82e0-b3390ae6f55a
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 12,841 MB, Power Query 12,722 MB, duration 9 min, CPU 912 s, rows 3,292,315, model 158 MB (Backup step in SemanticModelLogs)
- Refresh request 855c1cdb-8423-4eed-9d30-ed3914d690ac, 2026-11-20T10:28:52.947 to 2026-11-20T10:37:56.833, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99l-no-calc-columns on F64 data-1m-v1: refreshed, peak 12,879 MB (2026-11-20T04:56:45Z).
  - Peak change: -38 MB (-0.3%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 12,841 MB vs 716 MB (+12,125 MB), Power Query 12,722 MB vs 527 MB, model 158 MB vs 73 MB.
- Model size in memory when the full refresh started: 168 MB. The refresh may use the SKU maximum minus this: 25,432 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,898 MB: OVER (443%); F16 4,952 MB: OVER (259%); F32 10,072 MB: OVER (127%); F64 25,432 MB: fits (50%); PPU 102,232 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  d67995b0-588b-4c54-9f78-94503b7068b4 TabularSequencePoint        535.3     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        528.9    12.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        386.5    12.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        386.3    12.5 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        142.2     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        136.4     1.3       0
                         Customer Stats.Customer Stats           ExecuteSql         92.3     0.0       0
                         Customer Stats.Customer Stats              Process         44.0     1.3       0
                         Customer Stats.Customer Stats             ReadData         43.7     1.1  471482
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.0     5.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          3.9     3.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.8     0.8       0
```

## Log

```
2026-11-20T10:28:11Z run 20261120T102555Z-v99l-061e: variant=v99l-no-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T10:28:21Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T10:28:25Z F64: v99l-no-calc-columns is d67995b0-588b-4c54-9f78-94503b7068b4, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T10:28:52Z F64: model size in memory before the refresh: 167.7 MB
2026-11-20T10:28:53Z F64: refresh started, request 855c1cdb-8423-4eed-9d30-ed3914d690ac
2026-11-20T10:38:05Z F64: refresh refreshed (Completed) 
2026-11-20T10:38:05Z F64: monitoring database Monitoring KQL database
2026-11-20T10:39:42Z F64: ExecutionMetrics event found
2026-11-20T10:39:45Z F64: model size in memory right after the refresh: 194.2 MB
```
