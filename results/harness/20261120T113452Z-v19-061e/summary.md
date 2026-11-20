# Harness run 20261120T113452Z-v19-061e

- Task: refresh
- Variant: v19-pq-heavy-10m
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: b1e69601-02b8-401b-b04a-e23bc61201d5
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 762 MB, Power Query 716 MB, duration 0 min, CPU 15 s, rows 219,816, model n/a (no size)
- Refresh request 85c31852-e0d4-47fe-a0db-4f574e52b78a, 2026-11-20T11:35:55.11 to 2026-11-20T11:36:02.067, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v19-pq-heavy-10m on F64 data-1m-v1: failed, peak 23,336 MB (2026-11-20T06:19:48Z).
  - Peak change: -22,574 MB (-96.7%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 762 MB vs 667 MB (+95 MB), Power Query 716 MB vs 592 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: fits (25%); F16 5,120 MB: fits (15%); F32 10,240 MB: fits (7%); F64 25,600 MB: fits (3%); PPU 102,400 MB: fits (1%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
```

Steps running or failed when it stopped:

```
                                         Object  OperationDetailName                        Began Ended EndStatus
           5ac4ec23-e684-402f-a53d-9a6e18c4724f TabularSequencePoint  2026-11-20T11:35:58.435125Z  None          
                PQ Basket Pairs.PQ Basket Pairs       TabularRefresh 2026-11-20T11:35:58.4801663Z  None          
PQ Top Products by Year.PQ Top Products by Year       TabularRefresh 2026-11-20T11:35:58.4860354Z  None          
                PQ Customer RFM.PQ Customer RFM       TabularRefresh 2026-11-20T11:35:58.5017899Z  None          
                PQ Customer RFM.PQ Customer RFM           ExecuteSql 2026-11-20T11:35:58.6591156Z  None          
                PQ Basket Pairs.PQ Basket Pairs           ExecuteSql 2026-11-20T11:35:58.6600077Z  None          
PQ Top Products by Year.PQ Top Products by Year           ExecuteSql 2026-11-20T11:35:58.6631898Z  None          
      PQ Customer Segments.PQ Customer Segments       TabularRefresh 2026-11-20T11:35:59.4110205Z  None          
      PQ Customer Segments.PQ Customer Segments           ExecuteSql 2026-11-20T11:35:59.4364215Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          2.5     0.9      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          1.7     0.9      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          1.6     0.8 104990
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.5     0.1      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          1.3     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          0.8     0.1      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          0.7     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          0.7     0.3      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          0.6     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          0.5     0.3      0
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba          ExecuteSql          0.5     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          0.4     0.3 100450
```

**Screenshot: the refresh error of v19-pq-heavy-10m on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v19-pq-heavy-10m-refresh-error.png**

## Log

```
2026-11-20T11:35:29Z run 20261120T113452Z-v19-061e: variant=v19-pq-heavy-10m data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T11:35:37Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T11:35:40Z F64: v19-pq-heavy-10m is 5ac4ec23-e684-402f-a53d-9a6e18c4724f, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T11:35:55Z F64: model size in memory before the refresh: 0.1 MB
2026-11-20T11:35:55Z F64: refresh started, request 85c31852-e0d4-47fe-a0db-4f574e52b78a
2026-11-20T11:36:05Z F64: refresh failed (Failed) other
2026-11-20T11:36:05Z F64: monitoring database Monitoring KQL database
2026-11-20T11:37:40Z F64: ExecutionMetrics event found
```
