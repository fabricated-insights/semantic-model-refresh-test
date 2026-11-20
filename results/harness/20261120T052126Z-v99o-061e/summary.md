# Harness run 20261120T052126Z-v99o-061e

- Task: refresh
- Variant: v99o-sorts
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 8590f0cd-2c83-4f7d-bdd2-3863439c54f2
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 5,307 MB, Power Query 5,001 MB, duration 4 min, CPU 344 s, rows 21,583,972, model 99 MB (Backup step in SemanticModelLogs)
- Refresh request 35c9fcfe-6243-40e2-99a5-673ae3038e51, 2026-11-20T05:22:29.847 to 2026-11-20T05:27:06.247, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99o-sorts on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 5,307 MB vs 615 MB (+4,692 MB), Power Query 5,001 MB vs 335 MB, model 99 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (173%); F16 5,120 MB: OVER (104%); F32 10,240 MB: fits (52%); F64 25,600 MB: fits (21%); PPU 102,400 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  de183c23-bc85-4924-a529-71615701050c TabularSequencePoint        266.9     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        257.4    19.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        156.1    19.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        155.8    19.4 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        101.1     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          9.8     1.5       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          7.4     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql          7.4     0.0       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          7.2     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.5     8.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.2     6.2       0
                                Sales.Sales Line Label       TabularRefresh          5.7     5.5       0
```

## Log

```
2026-11-20T05:21:59Z run 20261120T052126Z-v99o-061e: variant=v99o-sorts data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T05:22:13Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T05:22:16Z F64: v99o-sorts is de183c23-bc85-4924-a529-71615701050c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T05:22:29Z F64: model size in memory before the refresh: 0.3 MB
2026-11-20T05:22:30Z F64: refresh started, request 35c9fcfe-6243-40e2-99a5-673ae3038e51
2026-11-20T05:27:11Z F64: refresh refreshed (Completed) 
2026-11-20T05:27:11Z F64: monitoring database Monitoring KQL database
2026-11-20T05:28:47Z F64: ExecutionMetrics event found
2026-11-20T05:28:49Z F64: model size in memory right after the refresh: 133.8 MB
```
