# Harness run 20261120T152610Z-v99j-061e

- Task: refresh
- Variant: v99j-buffer-stg-customer
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: da2eb662-77c5-4736-8513-5705a83b4766
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 503 MB, Power Query 439 MB, duration 0 min, CPU 11 s, rows 1,002,299, model n/a (no size)
- Refresh request 4e9f91fc-8c03-4574-ae15-da3ee39a52b0, 2026-11-20T15:28:57.937 to 2026-11-20T15:29:04.083, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99j-buffer-stg-customer on F64 data-1m-v1: failed, peak 197 MB (2026-11-20T10:11:36Z).
  - Peak change: +306 MB (+155.3%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 503 MB vs 667 MB (-164 MB), Power Query 439 MB vs 592 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 661 MB. The refresh may use the SKU maximum minus this: 24,939 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,405 MB: fits (21%); F16 4,459 MB: fits (11%); F32 9,579 MB: fits (5%); F64 24,939 MB: fits (2%); PPU 101,739 MB: fits (0%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                  49b9c9d3-9a88-4664-8d54-995932ee7dc2 TabularSequencePoint  2026-11-20T15:29:01.605967Z  None          
                         Customer Stats.Customer Stats       TabularRefresh 2026-11-20T15:29:01.7860778Z  None          
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh 2026-11-20T15:29:01.8258034Z  None          
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh  2026-11-20T15:29:01.863426Z  None          
                         Customer Stats.Customer Stats           ExecuteSql 2026-11-20T15:29:01.9479298Z  None          
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           ExecuteSql 2026-11-20T15:29:01.9484449Z  None          
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql 2026-11-20T15:29:01.9511055Z  None          
                                 Sales Flat.Sales Flat       TabularRefresh 2026-11-20T15:29:02.8412337Z  None          
                                 Sales Flat.Sales Flat           ExecuteSql 2026-11-20T15:29:02.8932555Z  None          
                   Product Date Grid.Product Date Grid       TabularRefresh 2026-11-20T15:29:03.1742141Z  None          
                   Product Date Grid.Product Date Grid              Process 2026-11-20T15:29:03.1792965Z  None          
                   Product Date Grid.Product Date Grid             ReadData  2026-11-20T15:29:03.180642Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.1     0.1      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.1     0.5      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          0.9     0.1      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          0.8     0.1      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          0.8     0.5 100450
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          0.8     0.5      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          0.7     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          0.7     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          0.6     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b            ReadData          0.3     0.1   4018
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b             Process          0.3     0.1      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          0.3     0.0      0
```

**Screenshot: the refresh error of v99j-buffer-stg-customer on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99j-buffer-stg-customer-refresh-error.png**

## Log

```
2026-11-20T15:28:26Z run 20261120T152610Z-v99j-061e: variant=v99j-buffer-stg-customer data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T15:28:34Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T15:28:35Z F64: v99j-buffer-stg-customer is 49b9c9d3-9a88-4664-8d54-995932ee7dc2, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T15:28:57Z F64: model size in memory before the refresh: 660.7 MB
2026-11-20T15:28:58Z F64: refresh started, request 4e9f91fc-8c03-4574-ae15-da3ee39a52b0
2026-11-20T15:29:08Z F64: refresh failed (Failed) other
2026-11-20T15:29:08Z F64: monitoring database Monitoring KQL database
2026-11-20T15:31:45Z F64: ExecutionMetrics event found
```
