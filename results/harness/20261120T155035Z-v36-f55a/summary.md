# Harness run 20261120T155035Z-v36-f55a

- Task: refresh
- Variant: v36-calc-summary-month-grain
- Data tag: data-10m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: af972181-59d0-4667-ae5c-4185527d20aa
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 14,931 MB, Power Query 1,651 MB, duration 19 min, CPU 1,867 s, rows 78,870,826, model 1,820 MB (Backup step in XMLA trace)
- Refresh request 6d25ae0d-923a-47b8-a065-c3f4c7375d9b, 2026-11-20T15:52:43.347 to 2026-11-20T16:13:16.957, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v36-calc-summary-month-grain on PPU data-10m-v1: refreshed, peak 14,935 MB (2026-11-20T10:26:54Z).
  - Peak change: -4 MB (-0.0%).
- Against v00-baseline on PPU data-10m-v1 (2026-11-18T11:14:13Z): peak 14,931 MB vs 1,834 MB (+13,097 MB), Power Query 1,651 MB vs 1,713 MB, model 1,820 MB vs 778 MB.
- Model size in memory when the full refresh started: 1,322 MB. The refresh may use the SKU maximum minus this: 101,078 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 1,744 MB: OVER (856%); F16 3,798 MB: OVER (393%); F32 8,918 MB: OVER (167%); F64 24,278 MB: fits (61%); PPU 101,078 MB: fits (15%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  12b658b6-453c-4047-85fa-3e02aebcdc2e TabularSequencePoint       1116.9     0.2        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        767.0   251.2        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        758.4   251.2        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        754.1   251.1 23719935
                                 Sales Copy.Sales Copy       TabularRefresh        327.3   192.3        0
                                 Sales Copy.Sales Copy              Process        259.9   163.8        0
                                 Sales Copy.Sales Copy             ReadData        228.1   163.7 23719935
                           Sales Summary.Sales Summary       TabularRefresh        168.4   101.1        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData        152.0   164.0        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq        149.9   148.6        0
                                                  <NA>               Commit        113.5     0.0     <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         62.0    33.2        0
```

## Log

```
2026-11-20T15:51:53Z run 20261120T155035Z-v36-f55a: variant=v36-calc-summary-month-grain data_tag=data-10m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T15:52:03Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T15:52:22Z PPU: v36-calc-summary-month-grain is 12b658b6-453c-4047-85fa-3e02aebcdc2e, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T15:52:39Z PPU: model size in memory before the refresh: 1321.9 MB
2026-11-20T15:52:43Z PPU: trace started (full)
2026-11-20T15:52:43Z PPU: refresh started, request 6d25ae0d-923a-47b8-a065-c3f4c7375d9b
2026-11-20T16:13:27Z PPU: refresh refreshed (Completed) 
2026-11-20T16:13:58Z PPU: trace captured 1380 events: ProgressReportEnd 1359, ExecutionMetrics 11, CommandEnd 10
2026-11-20T16:13:59Z PPU: model size in memory right after the refresh: 1400.8 MB
```
