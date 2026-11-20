# Harness run 20261120T122516Z-v99l-f55a

- Task: refresh
- Variant: v99l-no-calc-columns
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 56d4944a-5d56-4638-a00f-f4dbdc7c091f
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 12,855 MB, Power Query 12,741 MB, duration 17 min, CPU 1,874 s, rows 3,292,315, model 158 MB (Backup step in XMLA trace)
- Refresh request 941fbdc2-91b6-4329-922f-ff4e4aa8cc6b, 2026-11-20T12:27:57.293 to 2026-11-20T12:45:36.677, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99l-no-calc-columns on PPU data-1m-v1: refreshed, peak 12,995 MB (2026-11-20T06:22:48Z).
  - Peak change: -140 MB (-1.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 12,855 MB vs 666 MB (+12,189 MB), Power Query 12,741 MB vs 591 MB, model 158 MB vs 73 MB.
- Model size in memory when the full refresh started: 168 MB. The refresh may use the SKU maximum minus this: 102,232 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,898 MB: OVER (444%); F16 4,952 MB: OVER (260%); F32 10,072 MB: OVER (128%); F64 25,432 MB: fits (51%); PPU 102,232 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  bd05e14c-0c16-4a5f-9ea0-0eac63361a0c TabularSequencePoint       1042.6     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1032.4    27.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        678.6    27.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        678.2    27.1 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        353.7     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        300.8     3.2       0
                         Customer Stats.Customer Stats           ExecuteSql        162.2     0.0       0
                         Customer Stats.Customer Stats              Process        138.5     3.2       0
                         Customer Stats.Customer Stats             ReadData        137.7     2.6  471482
                                                  <NA>               Commit         12.7     0.0    <NA>
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.6     9.3       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.6     2.0       0
```

## Log

```
2026-11-20T12:27:19Z run 20261120T122516Z-v99l-f55a: variant=v99l-no-calc-columns data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T12:27:28Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T12:27:32Z PPU: v99l-no-calc-columns is bd05e14c-0c16-4a5f-9ea0-0eac63361a0c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T12:27:53Z PPU: model size in memory before the refresh: 167.7 MB
2026-11-20T12:27:57Z PPU: trace started (full)
2026-11-20T12:27:57Z PPU: refresh started, request 941fbdc2-91b6-4329-922f-ff4e4aa8cc6b
2026-11-20T12:45:40Z PPU: refresh refreshed (Completed) 
2026-11-20T12:46:11Z PPU: trace captured 422 events: ProgressReportEnd 402, ExecutionMetrics 10, CommandEnd 10
2026-11-20T12:46:13Z PPU: model size in memory right after the refresh: 194.2 MB
```
