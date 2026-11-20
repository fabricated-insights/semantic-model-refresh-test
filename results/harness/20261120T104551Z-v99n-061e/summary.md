# Harness run 20261120T104551Z-v99n-061e

- Task: refresh
- Variant: v99n-text-staging
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 21229922-4d20-4542-b4fe-aee7984f285d
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 688 MB, Power Query 586 MB, duration 10 min, CPU 693 s, rows 21,587,990, model 92 MB (Backup step in SemanticModelLogs)
- Refresh request 81daf2d4-e89c-48f2-98b6-0cca1fe399ad, 2026-11-20T10:49:03.62 to 2026-11-20T10:59:35.143, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99n-text-staging on F64 data-1m-v1: refreshed, peak 803 MB (2026-11-20T05:20:48Z).
  - Peak change: -115 MB (-14.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 688 MB vs 716 MB (-28 MB), Power Query 586 MB vs 527 MB, model 92 MB vs 73 MB.
- Model size in memory when the full refresh started: 91 MB. The refresh may use the SKU maximum minus this: 25,509 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,975 MB: fits (23%); F16 5,029 MB: fits (14%); F32 10,149 MB: fits (7%); F64 25,509 MB: fits (3%); PPU 102,309 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  08ef8a12-823e-4975-bebb-3bc315fc0c5d TabularSequencePoint        622.3     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        615.7    30.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        612.0    30.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        611.5    30.8 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.7     9.4       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.4     1.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.4     7.3       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.7     1.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.5     1.8  104990
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc       TabularRefresh          4.2     0.0       0
                                Sales.Sales Line Label       TabularRefresh          4.2     4.2       0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc           ExecuteSql          4.1     0.0       0
```

## Log

```
2026-11-20T10:48:26Z run 20261120T104551Z-v99n-061e: variant=v99n-text-staging data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T10:48:36Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T10:48:40Z F64: v99n-text-staging is 08ef8a12-823e-4975-bebb-3bc315fc0c5d, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T10:49:03Z F64: model size in memory before the refresh: 90.7 MB
2026-11-20T10:49:03Z F64: refresh started, request 81daf2d4-e89c-48f2-98b6-0cca1fe399ad
2026-11-20T10:59:45Z F64: refresh refreshed (Completed) 
2026-11-20T10:59:46Z F64: monitoring database Monitoring KQL database
2026-11-20T11:01:22Z F64: ExecutionMetrics event found
2026-11-20T11:01:25Z F64: model size in memory right after the refresh: 124.3 MB
```
