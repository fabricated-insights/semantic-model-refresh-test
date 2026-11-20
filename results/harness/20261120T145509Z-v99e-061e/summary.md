# Harness run 20261120T145509Z-v99e-061e

- Task: refresh
- Variant: v99e-sales-flat
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 2d9222d0-2ec7-46a2-96e5-9f7d12f5386f
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 290 MB, Power Query 252 MB, duration 0 min, CPU 6 s, rows 25,598, model n/a (no size)
- Refresh request 3330082a-cc2b-401f-9176-bc7000647194, 2026-11-20T14:57:59.42 to 2026-11-20T14:58:04.387, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99e-sales-flat on F64 data-1m-v1: failed, peak 728 MB (2026-11-20T09:45:32Z).
  - Peak change: -438 MB (-60.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 290 MB vs 667 MB (-377 MB), Power Query 252 MB vs 592 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 357 MB. The refresh may use the SKU maximum minus this: 25,243 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,709 MB: fits (11%); F16 4,763 MB: fits (6%); F32 9,883 MB: fits (3%); F64 25,243 MB: fits (1%); PPU 102,043 MB: fits (0%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
```

Steps running or failed when it stopped:

```
                                                                  Object  OperationDetailName                        Began Ended EndStatus
                                    b8cd0fd3-0d59-484f-8fea-ac343761db7b TabularSequencePoint 2026-11-20T14:58:02.3495173Z  None          
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh 2026-11-20T14:58:02.4417999Z  None          
                                                   Sales Flat.Sales Flat       TabularRefresh 2026-11-20T14:58:02.4652509Z  None          
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh 2026-11-20T14:58:02.4817216Z  None          
                                           Customer Stats.Customer Stats       TabularRefresh 2026-11-20T14:58:02.4968796Z  None          
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be           ExecuteSql 2026-11-20T14:58:02.5757178Z  None          
                                           Customer Stats.Customer Stats           ExecuteSql 2026-11-20T14:58:02.5783246Z  None          
                                                   Sales Flat.Sales Flat           ExecuteSql 2026-11-20T14:58:02.5851461Z  None          
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh 2026-11-20T14:58:03.6366271Z  None          
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql 2026-11-20T14:58:03.6645639Z  None          
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process 2026-11-20T14:58:03.7411498Z  None          
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData 2026-11-20T14:58:03.7423032Z  None          
                                                              Store.Name       TabularRefresh 2026-11-20T14:58:04.2792204Z  None          
```

Slowest steps:

```
                                                                                                       Object OperationDetailName  DurationSec  CpuSec  Rows
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.3     0.1     0
                                                             Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          1.2     0.0     0
                                                       Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          1.2     0.0     0
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          1.1     0.0     0
                                                             Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          1.0     0.0     0
                                                               Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          0.4     0.1     0
                                                               Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          0.2     0.0     0
                                                               Date.Date-44d762f0-a871-4687-b253-096276d9658b            ReadData          0.2     0.1  4018
                                                               Date.Date-44d762f0-a871-4687-b253-096276d9658b             Process          0.2     0.1     0
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18            ReadData          0.1     0.0  2517
                                                         Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18             Process          0.1     0.0     0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f      TabularRefresh          0.0     0.0     0
```

**Screenshot: the refresh error of v99e-sales-flat on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99e-sales-flat-refresh-error.png**

## Log

```
2026-11-20T14:57:20Z run 20261120T145509Z-v99e-061e: variant=v99e-sales-flat data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T14:57:32Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:57:37Z F64: v99e-sales-flat is b8cd0fd3-0d59-484f-8fea-ac343761db7b, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:57:59Z F64: model size in memory before the refresh: 356.6 MB
2026-11-20T14:57:59Z F64: refresh started, request 3330082a-cc2b-401f-9176-bc7000647194
2026-11-20T14:58:09Z F64: refresh failed (Failed) other
2026-11-20T14:58:09Z F64: monitoring database Monitoring KQL database
2026-11-20T15:00:46Z F64: ExecutionMetrics event found
```
