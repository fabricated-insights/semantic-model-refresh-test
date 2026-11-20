# Harness run 20261120T084327Z-v99a-061e

- Task: refresh
- Variant: v99a-no-big-calc-tables
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 218a0c62-85b0-4602-9045-c3e24981df9f
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 16,022 MB, Power Query 15,940 MB, duration 15 min, CPU 1,561 s, rows 22,085,043, model 185 MB (Backup step in SemanticModelLogs)
- Refresh request 737739fe-b113-49c1-97e9-7b685c14c5ab, 2026-11-20T08:46:17.51 to 2026-11-20T09:01:25.507, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99a-no-big-calc-tables on F64 data-1m-v1: refreshed, peak 16,013 MB (2026-11-20T01:00:52Z).
  - Peak change: +9 MB (+0.1%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 16,022 MB vs 716 MB (+15,306 MB), Power Query 15,940 MB vs 527 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 25,402 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (559%); F16 4,922 MB: OVER (326%); F32 10,042 MB: OVER (160%); F64 25,402 MB: fits (63%); PPU 102,202 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  96009ba6-0e71-4d15-b224-fac22fc40bc5 TabularSequencePoint        897.7     0.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        881.8    12.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        626.7    12.5       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        626.6    12.5 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        254.9     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        189.7     1.5       0
                         Customer Stats.Customer Stats           ExecuteSql        109.9     0.0       0
                         Customer Stats.Customer Stats              Process         79.6     1.4       0
                         Customer Stats.Customer Stats             ReadData         79.3     1.2  471482
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.7     1.1       0
                                Sales.Sales Line Label       TabularRefresh          3.3     3.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          2.8     4.5       0
```

## Log

```
2026-11-20T08:45:41Z run 20261120T084327Z-v99a-061e: variant=v99a-no-big-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T08:45:48Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:45:53Z F64: v99a-no-big-calc-tables is 96009ba6-0e71-4d15-b224-fac22fc40bc5, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:46:17Z F64: model size in memory before the refresh: 197.8 MB
2026-11-20T08:46:17Z F64: refresh started, request 737739fe-b113-49c1-97e9-7b685c14c5ab
2026-11-20T09:01:30Z F64: refresh refreshed (Completed) 
2026-11-20T09:01:30Z F64: monitoring database Monitoring KQL database
2026-11-20T09:03:07Z F64: ExecutionMetrics event found
2026-11-20T09:03:27Z F64: model size in memory right after the refresh: 232.6 MB
```
