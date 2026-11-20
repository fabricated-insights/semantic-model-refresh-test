# Harness run 20261120T094129Z-v99e-061e

- Task: refresh
- Variant: v99e-sales-flat
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 6157259e-ad92-4ddc-96ff-00d56b946253
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 728 MB, Power Query 704 MB, duration 0 min, CPU 7 s, rows 189,729, model n/a (no size)
- Refresh request 30b3ce55-a7d9-4d7a-86ec-fdc6854e180a, 2026-11-20T09:42:42.227 to 2026-11-20T09:42:47.517, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99e-sales-flat on F64 data-1m-v1: refreshed, peak 22,822 MB (2026-11-20T02:04:28Z).
  - Peak change: -22,094 MB (-96.8%). **FLAG: peak changed by more than 1%**
  - **FLAG: result changed from refreshed to failed**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 728 MB vs 716 MB (+12 MB), Power Query 704 MB vs 527 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 357 MB. The refresh may use the SKU maximum minus this: 25,243 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,709 MB: fits (27%); F16 4,763 MB: fits (15%); F32 9,883 MB: fits (7%); F64 25,243 MB: fits (3%); PPU 102,043 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                  b8cd0fd3-0d59-484f-8fea-ac343761db7b     TabularSequencePoint 2026-11-20T09:42:44.5115788Z  None          
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           TabularRefresh  2026-11-20T09:42:44.684737Z  None          
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T09:42:44.7013683Z  None          
                         Customer Stats.Customer Stats           TabularRefresh  2026-11-20T09:42:44.731725Z  None          
                         Customer Stats.Customer Stats               ExecuteSql 2026-11-20T09:42:44.8340533Z  None          
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T09:42:44.8393421Z  None          
                                 Sales Flat.Sales Flat           TabularRefresh 2026-11-20T09:42:46.1577101Z  None          
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59                  Process 2026-11-20T09:42:46.1874783Z  None          
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59                 ReadData 2026-11-20T09:42:46.1895855Z  None          
                                 Sales Flat.Sales Flat               ExecuteSql 2026-11-20T09:42:46.2118023Z  None          
            Model.15d460ac-5121-4fa3-9240-b70400d77763 RelationshipBuildPrepare 2026-11-20T09:42:46.3668774Z  None          
            Model.55fa90e1-00c5-4666-8bc8-dde516c69228 RelationshipBuildPrepare 2026-11-20T09:42:46.3718042Z  None          
            Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T09:42:46.7969556Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          2.1     0.5      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          1.4     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.3     0.1      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          1.2     0.0      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.1     0.1      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          1.0     0.0      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          0.9     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          0.7     0.5      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          0.6     0.5 100450
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b            ReadData          0.3     0.1   4018
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          0.3     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          0.3     0.0      0
```

**Screenshot: the refresh error of v99e-sales-flat on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99e-sales-flat-refresh-error.png**

## Log

```
2026-11-20T09:42:06Z run 20261120T094129Z-v99e-061e: variant=v99e-sales-flat data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T09:42:17Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T09:42:26Z F64: v99e-sales-flat is b8cd0fd3-0d59-484f-8fea-ac343761db7b, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:42:42Z F64: model size in memory before the refresh: 356.6 MB
2026-11-20T09:42:42Z F64: refresh started, request 30b3ce55-a7d9-4d7a-86ec-fdc6854e180a
2026-11-20T09:42:52Z F64: refresh failed (Failed) other
2026-11-20T09:42:52Z F64: monitoring database Monitoring KQL database
2026-11-20T09:45:29Z F64: ExecutionMetrics event found
```
