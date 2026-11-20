# Harness run 20261120T120527Z-v23-061e

- Task: refresh
- Variant: v23-dax-calc-tables
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 223fd533-adde-4493-9881-492e7bb78a85
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 1,405 MB, Power Query 1,035 MB, duration 1 min, CPU 91 s, rows 16,549,502, model 182 MB (Backup step in SemanticModelLogs)
- Refresh request d0b7fb84-b0fb-4d17-8343-085729918757, 2026-11-20T12:08:28.827 to 2026-11-20T12:09:21.4, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v23-dax-calc-tables on F64 data-1m-v1: refreshed, peak 1,405 MB (2026-11-20T06:46:38Z).
  - Peak change: +0 MB (+0.0%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 1,405 MB vs 667 MB (+738 MB), Power Query 1,035 MB vs 592 MB, model 182 MB vs 73 MB.
- Model size in memory when the full refresh started: 150 MB. The refresh may use the SKU maximum minus this: 25,450 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,916 MB: fits (48%); F16 4,970 MB: fits (28%); F32 10,090 MB: fits (14%); F64 25,450 MB: fits (6%); PPU 102,250 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            247f4e17-b0ab-46b0-9657-92e852883e58 TabularSequencePoint         44.9     0.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         36.2    13.6       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         35.2    13.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         35.0    13.5 2349091
                           Sales Copy.Sales Copy       TabularRefresh          7.8     6.5       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          6.0     6.6       0
             Product Date Grid.Product Date Grid             VertiPaq          5.9     5.9       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          5.9     5.9       0
                           Sales Copy.Sales Copy              Process          5.5     5.4       0
                           Sales Copy.Sales Copy             ReadData          5.3     5.3 2349091
             Product Date Grid.Product Date Grid              Process          4.8     4.4       0
             Product Date Grid.Product Date Grid       TabularRefresh          4.8     4.5       0
```

## Log

```
2026-11-20T12:07:53Z run 20261120T120527Z-v23-061e: variant=v23-dax-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T12:08:01Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:08:04Z F64: v23-dax-calc-tables is 247f4e17-b0ab-46b0-9657-92e852883e58, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:08:28Z F64: model size in memory before the refresh: 149.9 MB
2026-11-20T12:08:29Z F64: refresh started, request d0b7fb84-b0fb-4d17-8343-085729918757
2026-11-20T12:09:39Z F64: refresh refreshed (Completed) 
2026-11-20T12:09:39Z F64: monitoring database Monitoring KQL database
2026-11-20T12:11:15Z F64: ExecutionMetrics event found
2026-11-20T12:11:17Z F64: model size in memory right after the refresh: 183.9 MB
```
