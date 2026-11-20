# Harness run 20261120T063046Z-v21-061e

- Task: refresh
- Variant: v21-pq-group-by
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ca6b753f-b065-4c59-89b0-f8124e7e5ffd
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 3,992 MB, Power Query 3,695 MB, duration 1 min, CPU 99 s, rows 3,032,622, model 85 MB (Backup step in SemanticModelLogs)
- Refresh request 5a3aed6a-ec1d-4012-a2d3-87ecbea35605, 2026-11-20T06:33:33.16 to 2026-11-20T06:34:22.39, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v21-pq-group-by on F64 data-1m-v1: refreshed, peak 4,016 MB (2026-11-19T22:39:42Z).
  - Peak change: -24 MB (-0.6%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 3,992 MB vs 716 MB (+3,276 MB), Power Query 3,695 MB vs 527 MB, model 85 MB vs 73 MB.
- Model size in memory when the full refresh started: 92 MB. The refresh may use the SKU maximum minus this: 25,508 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,974 MB: OVER (134%); F16 5,028 MB: fits (79%); F32 10,148 MB: fits (39%); F64 25,508 MB: fits (16%); PPU 102,308 MB: fits (4%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  215d5bec-5f3c-4bbe-9ebf-b0ca5a0d0e72 TabularSequencePoint         43.4     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         43.1    10.8       0
                         Customer Stats.Customer Stats       TabularRefresh         41.0     1.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         35.8    10.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         35.6    10.7 2349091
                         Customer Stats.Customer Stats           ExecuteSql         34.7     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          7.1     0.0       0
                         Customer Stats.Customer Stats              Process          6.2     1.2       0
                         Customer Stats.Customer Stats             ReadData          5.9     1.0  471482
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.6     6.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.5     5.5       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.6     0.8       0
```

## Log

```
2026-11-20T06:32:59Z run 20261120T063046Z-v21-061e: variant=v21-pq-group-by data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T06:33:10Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T06:33:13Z F64: v21-pq-group-by is 215d5bec-5f3c-4bbe-9ebf-b0ca5a0d0e72, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T06:33:33Z F64: model size in memory before the refresh: 92.1 MB
2026-11-20T06:33:33Z F64: refresh started, request 5a3aed6a-ec1d-4012-a2d3-87ecbea35605
2026-11-20T06:34:43Z F64: refresh refreshed (Completed) 
2026-11-20T06:34:43Z F64: monitoring database Monitoring KQL database
2026-11-20T06:35:52Z F64: ExecutionMetrics event found
2026-11-20T06:35:54Z F64: model size in memory right after the refresh: 118.6 MB
```
