# Harness run 20261120T070105Z-v99q-f55a

- Task: refresh
- Variant: v99q-customer-stats
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: b7d2125f-6562-4274-afcb-7b16bc73dbda
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 3,472 MB, Power Query 3,243 MB, duration 3 min, CPU 345 s, rows 22,055,454, model 114 MB (Backup step in XMLA trace)
- Refresh request 92dc6de8-9552-4a14-afc1-911bb8b067dd, 2026-11-20T07:05:31.927 to 2026-11-20T07:08:29.383, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99q-customer-stats on PPU data-1m-v1: refreshed, peak 3,700 MB (2026-11-17T15:43:33Z).
  - Peak change: -228 MB (-6.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 3,472 MB vs 551 MB (+2,921 MB), Power Query 3,243 MB vs 298 MB, model 114 MB vs 73 MB.
- Model size in memory when the full refresh started: 127 MB. The refresh may use the SKU maximum minus this: 102,273 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,939 MB: OVER (118%); F16 4,993 MB: fits (70%); F32 10,113 MB: fits (34%); F64 25,473 MB: fits (14%); PPU 102,273 MB: fits (3%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  a0c7fd43-3720-419e-a1cf-b0e193d83052 TabularSequencePoint        162.9     0.2       0
                         Customer Stats.Customer Stats       TabularRefresh        157.8     2.8       0
                         Customer Stats.Customer Stats           ExecuteSql        135.5     0.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         84.4    26.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         83.0    25.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         82.6    25.7 2349091
                         Customer Stats.Customer Stats              Process         22.1     2.7       0
                         Customer Stats.Customer Stats             ReadData         21.4     2.2  471482
                                                  <NA>               Commit         11.9     0.0    <NA>
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          9.4     3.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          8.5    10.0       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          8.2     8.0       0
```

## Log

```
2026-11-20T07:04:54Z run 20261120T070105Z-v99q-f55a: variant=v99q-customer-stats data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T07:04:59Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T07:05:04Z PPU: v99q-customer-stats is a0c7fd43-3720-419e-a1cf-b0e193d83052, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T07:05:28Z PPU: model size in memory before the refresh: 127.3 MB
2026-11-20T07:05:31Z PPU: trace started (full)
2026-11-20T07:05:32Z PPU: refresh started, request 92dc6de8-9552-4a14-afc1-911bb8b067dd
2026-11-20T07:08:42Z PPU: refresh refreshed (Completed) 
2026-11-20T07:09:13Z PPU: trace captured 451 events: ProgressReportEnd 406, ExecutionMetrics 34, CommandEnd 11
2026-11-20T07:09:14Z PPU: model size in memory right after the refresh: 162.1 MB
```
