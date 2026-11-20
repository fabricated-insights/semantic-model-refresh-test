# Harness run 20261119T222206Z-v20-061e

- Task: refresh
- Variant: v20-pq-sort
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3c8ab43b-5bfd-4a35-9ba4-12615e399fb2
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 5,200 MB, Power Query 4,994 MB, duration 5 min, CPU 363 s, rows 2,561,140, model 72 MB (Backup step in SemanticModelLogs)
- Refresh request 1909c0a7-b91a-4312-bbea-82e27f16bda8, 2026-11-19T22:23:18.05 to 2026-11-19T22:28:13.257, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v20-pq-sort on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 5,200 MB vs 615 MB (+4,585 MB), Power Query 4,994 MB vs 335 MB, model 72 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (170%); F16 5,120 MB: OVER (102%); F32 10,240 MB: fits (51%); F64 25,600 MB: fits (20%); PPU 102,400 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    d6f42335-d4fb-411e-9ca5-a063e204bb89 TabularSequencePoint        287.6     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        274.9    18.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        183.1    18.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        182.7    17.9 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql         91.7     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.9     8.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.8     6.7       0
                                                                                       Commit          4.4     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.3     1.5       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.3     1.5       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.2     1.4  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          2.1     0.6       0
```

## Log

```
2026-11-19T22:22:50Z run 20261119T222206Z-v20-061e: variant=v20-pq-sort data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T22:23:02Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:23:05Z F64: v20-pq-sort is d6f42335-d4fb-411e-9ca5-a063e204bb89, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:23:17Z F64: model size in memory before the refresh: 0.0 MB
2026-11-19T22:23:18Z F64: refresh started, request 1909c0a7-b91a-4312-bbea-82e27f16bda8
2026-11-19T22:28:29Z F64: refresh refreshed (Completed) 
2026-11-19T22:28:29Z F64: monitoring database Monitoring KQL database
2026-11-19T22:31:06Z F64: ExecutionMetrics event found
2026-11-19T22:31:09Z F64: model size in memory right after the refresh: 91.9 MB
```
