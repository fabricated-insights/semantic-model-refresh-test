# Harness run 20261120T135656Z-v21-f55a

- Task: refresh
- Variant: v21-pq-group-by
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f4c99e9e-6485-4d46-9f5d-cfde196e32de
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 3,478 MB, Power Query 3,305 MB, duration 2 min, CPU 233 s, rows 3,032,622, model 85 MB (Backup step in XMLA trace)
- Refresh request 9109d0cb-f891-4468-a6aa-4ca786aaa9e4, 2026-11-20T13:58:02.767 to 2026-11-20T13:59:59.633, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v21-pq-group-by on PPU data-1m-v1: refreshed, peak 3,469 MB (2026-11-20T08:09:52Z).
  - Peak change: +9 MB (+0.3%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T13:40:11Z): peak 3,478 MB vs 604 MB (+2,874 MB), Power Query 3,305 MB vs 529 MB, model 85 MB vs 73 MB.
- Model size in memory when the full refresh started: 92 MB. The refresh may use the SKU maximum minus this: 102,308 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,974 MB: OVER (117%); F16 5,028 MB: fits (69%); F32 10,148 MB: fits (34%); F64 25,508 MB: fits (14%); PPU 102,308 MB: fits (3%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  b551b92f-7694-4efc-9e6f-4c13eaec6dcf TabularSequencePoint        108.4     0.1       0
                         Customer Stats.Customer Stats       TabularRefresh        105.0     2.6       0
                         Customer Stats.Customer Stats           ExecuteSql         87.0     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         69.1    22.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         67.5    22.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         67.0    22.0 2349091
                         Customer Stats.Customer Stats              Process         17.9     2.6       0
                         Customer Stats.Customer Stats             ReadData         17.4     2.2  471482
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         12.0    13.6       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         11.7    11.7       0
                                                  <NA>               Commit          6.6     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.3     1.9       0
```

## Log

```
2026-11-20T13:57:34Z run 20261120T135656Z-v21-f55a: variant=v21-pq-group-by data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T13:57:39Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T13:57:42Z PPU: v21-pq-group-by is b551b92f-7694-4efc-9e6f-4c13eaec6dcf, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T13:57:59Z PPU: model size in memory before the refresh: 92.1 MB
2026-11-20T13:58:02Z PPU: trace started (full)
2026-11-20T13:58:03Z PPU: refresh started, request 9109d0cb-f891-4468-a6aa-4ca786aaa9e4
2026-11-20T14:00:13Z PPU: refresh refreshed (Completed) 
2026-11-20T14:00:44Z PPU: trace captured 274 events: ProgressReportEnd 254, ExecutionMetrics 10, CommandEnd 10
2026-11-20T14:00:44Z PPU: model size in memory right after the refresh: 118.6 MB
```
