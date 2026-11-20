# Harness run 20261120T050204Z-v99n-061e

- Task: refresh
- Variant: v99n-text-staging
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 1cb51b86-777d-484f-b242-5073b3d64922
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 803 MB, Power Query 739 MB, duration 11 min, CPU 743 s, rows 21,587,990, model 92 MB (Backup step in SemanticModelLogs)
- Refresh request e2b47230-9821-4cec-b4cf-fa4f1e2abc36, 2026-11-20T05:06:27.923 to 2026-11-20T05:17:44.757, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99n-text-staging on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 803 MB vs 615 MB (+188 MB), Power Query 739 MB vs 335 MB, model 92 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (26%); F16 5,120 MB: fits (16%); F32 10,240 MB: fits (8%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    08ef8a12-823e-4975-bebb-3bc315fc0c5d TabularSequencePoint        668.5     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        659.8    33.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        657.8    33.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        657.4    33.6 2349091
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          8.2     0.6       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql          7.3     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.5     8.2       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.3     2.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.2     6.2       0
                                                  Sales.Sales Line Label       TabularRefresh          6.0     6.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          5.1     2.1       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.9     2.0  104990
```

## Log

```
2026-11-20T05:05:47Z run 20261120T050204Z-v99n-061e: variant=v99n-text-staging data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T05:06:00Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T05:06:04Z F64: v99n-text-staging is 08ef8a12-823e-4975-bebb-3bc315fc0c5d, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T05:06:27Z F64: model size in memory before the refresh: 0.3 MB
2026-11-20T05:06:28Z F64: refresh started, request e2b47230-9821-4cec-b4cf-fa4f1e2abc36
2026-11-20T05:18:10Z F64: refresh refreshed (Completed) 
2026-11-20T05:18:10Z F64: monitoring database Monitoring KQL database
2026-11-20T05:20:47Z F64: ExecutionMetrics event found
2026-11-20T05:20:49Z F64: model size in memory right after the refresh: 124.3 MB
```
