# Harness run 20261120T090417Z-v99b-061e

- Task: refresh
- Variant: v99b-one-sales-copy
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 4bdf7e15-78b5-477a-b78e-7d1f194f70b1
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 15,075 MB, Power Query 15,023 MB, duration 1 min, CPU 149 s, rows 216,067, model n/a (no size)
- Refresh request a27d2328-47b9-4339-993d-ba11caff2c20, 2026-11-20T09:07:11.723 to 2026-11-20T09:08:00.51, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99b-one-sales-copy on F64 data-1m-v1: failed, peak 25,582 MB (2026-11-20T01:10:02Z).
  - Peak change: -10,507 MB (-41.1%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 15,075 MB vs 716 MB (+14,359 MB), Power Query 15,023 MB vs 527 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (492%); F16 5,120 MB: OVER (294%); F32 10,240 MB: OVER (147%); F64 25,600 MB: fits (59%); PPU 102,400 MB: fits (15%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
```

Steps running or failed when it stopped:

```
                                          Object      OperationDetailName                        Began Ended EndStatus
            1fe6d06d-415b-469f-9bfa-d9105a1aa0a2     TabularSequencePoint 2026-11-20T09:07:13.0111576Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T09:07:13.0879419Z  None          
                           Sales Flat.Sales Flat           TabularRefresh 2026-11-20T09:07:13.1076364Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T09:07:13.2691014Z  None          
                           Sales Flat.Sales Flat               ExecuteSql 2026-11-20T09:07:13.2775622Z  None          
                   Customer Stats.Customer Stats           TabularRefresh 2026-11-20T09:07:14.3069403Z  None          
                   Customer Stats.Customer Stats               ExecuteSql 2026-11-20T09:07:14.3310543Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T09:07:14.5263877Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          7.3     0.7      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          3.9     0.7      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          3.8     0.7 104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          3.3     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          1.2     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.1     0.3      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          1.1     0.0      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          0.9     0.1      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          0.7     0.0      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          0.7     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          0.4     0.3      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          0.4     0.0      0
```

**Screenshot: the refresh error of v99b-one-sales-copy on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99b-one-sales-copy-refresh-error.png**

## Log

```
2026-11-20T09:06:32Z run 20261120T090417Z-v99b-061e: variant=v99b-one-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T09:06:45Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T09:06:48Z F64: v99b-one-sales-copy is 1fe6d06d-415b-469f-9bfa-d9105a1aa0a2, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:07:11Z F64: model size in memory before the refresh: 0.1 MB
2026-11-20T09:07:11Z F64: refresh started, request a27d2328-47b9-4339-993d-ba11caff2c20
2026-11-20T09:08:22Z F64: refresh failed (Failed) other
2026-11-20T09:08:22Z F64: monitoring database Monitoring KQL database
2026-11-20T09:11:00Z F64: ExecutionMetrics event found
```
