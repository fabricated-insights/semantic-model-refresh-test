# Harness run 20261119T223200Z-v21-061e

- Task: refresh
- Variant: v21-pq-group-by
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 65c65cf4-ef93-4cf5-bbf9-ddb89f6126a8
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 4,016 MB, Power Query 3,741 MB, duration 1 min, CPU 98 s, rows 3,032,622, model 84 MB (Backup step in SemanticModelLogs)
- Refresh request 5a230a0a-20af-4cbf-845f-ea770b5bf2eb, 2026-11-19T22:35:54.273 to 2026-11-19T22:36:42.823, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v21-pq-group-by on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 4,016 MB vs 615 MB (+3,401 MB), Power Query 3,741 MB vs 335 MB, model 84 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (131%); F16 5,120 MB: fits (78%); F32 10,240 MB: fits (39%); F64 25,600 MB: fits (16%); PPU 102,400 MB: fits (4%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            215d5bec-5f3c-4bbe-9ebf-b0ca5a0d0e72 TabularSequencePoint         42.4     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         42.0    10.8       0
                   Customer Stats.Customer Stats       TabularRefresh         39.6     1.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         34.8    10.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         34.5    10.7 2349091
                   Customer Stats.Customer Stats           ExecuteSql         33.4     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          7.1     0.0       0
                   Customer Stats.Customer Stats              Process          6.1     1.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.9     6.9       0
                   Customer Stats.Customer Stats             ReadData          5.8     1.1  471482
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.7     5.7       0
                                                               Commit          3.8     0.0       0
```

## Log

```
2026-11-19T22:35:14Z run 20261119T223200Z-v21-061e: variant=v21-pq-group-by data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T22:35:28Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:35:31Z F64: v21-pq-group-by is 215d5bec-5f3c-4bbe-9ebf-b0ca5a0d0e72, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:35:54Z F64: model size in memory before the refresh: 0.0 MB
2026-11-19T22:35:54Z F64: refresh started, request 5a230a0a-20af-4cbf-845f-ea770b5bf2eb
2026-11-19T22:37:04Z F64: refresh refreshed (Completed) 
2026-11-19T22:37:05Z F64: monitoring database Monitoring KQL database
2026-11-19T22:39:41Z F64: ExecutionMetrics event found
2026-11-19T22:39:43Z F64: model size in memory right after the refresh: 118.6 MB
```
