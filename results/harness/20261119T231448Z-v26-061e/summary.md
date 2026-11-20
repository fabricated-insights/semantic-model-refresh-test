# Harness run 20261119T231448Z-v26-061e

- Task: refresh
- Variant: v26-bad-dax
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6ae76161-d696-4051-8caf-22c35d7284ff
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,016 MB, Power Query 982 MB, duration 1 min, CPU 56 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 404abcae-11e3-45eb-ae32-75a7cfb3c7fc, 2026-11-19T23:15:45.657 to 2026-11-19T23:16:26.23, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v26-bad-dax on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 1,016 MB vs 615 MB (+401 MB), Power Query 982 MB vs 335 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (33%); F16 5,120 MB: fits (20%); F32 10,240 MB: fits (10%); F64 25,600 MB: fits (4%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    59ff6c07-aebe-46b6-b8b5-9ad2216819f2 TabularSequencePoint         35.5     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         35.2    10.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         33.7    10.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         33.5    10.7 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.0     5.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.9     4.9       0
                                                                                       Commit          2.5     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.4     0.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.5     0.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.4     0.7  104990
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          1.3     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.3     0.3       0
```

## Log

```
2026-11-19T23:15:22Z run 20261119T231448Z-v26-061e: variant=v26-bad-dax data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T23:15:30Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:15:33Z F64: v26-bad-dax is 59ff6c07-aebe-46b6-b8b5-9ad2216819f2, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:15:45Z F64: model size in memory before the refresh: 0.0 MB
2026-11-19T23:15:45Z F64: refresh started, request 404abcae-11e3-45eb-ae32-75a7cfb3c7fc
2026-11-19T23:16:31Z F64: refresh refreshed (Completed) 
2026-11-19T23:16:31Z F64: monitoring database Monitoring KQL database
2026-11-19T23:18:06Z F64: ExecutionMetrics event found
2026-11-19T23:18:07Z F64: model size in memory right after the refresh: 92.7 MB
```
