# Harness run 20261120T065415Z-v24a-061e

- Task: refresh
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a4662651-e1fb-4849-a310-41a1ab35faf9
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 664 MB, Power Query 458 MB, duration 1 min, CPU 68 s, rows 3,541,806, model 103 MB (Backup step in SemanticModelLogs)
- Refresh request 4633adbc-83b2-46f8-a18e-e1e9bc695680, 2026-11-20T06:55:22.723 to 2026-11-20T06:56:04.233, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v24a-second-fact on F64 data-1m-v1: refreshed, peak 687 MB (2026-11-19T22:59:59Z).
  - Peak change: -23 MB (-3.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 664 MB vs 716 MB (-52 MB), Power Query 458 MB vs 527 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 82 MB. The refresh may use the SKU maximum minus this: 25,518 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,984 MB: fits (22%); F16 5,038 MB: fits (13%); F32 10,158 MB: fits (7%); F64 25,518 MB: fits (3%); PPU 102,318 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    bf8ceaed-631f-4d6e-8156-09b5c5ce253a TabularSequencePoint         35.4     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         35.1    10.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         33.8    10.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         33.5    10.7 2349091
                      Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh          8.9     3.1       0
                      Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process          7.6     3.1       0
                      Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData          6.5     3.0  980666
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.1     6.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.0     5.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.3     0.3       0
                                                                                       Commit          3.3     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          2.6     0.0       0
```

## Log

```
2026-11-20T06:54:50Z run 20261120T065415Z-v24a-061e: variant=v24a-second-fact data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T06:55:01Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T06:55:05Z F64: v24a-second-fact is bf8ceaed-631f-4d6e-8156-09b5c5ce253a, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T06:55:22Z F64: model size in memory before the refresh: 82.4 MB
2026-11-20T06:55:22Z F64: refresh started, request 4633adbc-83b2-46f8-a18e-e1e9bc695680
2026-11-20T06:56:08Z F64: refresh refreshed (Completed) 
2026-11-20T06:56:08Z F64: monitoring database Monitoring KQL database
2026-11-20T06:58:45Z F64: ExecutionMetrics event found
2026-11-20T06:58:47Z F64: model size in memory right after the refresh: 110.0 MB
```
