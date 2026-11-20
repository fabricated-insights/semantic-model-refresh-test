# Harness run 20261120T043422Z-v99l-061e

- Task: refresh
- Variant: v99l-no-calc-columns
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 5f5df586-284f-4db5-a7ab-2890d64fc11b
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 12,879 MB, Power Query 12,798 MB, duration 18 min, CPU 2,071 s, rows 3,292,315, model 158 MB (Backup step in SemanticModelLogs)
- Refresh request 102f1009-5a63-4ae3-83fa-397f7beffc0b, 2026-11-20T04:35:54.123 to 2026-11-20T04:53:56.35, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99l-no-calc-columns on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 12,879 MB vs 615 MB (+12,264 MB), Power Query 12,798 MB vs 335 MB, model 158 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (420%); F16 5,120 MB: OVER (252%); F32 10,240 MB: OVER (126%); F64 25,600 MB: fits (50%); PPU 102,400 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  d67995b0-588b-4c54-9f78-94503b7068b4 TabularSequencePoint       1069.2     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1065.1    23.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        781.4    22.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        781.1    22.7 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        283.5     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        282.6     2.5       0
                         Customer Stats.Customer Stats           ExecuteSql        182.3     0.0       0
                         Customer Stats.Customer Stats              Process        100.2     2.5       0
                         Customer Stats.Customer Stats             ReadData         99.6     2.0  471482
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.6     1.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.1     8.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          6.9     6.8       0
```

## Log

```
2026-11-20T04:35:24Z run 20261120T043422Z-v99l-061e: variant=v99l-no-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T04:35:36Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T04:35:39Z F64: v99l-no-calc-columns is d67995b0-588b-4c54-9f78-94503b7068b4, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T04:35:54Z F64: model size in memory before the refresh: 0.3 MB
2026-11-20T04:35:54Z F64: refresh started, request 102f1009-5a63-4ae3-83fa-397f7beffc0b
2026-11-20T04:54:07Z F64: refresh refreshed (Completed) 
2026-11-20T04:54:07Z F64: monitoring database Monitoring KQL database
2026-11-20T04:56:44Z F64: ExecutionMetrics event found
2026-11-20T04:56:47Z F64: model size in memory right after the refresh: 194.2 MB
```
