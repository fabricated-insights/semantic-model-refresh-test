# Harness run 20261120T062952Z-v99n-f55a

- Task: refresh
- Variant: v99n-text-staging
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 72532c70-7294-4655-907d-b1746a0796dc
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 668 MB, Power Query 566 MB, duration 10 min, CPU 621 s, rows 21,587,990, model 92 MB (Backup step in XMLA trace)
- Refresh request 52c6f343-d46e-4b0e-8220-686de145f6e9, 2026-11-20T06:32:56.347 to 2026-11-20T06:43:07.833, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v99n-text-staging on PPU data-1m-v1: refreshed, peak 905 MB (2026-11-17T14:55:22Z).
  - Peak change: -237 MB (-26.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-19T21:55:23Z): peak 668 MB vs 551 MB (+117 MB), Power Query 566 MB vs 298 MB, model 92 MB vs 73 MB.
- Model size in memory when the full refresh started: 91 MB. The refresh may use the SKU maximum minus this: 102,309 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,975 MB: fits (22%); F16 5,029 MB: fits (13%); F32 10,149 MB: fits (7%); F64 25,509 MB: fits (3%); PPU 102,309 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                Object  OperationDetailName  DurationSec  CpuSec    Rows
                  b50ca483-f3ad-48d4-bf77-74585e534ddb TabularSequencePoint        599.0     0.2       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh        588.7    35.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process        586.4    35.1       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData        585.8    34.8 2349091
                                                  <NA>               Commit          9.0     0.0    <NA>
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData          7.8     9.3       0
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq          7.5     7.4       0
                                Sales.Sales Line Label       TabularRefresh          6.7     6.5       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.9     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.5     2.0       0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.4     1.9  104990
                                   Sales.Customer Name       TabularRefresh          3.5     2.7       0
```

## Log

```
2026-11-20T06:32:19Z run 20261120T062952Z-v99n-f55a: variant=v99n-text-staging data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T06:32:27Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T06:32:31Z PPU: v99n-text-staging is b50ca483-f3ad-48d4-bf77-74585e534ddb, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T06:32:52Z PPU: model size in memory before the refresh: 90.7 MB
2026-11-20T06:32:56Z PPU: trace started (full)
2026-11-20T06:32:56Z PPU: refresh started, request 52c6f343-d46e-4b0e-8220-686de145f6e9
2026-11-20T06:43:08Z PPU: refresh refreshed (Completed) 
2026-11-20T06:43:38Z PPU: trace captured 434 events: ProgressReportEnd 389, ExecutionMetrics 34, CommandEnd 11
2026-11-20T06:43:40Z PPU: model size in memory right after the refresh: 124.3 MB
```
