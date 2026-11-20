# Harness run 20261120T155210Z-v99l-061e

- Task: refresh
- Variant: v99l-no-calc-columns
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 83734d31-0f28-469e-bf4f-aa157bdf5fc7
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 13,051 MB, Power Query 12,966 MB, duration 5 min, CPU 461 s, rows 3,292,315, model 158 MB (Backup step in SemanticModelLogs)
- Refresh request ac3ecf65-398b-4351-98bd-51b05f068f98, 2026-11-20T15:53:22.69 to 2026-11-20T15:58:16.977, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99l-no-calc-columns on F64 data-1m-v1: refreshed, peak 12,841 MB (2026-11-20T10:39:43Z).
  - Peak change: +210 MB (+1.6%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 13,051 MB vs 667 MB (+12,384 MB), Power Query 12,966 MB vs 592 MB, model 158 MB vs 73 MB.
- Model size in memory when the full refresh started: 168 MB. The refresh may use the SKU maximum minus this: 25,432 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,898 MB: OVER (450%); F16 4,952 MB: OVER (264%); F32 10,072 MB: OVER (130%); F64 25,432 MB: fits (51%); PPU 102,232 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  d67995b0-588b-4c54-9f78-94503b7068b4 TabularSequencePoint        286.9     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        279.7    12.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        140.2     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        139.5    12.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        139.2    11.9 2349091
                         Customer Stats.Customer Stats       TabularRefresh        133.2     1.4       0
                         Customer Stats.Customer Stats           ExecuteSql         96.6     0.0       0
                         Customer Stats.Customer Stats              Process         36.4     1.4       0
                         Customer Stats.Customer Stats             ReadData         36.1     1.2  471482
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.0     5.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          3.9     3.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.2     0.9       0
```

## Log

```
2026-11-20T15:52:51Z run 20261120T155210Z-v99l-061e: variant=v99l-no-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T15:53:02Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T15:53:07Z F64: v99l-no-calc-columns is d67995b0-588b-4c54-9f78-94503b7068b4, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T15:53:22Z F64: model size in memory before the refresh: 167.7 MB
2026-11-20T15:53:22Z F64: refresh started, request ac3ecf65-398b-4351-98bd-51b05f068f98
2026-11-20T15:58:34Z F64: refresh refreshed (Completed) 
2026-11-20T15:58:34Z F64: monitoring database Monitoring KQL database
2026-11-20T16:00:09Z F64: ExecutionMetrics event found
2026-11-20T16:00:28Z F64: model size in memory right after the refresh: 194.2 MB
```
