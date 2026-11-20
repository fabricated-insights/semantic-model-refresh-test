# Harness run 20261119T214957Z-v00-f55a

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 4fb63b10-b506-401f-a875-20f3624783c4
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 551 MB, Power Query 298 MB, duration 1 min, CPU 98 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 0fb83227-9732-4fc0-97af-febce8cbb199, 2026-11-19T21:53:37.113 to 2026-11-19T21:54:43.947, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v00-baseline on PPU data-1m-v1: refreshed, peak 550 MB (2026-11-19T05:58:08Z).
  - Peak change: +1 MB (+0.2%).
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (18%); F16 5,054 MB: fits (11%); F32 10,174 MB: fits (5%); F64 25,534 MB: fits (2%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    0eee6936-1906-41cc-ae01-289b0589e4e1 TabularSequencePoint         58.7     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.0    19.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         55.3    19.3       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         54.9    19.2 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.6    12.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.4    10.2       0
                                                                    <NA>               Commit          4.4     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          3.8     1.6       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.7     1.5       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.6     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.6     1.5  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          1.7     0.5       0
```

## Log

```
2026-11-19T21:52:20Z run 20261119T214957Z-v00-f55a: variant=v00-baseline data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-19T21:52:30Z PPU: update from Git 331791b5ff71d5ca6193d149c439b53eaa125c11 -> eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T21:52:57Z PPU: v00-baseline is 0eee6936-1906-41cc-ae01-289b0589e4e1, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T21:53:32Z PPU: model size in memory before the refresh: 66.2 MB
2026-11-19T21:53:36Z PPU: trace started (full)
2026-11-19T21:53:38Z PPU: refresh started, request 0fb83227-9732-4fc0-97af-febce8cbb199
2026-11-19T21:54:48Z PPU: refresh refreshed (Completed) 
2026-11-19T21:55:23Z PPU: trace captured 256 events: ProgressReportEnd 236, ExecutionMetrics 10, CommandEnd 10
2026-11-19T21:55:24Z PPU: model size in memory right after the refresh: 92.7 MB
```
