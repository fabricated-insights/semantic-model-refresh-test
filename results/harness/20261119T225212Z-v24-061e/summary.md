# Harness run 20261119T225212Z-v24-061e

- Task: refresh
- Variant: v24-bidirectional
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 26518d20-e534-4611-9bdf-a57378a67972
- Refresh parallelism requested: 6

## F64

- Result: **refreshed** 
- Peak 706 MB, Power Query 616 MB, duration 1 min, CPU 99 s, rows 2,561,140, model 73 MB (Backup step in SemanticModelLogs)
- Refresh request c48c0dd5-3049-4ed0-bcd8-2432bc28f033, 2026-11-19T22:53:14.607 to 2026-11-19T22:54:22.923, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v24-bidirectional on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 706 MB vs 615 MB (+91 MB), Power Query 616 MB vs 335 MB, model 73 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (23%); F16 5,120 MB: fits (14%); F32 10,240 MB: fits (7%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Slowest steps:

```
                                                                  Object  OperationDetailName  DurationSec  CpuSec    Rows
                                    6b149a33-ae47-4ec8-8d3a-22bfd227d31b TabularSequencePoint         59.2     0.1       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh         58.5    17.8       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba              Process         56.8    17.7       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             ReadData         56.3    17.6 2349091
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba    AnalyzeEncodeData         10.5    11.9       0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba             VertiPaq         10.3    10.4       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18       TabularRefresh          7.5     0.1       0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18           ExecuteSql          7.3     0.0       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh          4.6     1.8       0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh          3.2     0.7       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process          2.9     1.8       0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData          2.8     1.7  104990
```

## Log

```
2026-11-19T22:52:46Z run 20261119T225212Z-v24-061e: variant=v24-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-19T22:52:57Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:53:00Z F64: v24-bidirectional is 6b149a33-ae47-4ec8-8d3a-22bfd227d31b, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:53:14Z F64: model size in memory before the refresh: 0.0 MB
2026-11-19T22:53:14Z F64: refresh started, request c48c0dd5-3049-4ed0-bcd8-2432bc28f033
2026-11-19T22:54:25Z F64: refresh refreshed (Completed) 
2026-11-19T22:54:25Z F64: monitoring database Monitoring KQL database
2026-11-19T22:56:00Z F64: ExecutionMetrics event found
2026-11-19T22:56:02Z F64: model size in memory right after the refresh: 92.7 MB
```
