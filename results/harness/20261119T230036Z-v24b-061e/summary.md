# Harness run 20261119T230036Z-v24b-061e

- Task: refresh
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 41a32c3f-a71f-466e-ad00-8bf3d3f76f23
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 661 MB, Power Query 456 MB, duration 1 min, CPU 73 s, rows 3,541,806, model 103 MB (Backup step in SemanticModelLogs)
- Refresh request d9c92122-d1c3-479a-a239-5955897d4520, 2026-11-19T23:04:35.88 to 2026-11-19T23:05:20.107, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v24b-second-fact-bidirectional on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 661 MB vs 615 MB (+46 MB), Power Query 456 MB vs 335 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (22%); F16 5,120 MB: fits (13%); F32 10,240 MB: fits (6%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  a21050a7-7531-4f04-a061-b795aa01fdf7 TabularSequencePoint         38.1     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         37.7    11.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         36.5    11.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         36.2    11.5 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh          8.8     3.0       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process          7.8     3.0       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData          6.9     3.0  980666
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.2     6.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.1     5.1       0
                                                                     Commit          3.8     0.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.5     0.9       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          1.6     0.8       0
```

## Log

```
2026-11-19T23:04:03Z run 20261119T230036Z-v24b-061e: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T23:04:11Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:04:13Z F64: v24b-second-fact-bidirectional is a21050a7-7531-4f04-a061-b795aa01fdf7, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:04:35Z F64: model size in memory before the refresh: 0.0 MB
2026-11-19T23:04:36Z F64: refresh started, request d9c92122-d1c3-479a-a239-5955897d4520
2026-11-19T23:05:21Z F64: refresh refreshed (Completed) 
2026-11-19T23:05:21Z F64: monitoring database Monitoring KQL database
2026-11-19T23:06:56Z F64: ExecutionMetrics event found
2026-11-19T23:07:14Z F64: model size in memory right after the refresh: 110.0 MB
```
