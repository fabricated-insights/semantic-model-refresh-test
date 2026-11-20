# Harness run 20261120T090642Z-v30-f55a

- Task: refresh
- Variant: v30-double-instead-of-fixed
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 040f8d7c-2c64-4995-a484-528ae78181b9
- Refresh parallelism requested: 6

## PPU

- Result: **refreshed** 
- Peak 983 MB, Power Query 906 MB, duration 1 min, CPU 129 s, rows 2,561,140, model 73 MB (Backup step in XMLA trace)
- Refresh request 54484a46-95e5-4e42-88b5-a35154688604, 2026-11-20T09:09:58.587 to 2026-11-20T09:11:28.12, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: XMLA trace ExecutionMetrics
- Previous harness run of v30-double-instead-of-fixed on PPU data-1m-v1: refreshed, peak 758 MB (2026-11-19T23:33:22Z).
  - Peak change: +225 MB (+29.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on PPU data-1m-v1 (2026-11-20T07:15:05Z): peak 983 MB vs 666 MB (+317 MB), Power Query 906 MB vs 591 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 102,334 MB on PPU.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,000 MB: fits (33%); F16 5,054 MB: fits (19%); F32 10,174 MB: fits (10%); F64 25,534 MB: fits (4%); PPU 102,334 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    9e47cacd-824d-4e24-8998-6f639088fddf TabularSequencePoint         77.0     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         75.9    24.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         73.4    24.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         72.5    23.8 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         14.6    16.0       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         14.3    14.2       0
                                                                    <NA>               Commit          9.2     0.0    <NA>
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          5.8     1.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          4.3     1.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          4.2     1.7  104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.2     0.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql          2.4     0.0       0
```

## Log

```
2026-11-20T09:09:18Z run 20261120T090642Z-v30-f55a: variant=v30-double-instead-of-fixed data_tag=data-1m-v1 source_type=parquet targets=['PPU'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=f55af17e-471c-424f-bed7-8c7664a20052
2026-11-20T09:09:26Z PPU: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T09:09:29Z PPU: v30-double-instead-of-fixed is 9e47cacd-824d-4e24-8998-6f639088fddf, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:09:54Z PPU: model size in memory before the refresh: 66.4 MB
2026-11-20T09:09:58Z PPU: trace started (full)
2026-11-20T09:09:58Z PPU: refresh started, request 54484a46-95e5-4e42-88b5-a35154688604
2026-11-20T09:11:39Z PPU: refresh refreshed (Completed) 
2026-11-20T09:12:09Z PPU: trace captured 268 events: ProgressReportEnd 236, ExecutionMetrics 22, CommandEnd 10
2026-11-20T09:12:10Z PPU: model size in memory right after the refresh: 92.9 MB
```
