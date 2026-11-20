# Harness run 20261120T011726Z-v99d-061e

- Task: refresh
- Variant: v99d-power-query
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 0a9cdf4e-7575-46b8-9373-6faca1856d4c
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 16,031 MB, Power Query 15,929 MB, duration 18 min, CPU 2,033 s, rows 22,085,043, model 185 MB (Backup step in SemanticModelLogs)
- Refresh request 68466405-1047-4c02-8181-322cf0d45742, 2026-11-20T01:20:21.397 to 2026-11-20T01:38:27.863, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99d-power-query on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 16,031 MB vs 615 MB (+15,416 MB), Power Query 15,929 MB vs 335 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (523%); F16 5,120 MB: OVER (313%); F32 10,240 MB: OVER (157%); F64 25,600 MB: fits (63%); PPU 102,400 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  0effade8-bfbb-4759-b64a-81c4f00d4b76 TabularSequencePoint       1070.2     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1057.0    24.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        700.8    24.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        700.6    24.8 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        356.0     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        329.9     2.5       0
                         Customer Stats.Customer Stats           ExecuteSql        199.3     0.0       0
                         Customer Stats.Customer Stats              Process        130.3     2.4       0
                         Customer Stats.Customer Stats             ReadData        129.7     2.0  471482
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.6     1.9       0
                                Sales.Sales Line Label       TabularRefresh          5.9     5.7       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.9     7.0       0
```

## Log

```
2026-11-20T01:19:43Z run 20261120T011726Z-v99d-061e: variant=v99d-power-query data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T01:19:54Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T01:19:58Z F64: v99d-power-query is 0effade8-bfbb-4759-b64a-81c4f00d4b76, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T01:20:21Z F64: model size in memory before the refresh: 0.3 MB
2026-11-20T01:20:21Z F64: refresh started, request 68466405-1047-4c02-8181-322cf0d45742
2026-11-20T01:38:34Z F64: refresh refreshed (Completed) 
2026-11-20T01:38:34Z F64: monitoring database Monitoring KQL database
2026-11-20T01:40:10Z F64: ExecutionMetrics event found
2026-11-20T01:40:29Z F64: model size in memory right after the refresh: 232.6 MB
```
