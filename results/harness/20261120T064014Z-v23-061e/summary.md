# Harness run 20261120T064014Z-v23-061e

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f87190be-6e28-4903-bc7d-a384d5f571b1
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,405 MB, Power Query 340 MB, duration 1 min, CPU 140 s, rows 16,549,502, model 184 MB (Backup step in SemanticModelLogs)
- Refresh request 7ae621a3-84fc-41ae-8f6e-004644607015, 2026-11-20T06:43:20.673 to 2026-11-20T06:44:42.563, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v23-dax-calc-tables on F64 data-1m-v1: refreshed, peak 1,406 MB (2026-11-19T22:51:31Z).
  - Peak change: -1 MB (-0.1%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 1,405 MB vs 716 MB (+689 MB), Power Query 340 MB vs 527 MB, model 184 MB vs 73 MB.
- Model size in memory when the full refresh started: 150 MB. The refresh may use the SKU maximum minus this: 25,450 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,916 MB: fits (48%); F16 4,970 MB: fits (28%); F32 10,090 MB: fits (14%); F64 25,450 MB: fits (6%); PPU 102,250 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            247f4e17-b0ab-46b0-9657-92e852883e58 TabularSequencePoint         70.2     0.3       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         56.0    19.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         53.3    19.1       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         52.7    19.0 2349091
                           Sales Copy.Sales Copy       TabularRefresh         13.0    10.8       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.8    11.7       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.6    10.3       0
             Product Date Grid.Product Date Grid             VertiPaq          9.7     9.8       0
                           Sales Copy.Sales Copy              Process          9.3     9.1       0
                           Sales Copy.Sales Copy             ReadData          9.0     9.0 2349091
             Product Date Grid.Product Date Grid       TabularRefresh          7.7     7.1       0
             Product Date Grid.Product Date Grid              Process          7.7     7.1       0
```

## Log

```
2026-11-20T06:42:42Z run 20261120T064014Z-v23-061e: variant=v23-dax-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T06:42:53Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T06:42:57Z F64: v23-dax-calc-tables is 247f4e17-b0ab-46b0-9657-92e852883e58, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T06:43:20Z F64: model size in memory before the refresh: 149.9 MB
2026-11-20T06:43:20Z F64: refresh started, request 7ae621a3-84fc-41ae-8f6e-004644607015
2026-11-20T06:45:01Z F64: refresh refreshed (Completed) 
2026-11-20T06:45:01Z F64: monitoring database Monitoring KQL database
2026-11-20T06:46:37Z F64: ExecutionMetrics event found
2026-11-20T06:46:39Z F64: model size in memory right after the refresh: 185.3 MB
```
