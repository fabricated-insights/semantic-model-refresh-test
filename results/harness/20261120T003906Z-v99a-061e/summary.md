# Harness run 20261120T003906Z-v99a-061e

- Task: refresh
- Variant: v99a-no-big-calc-tables
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6d0b0032-1f63-417e-92b9-7a1e28ab955e
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 16,013 MB, Power Query 15,914 MB, duration 16 min, CPU 1,643 s, rows 22,085,043, model 185 MB (Backup step in SemanticModelLogs)
- Refresh request d3fc933f-d12f-4f9f-80d0-a1815354862c, 2026-11-20T00:42:01.683 to 2026-11-20T00:58:10.937, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99a-no-big-calc-tables on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 16,013 MB vs 615 MB (+15,398 MB), Power Query 15,914 MB vs 335 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (522%); F16 5,120 MB: OVER (313%); F32 10,240 MB: OVER (156%); F64 25,600 MB: fits (63%); PPU 102,400 MB: fits (16%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                          Object  OperationDetailName  DurationSec  CpuSec    Rows
            96009ba6-0e71-4d15-b224-fac22fc40bc5 TabularSequencePoint        955.4     0.2       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        943.2    23.6       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        657.7    23.6       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        657.4    23.6 2349091
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        285.3     0.0       0
                   Customer Stats.Customer Stats       TabularRefresh        236.9     2.6       0
                   Customer Stats.Customer Stats           ExecuteSql        168.0     0.0       0
                   Customer Stats.Customer Stats              Process         68.8     2.6       0
                   Customer Stats.Customer Stats             ReadData         68.3     2.2  471482
  Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          9.2     0.1       0
  Date.Date-44d762f0-a871-4687-b253-096276d9658b           ExecuteSql          8.8     0.0       0
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          5.7     7.7       0
```

## Log

```
2026-11-20T00:41:23Z run 20261120T003906Z-v99a-061e: variant=v99a-no-big-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T00:41:36Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T00:41:39Z F64: v99a-no-big-calc-tables is 96009ba6-0e71-4d15-b224-fac22fc40bc5, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:42:01Z F64: model size in memory before the refresh: 0.3 MB
2026-11-20T00:42:01Z F64: refresh started, request d3fc933f-d12f-4f9f-80d0-a1815354862c
2026-11-20T00:58:14Z F64: refresh refreshed (Completed) 
2026-11-20T00:58:14Z F64: monitoring database Monitoring KQL database
2026-11-20T01:00:51Z F64: ExecutionMetrics event found
2026-11-20T01:00:54Z F64: model size in memory right after the refresh: 232.6 MB
```
