# Harness run 20261119T224557Z-v23-061e

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 064b4a1f-18ec-41a4-aa05-ca63b0264a20
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,406 MB, Power Query 336 MB, duration 1 min, CPU 84 s, rows 16,549,502, model 184 MB (Backup step in SemanticModelLogs)
- Refresh request 479d9e41-c059-4bef-866b-e4f72873e8ad, 2026-11-19T22:48:58.38 to 2026-11-19T22:49:50.307, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v23-dax-calc-tables on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 1,406 MB vs 615 MB (+791 MB), Power Query 336 MB vs 335 MB, model 184 MB vs 73 MB.
- Model size in memory when the full refresh started: 1,296 MB. The refresh may use the SKU maximum minus this: 24,304 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 1,770 MB: fits (79%); F16 3,824 MB: fits (37%); F32 8,944 MB: fits (16%); F64 24,304 MB: fits (6%); PPU 101,104 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            247f4e17-b0ab-46b0-9657-92e852883e58 TabularSequencePoint         43.8     0.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         35.5    10.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         33.7    10.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         33.4    10.7 2349091
                           Sales Copy.Sales Copy       TabularRefresh          7.6     6.3       0
             Product Date Grid.Product Date Grid             VertiPaq          5.6     5.6       0
                           Sales Copy.Sales Copy              Process          5.4     5.3       0
                           Sales Copy.Sales Copy             ReadData          5.2     5.2 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          4.9     5.7       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          4.8     4.8       0
             Product Date Grid.Product Date Grid       TabularRefresh          4.8     4.5       0
             Product Date Grid.Product Date Grid              Process          4.8     4.5       0
```

## Log

```
2026-11-19T22:48:20Z run 20261119T224557Z-v23-061e: variant=v23-dax-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T22:48:28Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:48:41Z F64: v23-dax-calc-tables is 247f4e17-b0ab-46b0-9657-92e852883e58, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:48:58Z F64: model size in memory before the refresh: 1296.3 MB
2026-11-19T22:48:58Z F64: refresh started, request 479d9e41-c059-4bef-866b-e4f72873e8ad
2026-11-19T22:50:08Z F64: refresh refreshed (Completed) 
2026-11-19T22:50:09Z F64: monitoring database Monitoring KQL database
2026-11-19T22:50:58Z F64: ExecutionMetrics event found
2026-11-19T22:51:32Z F64: model size in memory right after the refresh: 185.3 MB
```
