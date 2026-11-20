# Harness run 20261120T053608Z-v99k-f55a

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 8b9abd9f-a2e4-4ef6-9b76-aaa9b7141954
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 13,231 MB, Power Query 13,108 MB, duration 16 min, CPU 1,662 s, rows 22,085,043, model 185 MB (Backup step in XMLA trace)
- Refresh request 959f4ccf-fcad-4261-bfa6-d0f7c61c62c6, 2026-11-20T05:38:58.777 to 2026-11-20T05:55:03.087, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99k-no-buffers on PPU data-1m-v1: refreshed, peak 13,038 MB (2026-11-16T23:27:08Z).
  - Peak change: +193 MB (+1.5%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 13,231 MB vs 551 MB (+12,680 MB), Power Query 13,108 MB vs 298 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 198 MB. The refresh may use the SKU maximum minus this: 102,202 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,868 MB: OVER (461%); F16 4,922 MB: OVER (269%); F32 10,042 MB: OVER (132%); F64 25,402 MB: fits (52%); PPU 102,202 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    036d4881-e715-4a7c-9782-be79275ef5ac TabularSequencePoint        949.6     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        938.8    26.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        665.4    26.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        665.1    26.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        273.2     0.0       0
                                           Customer Stats.Customer Stats       TabularRefresh        271.9     2.7       0
                                           Customer Stats.Customer Stats           ExecuteSql        185.1     0.0       0
                                           Customer Stats.Customer Stats              Process         86.6     2.6       0
                                           Customer Stats.Customer Stats             ReadData         85.9     2.1  471482
                                                                    <NA>               Commit         12.7     0.0    <NA>
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          8.2     0.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          7.7     2.0       0
```

## Log

```
2026-11-20T05:38:20Z run 20261120T053608Z-v99k-f55a: variant=v99k-no-buffers data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T05:38:30Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T05:38:35Z PPU: v99k-no-buffers is 036d4881-e715-4a7c-9782-be79275ef5ac, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T05:38:55Z PPU: model size in memory before the refresh: 197.8 MB
2026-11-20T05:38:58Z PPU: trace started (full)
2026-11-20T05:38:58Z PPU: refresh started, request 959f4ccf-fcad-4261-bfa6-d0f7c61c62c6
2026-11-20T05:55:11Z PPU: refresh refreshed (Completed) 
2026-11-20T05:55:42Z PPU: trace captured 488 events: ProgressReportEnd 443, ExecutionMetrics 34, CommandEnd 11
2026-11-20T05:55:43Z PPU: model size in memory right after the refresh: 232.6 MB
```
