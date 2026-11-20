# Harness run 20261119T225638Z-v24a-061e

- Task: refresh
- Variant: v24a-second-fact
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e1c7492f-1ee5-476a-a44b-56be01f4194a
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 687 MB, Power Query 482 MB, duration 1 min, CPU 117 s, rows 3,541,806, model 103 MB (Backup step in SemanticModelLogs)
- Refresh request c2606b3b-907c-4ab6-8685-e78e3b6f1940, 2026-11-19T22:57:43.143 to 2026-11-19T22:58:49.553, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v24a-second-fact on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 687 MB vs 615 MB (+72 MB), Power Query 482 MB vs 335 MB, model 103 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (22%); F16 5,120 MB: fits (13%); F32 10,240 MB: fits (7%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  bf8ceaed-631f-4d6e-8156-09b5c5ce253a TabularSequencePoint         57.4     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         56.8    18.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         54.0    18.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         53.7    18.2 2349091
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa       TabularRefresh         13.3     5.5       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa              Process         12.8     5.5       0
    Orders.Orders-94d3e280-e417-4d9d-ad5b-23ddbd1891fa             ReadData         11.0     5.4  980666
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          9.3    10.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          9.1     9.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.1     1.7       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          3.0     1.6       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.9     1.6  104990
```

## Log

```
2026-11-19T22:57:17Z run 20261119T225638Z-v24a-061e: variant=v24a-second-fact data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T22:57:26Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:57:29Z F64: v24a-second-fact is bf8ceaed-631f-4d6e-8156-09b5c5ce253a, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:57:43Z F64: model size in memory before the refresh: 0.0 MB
2026-11-19T22:57:43Z F64: refresh started, request c2606b3b-907c-4ab6-8685-e78e3b6f1940
2026-11-19T22:58:53Z F64: refresh refreshed (Completed) 
2026-11-19T22:58:53Z F64: monitoring database Monitoring KQL database
2026-11-19T22:59:42Z F64: ExecutionMetrics event found
2026-11-19T23:00:00Z F64: model size in memory right after the refresh: 110.0 MB
```
