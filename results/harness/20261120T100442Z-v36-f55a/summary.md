# Harness run 20261120T100442Z-v36-f55a

- Task: refresh
- Variant: v36-calc-summary-month-grain
- Data tag: data-10m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3021f7c1-32b0-403f-869e-23df077c64b3
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 14,935 MB, Power Query 1,952 MB, duration 17 min, CPU 1,733 s, rows 78,870,826, model 1,826 MB (Backup step in XMLA trace)
- Refresh request ff958005-df8c-40dd-9647-bed7beaccfa4, 2026-11-20T10:08:39.04 to 2026-11-20T10:26:19.37, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v36-calc-summary-month-grain on PPU data-10m-v1: refreshed, peak 14,936 MB (2026-11-20T00:34:01Z).
  - Peak change: -1 MB (-0.0%).
- Against v00-baseline on PPU data-10m-v1 (2026-11-18T11:14:13Z): peak 14,935 MB vs 1,834 MB (+13,101 MB), Power Query 1,952 MB vs 1,713 MB, model 1,826 MB vs 778 MB.
- Model size in memory when the full refresh started: 1,322 MB. The refresh may use the SKU maximum minus this: 101,078 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 1,744 MB: OVER (856%); F16 3,798 MB: OVER (393%); F32 8,918 MB: OVER (167%); F64 24,278 MB: fits (62%); PPU 101,078 MB: fits (15%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  12b658b6-453c-4047-85fa-3e02aebcdc2e TabularSequencePoint       1019.4     1.9        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        839.1   241.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        813.6   241.7        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        811.6   241.7 23719935
                                 Sales Copy.Sales Copy       TabularRefresh        164.2   119.0        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh        146.6    52.1        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData        137.0   145.2        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process        136.6    52.0        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq        134.5   131.6        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData        131.0    51.3  1679846
                                 Sales Copy.Sales Copy              Process        112.6    97.5        0
                           Sales Summary.Sales Summary       TabularRefresh        112.0    69.7        0
```

## Log

```
2026-11-20T10:07:20Z run 20261120T100442Z-v36-f55a: variant=v36-calc-summary-month-grain data_tag=data-10m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T10:07:30Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T10:08:05Z PPU: v36-calc-summary-month-grain is 12b658b6-453c-4047-85fa-3e02aebcdc2e, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T10:08:35Z PPU: model size in memory before the refresh: 1322.1 MB
2026-11-20T10:08:38Z PPU: trace started (full)
2026-11-20T10:08:39Z PPU: refresh started, request ff958005-df8c-40dd-9647-bed7beaccfa4
2026-11-20T10:26:22Z PPU: refresh refreshed (Completed) 
2026-11-20T10:26:53Z PPU: trace captured 1391 events: ProgressReportEnd 1359, ExecutionMetrics 22, CommandEnd 10
2026-11-20T10:26:55Z PPU: model size in memory right after the refresh: 1406.8 MB
```
