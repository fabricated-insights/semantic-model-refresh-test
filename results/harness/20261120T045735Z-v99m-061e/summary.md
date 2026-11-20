# Harness run 20261120T045735Z-v99m-061e

- Task: refresh
- Variant: v99m-baseline-pq
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 277ba41b-9483-459b-9a91-6330e12723f1
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 625 MB, Power Query 270 MB, duration 1 min, CPU 65 s, rows 21,583,972, model 102 MB (Backup step in SemanticModelLogs)
- Refresh request 1a11c6e5-6d48-4417-b3a5-151cefba81de, 2026-11-20T04:58:33.957 to 2026-11-20T04:59:18.317, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99m-baseline-pq on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 625 MB vs 615 MB (+10 MB), Power Query 270 MB vs 335 MB, model 102 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (20%); F16 5,120 MB: fits (12%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (2%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    653e733e-f558-46e8-a7e4-42a4c2c8fddd TabularSequencePoint         38.8     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         34.5    11.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         33.3    11.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         33.0    11.1 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          3.4     4.4       0
                                                                                       Commit          3.4     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          3.3     3.3       0
                                                  Sales.Sales Line Label       TabularRefresh          3.2     3.1       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.3     1.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.4     1.0       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.3     0.3       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          1.3     0.9  104990
```

## Log

```
2026-11-20T04:58:06Z run 20261120T045735Z-v99m-061e: variant=v99m-baseline-pq data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T04:58:18Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T04:58:20Z F64: v99m-baseline-pq is 653e733e-f558-46e8-a7e4-42a4c2c8fddd, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T04:58:33Z F64: model size in memory before the refresh: 0.3 MB
2026-11-20T04:58:34Z F64: refresh started, request 1a11c6e5-6d48-4417-b3a5-151cefba81de
2026-11-20T04:59:19Z F64: refresh refreshed (Completed) 
2026-11-20T04:59:19Z F64: monitoring database Monitoring KQL database
2026-11-20T05:00:55Z F64: ExecutionMetrics event found
2026-11-20T05:01:29Z F64: model size in memory right after the refresh: 136.1 MB
```
