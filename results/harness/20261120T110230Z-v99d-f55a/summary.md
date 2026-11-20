# Harness run 20261120T110230Z-v99d-f55a

- Task: refresh
- Variant: v99d-power-query
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 9d47ee90-b0ed-45e6-8994-f1b67aa89bd4
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 16,009 MB, Power Query 15,893 MB, duration 19 min, CPU 1,988 s, rows 22,085,043, model 185 MB (Backup step in XMLA trace)
- Refresh request a92c01d3-a2c7-4cdf-a136-ae60b6a1052d, 2026-11-20T11:06:56.493 to 2026-11-20T11:26:30.09, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99d-power-query on PPU data-1m-v1: refreshed, peak 16,024 MB (2026-11-20T02:45:31Z).
  - Peak change: -15 MB (-0.1%).
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 16,009 MB vs 666 MB (+15,343 MB), Power Query 15,893 MB vs 591 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 102,202 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (558%); F16 4,922 MB: OVER (325%); F32 10,042 MB: OVER (159%); F64 25,402 MB: fits (63%); PPU 102,202 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  2fb3d992-aae5-40d4-ac2d-710eb2f49931 TabularSequencePoint       1157.8     0.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1124.2    26.4       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        698.7     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        641.5     2.7       0
                         Customer Stats.Customer Stats           ExecuteSql        549.5     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        425.3    26.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        425.0    26.3 2349091
                         Customer Stats.Customer Stats              Process         91.9     2.6       0
                         Customer Stats.Customer Stats             ReadData         91.3     2.1  471482
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh         12.6     3.2       0
                                                  <NA>               Commit         12.4     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process         11.1     3.2       0
```

## Log

```
2026-11-20T11:06:01Z run 20261120T110230Z-v99d-f55a: variant=v99d-power-query data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T11:06:08Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:06:25Z PPU: v99d-power-query is 2fb3d992-aae5-40d4-ac2d-710eb2f49931, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:06:52Z PPU: model size in memory before the refresh: 197.8 MB
2026-11-20T11:06:56Z PPU: trace started (full)
2026-11-20T11:06:56Z PPU: refresh started, request a92c01d3-a2c7-4cdf-a136-ae60b6a1052d
2026-11-20T11:26:40Z PPU: refresh refreshed (Completed) 
2026-11-20T11:27:11Z PPU: trace captured 462 events: ProgressReportEnd 442, ExecutionMetrics 10, CommandEnd 10
2026-11-20T11:27:13Z PPU: model size in memory right after the refresh: 232.6 MB
```
