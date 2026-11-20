# Harness run 20261120T053552Z-v99q-061e

- Task: refresh
- Variant: v99q-customer-stats
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: cc5b976e-57b6-4b6e-adda-aee4a4cb875d
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 3,562 MB, Power Query 3,329 MB, duration 1 min, CPU 110 s, rows 22,055,454, model 114 MB (Backup step in SemanticModelLogs)
- Refresh request afeb0413-a98b-4515-9c17-69b8e9cd75e7, 2026-11-20T05:39:37.79 to 2026-11-20T05:40:33.613, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99q-customer-stats on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 3,562 MB vs 615 MB (+2,947 MB), Power Query 3,329 MB vs 335 MB, model 114 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (116%); F16 5,120 MB: fits (70%); F32 10,240 MB: fits (35%); F64 25,600 MB: fits (14%); PPU 102,400 MB: fits (3%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            d23d017e-5e59-44df-9370-2adb1e080a45 TabularSequencePoint         49.4     0.1       0
                   Customer Stats.Customer Stats       TabularRefresh         48.5     1.5       0
                   Customer Stats.Customer Stats           ExecuteSql         42.5     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         36.3    11.7       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         35.0    11.6       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.8    11.6 2349091
  Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          7.4     0.0       0
  Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          7.2     0.0       0
                   Customer Stats.Customer Stats              Process          5.9     1.5       0
                   Customer Stats.Customer Stats             ReadData          5.6     1.3  471482
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.0     5.1       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          3.9     3.9       0
```

## Log

```
2026-11-20T05:39:05Z run 20261120T053552Z-v99q-061e: variant=v99q-customer-stats data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T05:39:13Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T05:39:16Z F64: v99q-customer-stats is d23d017e-5e59-44df-9370-2adb1e080a45, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T05:39:37Z F64: model size in memory before the refresh: 0.3 MB
2026-11-20T05:39:37Z F64: refresh started, request afeb0413-a98b-4515-9c17-69b8e9cd75e7
2026-11-20T05:40:48Z F64: refresh refreshed (Completed) 
2026-11-20T05:40:48Z F64: monitoring database Monitoring KQL database
2026-11-20T05:42:24Z F64: ExecutionMetrics event found
2026-11-20T05:42:26Z F64: model size in memory right after the refresh: 162.1 MB
```
