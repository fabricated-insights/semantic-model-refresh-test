# Harness run 20261119T234142Z-v33-f55a

- Task: refresh
- Variant: v33-auto-date-time
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 42231623-cb8b-476e-97a3-377a7aa8ae4b
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 554 MB, Power Query 456 MB, duration 1 min, CPU 108 s, rows 2,791,244, model 74 MB (Backup step in XMLA trace)
- Refresh request 1c1ffefd-80eb-4c55-ae82-a6a4e70a41fc, 2026-11-19T23:44:17.367 to 2026-11-19T23:45:28.71, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v33-auto-date-time on PPU data-1m-v1: refreshed, peak 1,952 MB (2026-11-17T14:39:51Z).
  - Peak change: -1,398 MB (-71.6%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 554 MB vs 551 MB (+3 MB), Power Query 456 MB vs 298 MB, model 74 MB vs 73 MB.
- Model size in memory when the full refresh started: 70 MB. The refresh may use the SKU maximum minus this: 102,330 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,996 MB: fits (18%); F16 5,050 MB: fits (11%); F32 10,170 MB: fits (5%); F64 25,530 MB: fits (2%); PPU 102,330 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    fbb53e0d-05a8-434a-9ad9-ec2dac2730d7 TabularSequencePoint         63.5     0.2       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         62.6    19.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         59.6    18.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         59.1    18.8 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.6    11.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.5    10.4       0
                                                                    <NA>               Commit          5.5     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.3     1.7       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.3     0.6       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.9     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.8     1.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.6     1.6  104990
```

## Log

```
2026-11-19T23:43:45Z run 20261119T234142Z-v33-f55a: variant=v33-auto-date-time data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T23:43:50Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T23:43:55Z PPU: v33-auto-date-time is fbb53e0d-05a8-434a-9ad9-ec2dac2730d7, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T23:44:13Z PPU: model size in memory before the refresh: 69.7 MB
2026-11-19T23:44:17Z PPU: trace started (full)
2026-11-19T23:44:17Z PPU: refresh started, request 1c1ffefd-80eb-4c55-ae82-a6a4e70a41fc
2026-11-19T23:45:57Z PPU: refresh refreshed (Completed) 
2026-11-19T23:46:28Z PPU: trace captured 393 events: ProgressReportEnd 348, ExecutionMetrics 34, CommandEnd 11
2026-11-19T23:46:29Z PPU: model size in memory right after the refresh: 96.2 MB
```
