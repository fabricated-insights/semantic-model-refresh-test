# Harness run 20261120T080216Z-v21-f55a

- Task: refresh
- Variant: v21-pq-group-by
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 5a06954d-162b-4610-8a90-7b18ac7f13f9
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 3,469 MB, Power Query 3,291 MB, duration 4 min, CPU 350 s, rows 3,032,622, model 85 MB (Backup step in XMLA trace)
- Refresh request 7624b4ed-650c-452e-9c93-e21e54b698a4, 2026-11-20T08:05:10.627 to 2026-11-20T08:08:57.24, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v21-pq-group-by on PPU data-1m-v1: refreshed, peak 3,500 MB (2026-11-19T22:41:51Z).
  - Peak change: -31 MB (-0.9%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 3,469 MB vs 666 MB (+2,803 MB), Power Query 3,291 MB vs 591 MB, model 85 MB vs 73 MB.
- Model size in memory when the full refresh started: 92 MB. The refresh may use the SKU maximum minus this: 102,308 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,974 MB: OVER (117%); F16 5,028 MB: fits (69%); F32 10,148 MB: fits (34%); F64 25,508 MB: fits (14%); PPU 102,308 MB: fits (3%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  b551b92f-7694-4efc-9e6f-4c13eaec6dcf TabularSequencePoint        212.9     0.2       0
                         Customer Stats.Customer Stats       TabularRefresh        209.9     3.5       0
                         Customer Stats.Customer Stats           ExecuteSql        177.2     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        160.8    34.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        152.2    33.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        151.4    33.6 2349091
                         Customer Stats.Customer Stats              Process         32.6     3.5       0
                         Customer Stats.Customer Stats             ReadData         31.9     3.0  471482
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         14.4     3.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         13.3    14.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         12.9    12.5       0
                                                  <NA>               Commit         10.0     0.0    <NA>
```

## Log

```
2026-11-20T08:04:30Z run 20261120T080216Z-v21-f55a: variant=v21-pq-group-by data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T08:04:41Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T08:04:44Z PPU: v21-pq-group-by is b551b92f-7694-4efc-9e6f-4c13eaec6dcf, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T08:05:06Z PPU: model size in memory before the refresh: 92.1 MB
2026-11-20T08:05:10Z PPU: trace started (full)
2026-11-20T08:05:10Z PPU: refresh started, request 7624b4ed-650c-452e-9c93-e21e54b698a4
2026-11-20T08:09:21Z PPU: refresh refreshed (Completed) 
2026-11-20T08:09:52Z PPU: trace captured 286 events: ProgressReportEnd 254, ExecutionMetrics 22, CommandEnd 10
2026-11-20T08:09:53Z PPU: model size in memory right after the refresh: 118.6 MB
```
