# Harness run 20261120T001650Z-v36-f55a

- Task: refresh
- Variant: v36-calc-summary-month-grain
- Data tag: data-10m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ca203a1b-7e22-44d2-bde1-601799171579
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 14,936 MB, Power Query 1,835 MB, duration 12 min, CPU 1,435 s, rows 78,870,826, model 1,826 MB (Backup step in XMLA trace)
- Refresh request d04dd49e-b419-424e-90a1-56b43eaa2f77, 2026-11-20T00:20:17.707 to 2026-11-20T00:33:04.123, workspace at eb585e4, DataTag read back data-10m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v36-calc-summary-month-grain on PPU data-10m-v1: refreshed, peak 14,929 MB (2026-11-17T10:41:08Z).
  - Peak change: +7 MB (+0.0%).
- Against v00-baseline on PPU data-10m-v1 (2026-11-18T11:14:13Z): peak 14,936 MB vs 1,834 MB (+13,102 MB), Power Query 1,835 MB vs 1,713 MB, model 1,826 MB vs 778 MB.
- Model size in memory when the full refresh started: 1,322 MB. The refresh may use the SKU maximum minus this: 101,078 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 1,744 MB: OVER (856%); F16 3,798 MB: OVER (393%); F32 8,918 MB: OVER (167%); F64 24,278 MB: fits (62%); PPU 101,078 MB: fits (15%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec     Rows
                  12b658b6-453c-4047-85fa-3e02aebcdc2e TabularSequencePoint        725.3     1.8        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        546.6   181.5        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        538.0   181.5        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        534.5   181.5 23719935
                                 Sales Copy.Sales Copy       TabularRefresh        162.7   120.0        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData        154.8   168.1        0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq        153.1   153.0        0
                                 Sales Copy.Sales Copy              Process        112.5    98.2        0
                           Sales Summary.Sales Summary       TabularRefresh        110.9    71.2        0
                                 Sales Copy.Sales Copy             ReadData         98.4    98.1 23719935
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         49.1    26.0        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         44.8    26.0        0
```

## Log

```
2026-11-20T00:19:21Z run 20261120T001650Z-v36-f55a: variant=v36-calc-summary-month-grain data_tag=data-10m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T00:19:31Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T00:19:51Z PPU: v36-calc-summary-month-grain is 12b658b6-453c-4047-85fa-3e02aebcdc2e, DataTag reads back data-10m-v1, SourceType parquet
2026-11-20T00:20:14Z PPU: model size in memory before the refresh: 1321.5 MB
2026-11-20T00:20:17Z PPU: trace started (full)
2026-11-20T00:20:17Z PPU: refresh started, request d04dd49e-b419-424e-90a1-56b43eaa2f77
2026-11-20T00:33:30Z PPU: refresh refreshed (Completed) 
2026-11-20T00:34:01Z PPU: trace captured 1405 events: ProgressReportEnd 1360, ExecutionMetrics 34, CommandEnd 11
2026-11-20T00:34:02Z PPU: model size in memory right after the refresh: 1407.0 MB
```
