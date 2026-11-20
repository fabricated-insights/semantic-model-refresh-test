# Harness run 20261120T110155Z-v99o-061e

- Task: refresh
- Variant: v99o-sorts
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 774350f1-e1d9-4de1-a23d-b8faef1ae090
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 5,340 MB, Power Query 5,062 MB, duration 3 min, CPU 193 s, rows 21,583,972, model 99 MB (Backup step in SemanticModelLogs)
- Refresh request 8db9675f-e460-469e-8900-a79f617e712f, 2026-11-20T11:03:18.813 to 2026-11-20T11:06:00.327, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99o-sorts on F64 data-1m-v1: refreshed, peak 5,307 MB (2026-11-20T05:28:48Z).
  - Peak change: +33 MB (+0.6%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 5,340 MB vs 716 MB (+4,624 MB), Power Query 5,062 MB vs 527 MB, model 99 MB vs 73 MB.
- Model size in memory when the full refresh started: 99 MB. The refresh may use the SKU maximum minus this: 25,501 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,967 MB: OVER (180%); F16 5,021 MB: OVER (106%); F32 10,141 MB: fits (53%); F64 25,501 MB: fits (21%); PPU 102,301 MB: fits (5%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    de183c23-bc85-4924-a529-71615701050c TabularSequencePoint        156.2     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        145.9    11.4       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         96.5    11.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         96.3    11.3 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql         49.3     0.0       0
                                                  Sales.Sales Line Label       TabularRefresh          3.2     3.1       0
                                                                                       Commit          3.0     0.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          2.9     4.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          2.7     2.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          2.7     0.8       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.6     0.3       0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh          1.6     0.0       0
```

## Log

```
2026-11-20T11:02:48Z run 20261120T110155Z-v99o-061e: variant=v99o-sorts data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T11:03:00Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:03:04Z F64: v99o-sorts is de183c23-bc85-4924-a529-71615701050c, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:03:18Z F64: model size in memory before the refresh: 99.0 MB
2026-11-20T11:03:19Z F64: refresh started, request 8db9675f-e460-469e-8900-a79f617e712f
2026-11-20T11:06:29Z F64: refresh refreshed (Completed) 
2026-11-20T11:06:30Z F64: monitoring database Monitoring KQL database
2026-11-20T11:08:06Z F64: ExecutionMetrics event found
2026-11-20T11:08:27Z F64: model size in memory right after the refresh: 133.8 MB
```
