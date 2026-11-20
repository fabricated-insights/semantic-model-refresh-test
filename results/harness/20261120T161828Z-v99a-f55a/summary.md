# Harness run 20261120T161828Z-v99a-f55a

- Task: refresh
- Variant: v99a-no-big-calc-tables
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 4ae3dc5c-38ac-4319-97cc-70da3ca436aa
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 16,020 MB, Power Query 15,897 MB, duration 27 min, CPU 2,941 s, rows 22,085,043, model 185 MB (Backup step in XMLA trace)
- Refresh request 105bee65-6452-45c0-90e8-155435a16f16, 2026-11-20T16:21:19.743 to 2026-11-20T16:48:16.34, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99a-no-big-calc-tables on PPU data-1m-v1: refreshed, peak 16,162 MB (2026-11-20T10:52:28Z).
  - Peak change: -142 MB (-0.9%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 16,020 MB vs 604 MB (+15,416 MB), Power Query 15,897 MB vs 529 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 102,202 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (559%); F16 4,922 MB: OVER (325%); F32 10,042 MB: OVER (160%); F64 25,402 MB: fits (63%); PPU 102,202 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  948a9aac-0241-4366-b5de-ce4224c7bc48 TabularSequencePoint       1600.9     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1574.5    27.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process       1163.4    27.8       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData       1163.1    27.8 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        411.0     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        355.7     3.0       0
                         Customer Stats.Customer Stats           ExecuteSql        208.2     0.0       0
                         Customer Stats.Customer Stats              Process        147.3     3.0       0
                         Customer Stats.Customer Stats             ReadData        146.7     2.5  471482
                                                  <NA>               Commit         12.3     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.9     2.3       0
                                Sales.Sales Line Label       TabularRefresh          6.3     6.0       0
```

## Log

```
2026-11-20T16:20:42Z run 20261120T161828Z-v99a-f55a: variant=v99a-no-big-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T16:20:49Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T16:20:53Z PPU: v99a-no-big-calc-tables is 948a9aac-0241-4366-b5de-ce4224c7bc48, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T16:21:16Z PPU: model size in memory before the refresh: 197.8 MB
2026-11-20T16:21:19Z PPU: trace started (full)
2026-11-20T16:21:19Z PPU: refresh started, request 105bee65-6452-45c0-90e8-155435a16f16
2026-11-20T16:48:34Z PPU: refresh refreshed (Completed) 
2026-11-20T16:49:04Z PPU: trace captured 463 events: ProgressReportEnd 442, ExecutionMetrics 11, CommandEnd 10
2026-11-20T16:49:06Z PPU: model size in memory right after the refresh: 232.6 MB
```
