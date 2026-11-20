# Harness run 20261120T040302Z-v99k-061e

- Task: refresh
- Variant: v99k-no-buffers
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 7687a791-dcc7-46f0-a7b3-faa4119c2b20
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 13,034 MB, Power Query 12,915 MB, duration 25 min, CPU 2,741 s, rows 22,085,043, model 185 MB (Backup step in SemanticModelLogs)
- Refresh request 46b6461a-ef4f-46d2-87ce-31a92f4d3968, 2026-11-20T04:06:57.95 to 2026-11-20T04:32:11.55, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99k-no-buffers on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 13,034 MB vs 615 MB (+12,419 MB), Power Query 12,915 MB vs 335 MB, model 185 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (425%); F16 5,120 MB: OVER (255%); F32 10,240 MB: OVER (127%); F64 25,600 MB: fits (51%); PPU 102,400 MB: fits (13%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  15619243-80f2-4103-abfe-ed7d0d628749 TabularSequencePoint       1492.9     0.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh       1480.6    24.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process       1064.8    24.9       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData       1064.5    24.9 2349091
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql        415.7     0.0       0
                         Customer Stats.Customer Stats       TabularRefresh        345.6     2.8       0
                         Customer Stats.Customer Stats           ExecuteSql        224.5     0.0       0
                         Customer Stats.Customer Stats              Process        120.9     2.7       0
                         Customer Stats.Customer Stats             ReadData        120.2     2.2  471482
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          6.8     2.6       0
                                Sales.Sales Line Label       TabularRefresh          6.5     6.1       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          6.3     2.5       0
```

## Log

```
2026-11-20T04:06:19Z run 20261120T040302Z-v99k-061e: variant=v99k-no-buffers data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T04:06:32Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T04:06:35Z F64: v99k-no-buffers is 15619243-80f2-4103-abfe-ed7d0d628749, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T04:06:57Z F64: model size in memory before the refresh: 0.3 MB
2026-11-20T04:06:58Z F64: refresh started, request 46b6461a-ef4f-46d2-87ce-31a92f4d3968
2026-11-20T04:32:15Z F64: refresh refreshed (Completed) 
2026-11-20T04:32:15Z F64: monitoring database Monitoring KQL database
2026-11-20T04:33:51Z F64: ExecutionMetrics event found
2026-11-20T04:33:54Z F64: model size in memory right after the refresh: 232.6 MB
```
