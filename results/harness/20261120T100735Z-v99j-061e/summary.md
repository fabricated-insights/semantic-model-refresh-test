# Harness run 20261120T100735Z-v99j-061e

- Task: refresh
- Variant: v99j-buffer-stg-customer
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: ff487a91-1b8e-4742-a352-7a27378264dc
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 197 MB, Power Query 167 MB, duration 0 min, CPU 15 s, rows 276,795, model n/a (no size)
- Refresh request 15ef4faa-5586-43e8-869b-a7e5e5a9311e, 2026-11-20T10:08:46.447 to 2026-11-20T10:08:52.54, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99j-buffer-stg-customer on F64 data-1m-v1: refreshed, peak 23,051 MB (2026-11-20T04:02:33Z).
  - Peak change: -22,854 MB (-99.1%). **FLAG: peak changed by more than 1%**
  - **FLAG: result changed from refreshed to failed**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 197 MB vs 716 MB (-519 MB), Power Query 167 MB vs 527 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 661 MB. The refresh may use the SKU maximum minus this: 24,939 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,405 MB: fits (8%); F16 4,459 MB: fits (4%); F32 9,579 MB: fits (2%); F64 24,939 MB: fits (1%); PPU 101,739 MB: fits (0%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                                                        Object      OperationDetailName                        Began Ended EndStatus
                          49b9c9d3-9a88-4664-8d54-995932ee7dc2     TabularSequencePoint 2026-11-20T10:08:49.1172149Z  None          
              Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T10:08:49.3381297Z  None          
                                         Sales Flat.Sales Flat           TabularRefresh 2026-11-20T10:08:49.3538307Z  None          
                                 Customer Stats.Customer Stats           TabularRefresh 2026-11-20T10:08:49.3847168Z  None          
                                 Customer Stats.Customer Stats               ExecuteSql 2026-11-20T10:08:49.4618229Z  None          
              Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T10:08:49.4650094Z  None          
                                         Sales Flat.Sales Flat               ExecuteSql 2026-11-20T10:08:49.4738776Z  None          
        Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           TabularRefresh 2026-11-20T10:08:50.6270531Z  None          
        Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59               ExecuteSql 2026-11-20T10:08:50.6831649Z  None          
                           Product Date Grid.Product Date Grid           TabularRefresh 2026-11-20T10:08:52.2463956Z  None          
                           Product Date Grid.Product Date Grid                  Process 2026-11-20T10:08:52.2523079Z  None          
                           Product Date Grid.Product Date Grid                 ReadData 2026-11-20T10:08:52.2534324Z  None          
                    Model.15d460ac-5121-4fa3-9240-b70400d77763 RelationshipBuildPrepare 2026-11-20T10:08:52.2967176Z  None          
                    Model.55fa90e1-00c5-4666-8bc8-dde516c69228 RelationshipBuildPrepare 2026-11-20T10:08:52.3018976Z  None          
                    Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T10:08:52.3062832Z  None          
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.Quarter           TabularRefresh 2026-11-20T10:08:52.3722561Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          2.9     0.5      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          2.4     0.1      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          2.1     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          1.8     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.3     0.1      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          0.9     0.5 100450
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          0.9     0.5      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          0.8     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b            ReadData          0.4     0.0   4018
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b             Process          0.4     0.1      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          0.3     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          0.3     0.1      0
```

**Screenshot: the refresh error of v99j-buffer-stg-customer on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99j-buffer-stg-customer-refresh-error.png**

## Log

```
2026-11-20T10:08:17Z run 20261120T100735Z-v99j-061e: variant=v99j-buffer-stg-customer data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T10:08:26Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T10:08:28Z F64: v99j-buffer-stg-customer is 49b9c9d3-9a88-4664-8d54-995932ee7dc2, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T10:08:46Z F64: model size in memory before the refresh: 660.7 MB
2026-11-20T10:08:46Z F64: refresh started, request 15ef4faa-5586-43e8-869b-a7e5e5a9311e
2026-11-20T10:08:56Z F64: refresh failed (Failed) other
2026-11-20T10:08:57Z F64: monitoring database Monitoring KQL database
2026-11-20T10:11:34Z F64: ExecutionMetrics event found
```
