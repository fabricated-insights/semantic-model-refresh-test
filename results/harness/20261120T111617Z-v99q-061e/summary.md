# Harness run 20261120T111617Z-v99q-061e

- Task: refresh
- Variant: v99q-customer-stats
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: d201049d-f705-4454-a861-ea3989e37277
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 3,572 MB, Power Query 3,338 MB, duration 1 min, CPU 125 s, rows 22,055,454, model 114 MB (Backup step in SemanticModelLogs)
- Refresh request eecedaf1-b312-432c-9ec3-00381e6c1d9e, 2026-11-20T11:17:19.19 to 2026-11-20T11:18:21.71, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99q-customer-stats on F64 data-1m-v1: refreshed, peak 3,562 MB (2026-11-20T05:42:25Z).
  - Peak change: +10 MB (+0.3%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 3,572 MB vs 716 MB (+2,856 MB), Power Query 3,338 MB vs 527 MB, model 114 MB vs 73 MB.
- Model size in memory when the full refresh started: 127 MB. The refresh may use the SKU maximum minus this: 25,473 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,939 MB: OVER (122%); F16 4,993 MB: fits (72%); F32 10,113 MB: fits (35%); F64 25,473 MB: fits (14%); PPU 102,273 MB: fits (3%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            d23d017e-5e59-44df-9370-2adb1e080a45 TabularSequencePoint         55.6     0.1       0
                   Customer Stats.Customer Stats       TabularRefresh         53.7     1.4       0
                   Customer Stats.Customer Stats           ExecuteSql         46.2     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         37.4    11.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         35.9    11.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         35.7    11.4 2349091
                   Customer Stats.Customer Stats              Process          7.4     1.3       0
                   Customer Stats.Customer Stats             ReadData          7.1     1.1  471482
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.1     5.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.0     4.0       0
                                                               Commit          3.9     0.0       0
                          Sales.Sales Line Label       TabularRefresh          3.3     3.2       0
```

## Log

```
2026-11-20T11:16:50Z run 20261120T111617Z-v99q-061e: variant=v99q-customer-stats data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T11:17:00Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:17:04Z F64: v99q-customer-stats is d23d017e-5e59-44df-9370-2adb1e080a45, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:17:19Z F64: model size in memory before the refresh: 127.3 MB
2026-11-20T11:17:19Z F64: refresh started, request eecedaf1-b312-432c-9ec3-00381e6c1d9e
2026-11-20T11:18:29Z F64: refresh refreshed (Completed) 
2026-11-20T11:18:29Z F64: monitoring database Monitoring KQL database
2026-11-20T11:20:05Z F64: ExecutionMetrics event found
2026-11-20T11:20:07Z F64: model size in memory right after the refresh: 162.1 MB
```
