# Harness run 20261119T215718Z-v18-061e

- Task: refresh
- Variant: v18-pq-10m-summary
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 20c05c24-3ff6-4ebd-893a-1f9d06f45e3c
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,583 MB, Power Query 1,445 MB, duration 1 min, CPU 109 s, rows 2,561,730, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request 64fe85ea-06ae-4046-afd2-d09a21a00b40, 2026-11-19T21:59:52.017 to 2026-11-19T22:00:47.747, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v18-pq-10m-summary on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 1,583 MB vs 615 MB (+968 MB), Power Query 1,445 MB vs 335 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (52%); F16 5,120 MB: fits (31%); F32 10,240 MB: fits (15%); F64 25,600 MB: fits (6%); PPU 102,400 MB: fits (2%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    488c2f22-ab75-4ac9-87fa-79b129d25c49 TabularSequencePoint         49.6     0.0       0
                                   Store Year Summary.Store Year Summary       TabularRefresh         49.5     0.0       0
                                   Store Year Summary.Store Year Summary           ExecuteSql         49.4     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         36.8    11.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         35.4    10.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         35.2    10.9 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.4     6.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.3     5.3       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.1     0.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.8     0.9       0
                                                                                       Commit          2.6     0.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          2.5     0.0       0
```

## Log

```
2026-11-19T21:59:22Z run 20261119T215718Z-v18-061e: variant=v18-pq-10m-summary data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T21:59:31Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T21:59:33Z F64: v18-pq-10m-summary is 488c2f22-ab75-4ac9-87fa-79b129d25c49, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T21:59:51Z F64: model size in memory before the refresh: 0.0 MB
2026-11-19T21:59:52Z F64: refresh started, request 64fe85ea-06ae-4046-afd2-d09a21a00b40
2026-11-19T22:01:02Z F64: refresh refreshed (Completed) 
2026-11-19T22:01:02Z F64: monitoring database Monitoring KQL database
2026-11-19T22:02:37Z F64: ExecutionMetrics event found
2026-11-19T22:02:39Z F64: model size in memory right after the refresh: 92.7 MB
```
