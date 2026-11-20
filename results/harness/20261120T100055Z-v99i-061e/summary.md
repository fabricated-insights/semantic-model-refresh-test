# Harness run 20261120T100055Z-v99i-061e

- Task: refresh
- Variant: v99i-buffer-stg-sales
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 94dc589b-4fd3-46bb-9a2d-431a1a2d49bb
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 14,948 MB, Power Query 14,864 MB, duration 1 min, CPU 153 s, rows 10,559,477, model n/a (no size)
- Refresh request ad124055-f199-488a-84d2-09abf6fcb1b0, 2026-11-20T10:04:09.92 to 2026-11-20T10:04:56.44, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99i-buffer-stg-sales on F64 data-1m-v1: failed, peak 25,521 MB (2026-11-20T03:46:03Z).
  - Peak change: -10,573 MB (-41.4%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 14,948 MB vs 716 MB (+14,232 MB), Power Query 14,864 MB vs 527 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (488%); F16 5,120 MB: OVER (292%); F32 10,240 MB: OVER (146%); F64 25,600 MB: fits (58%); PPU 102,400 MB: fits (15%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
            fe4b7ed4-bbdc-48ba-aa51-e9eae49eb056     TabularSequencePoint 2026-11-20T10:04:12.3504262Z  None          
                   Customer Stats.Customer Stats           TabularRefresh 2026-11-20T10:04:12.4638333Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T10:04:12.4799196Z  None          
                           Sales Flat.Sales Flat           TabularRefresh 2026-11-20T10:04:12.5142822Z  None          
                   Customer Stats.Customer Stats               ExecuteSql 2026-11-20T10:04:12.6433689Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T10:04:12.6451937Z  None          
                           Sales Flat.Sales Flat               ExecuteSql 2026-11-20T10:04:12.6502789Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T10:04:13.6340548Z  None          
      Model.15d460ac-5121-4fa3-9240-b70400d77763 RelationshipBuildPrepare 2026-11-20T10:04:13.8893876Z  None          
      Model.55fa90e1-00c5-4666-8bc8-dde516c69228 RelationshipBuildPrepare 2026-11-20T10:04:13.8924697Z  None          
      Model.7a71d08b-0c26-46a2-b754-69b8e39a97f9 RelationshipBuildPrepare 2026-11-20T10:04:16.2493864Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec     Rows
                                     Product Date Grid.Product Date Grid            VertiPaq          5.8     5.8        0
                                     Product Date Grid.Product Date Grid             Process          4.8     4.5        0
                                     Product Date Grid.Product Date Grid      TabularRefresh          4.8     4.5        0
                                     Product Date Grid.Product Date Grid            ReadData          4.4     4.4 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          3.3     1.0        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          2.8     0.9        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          2.7     0.9   104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.0     0.4        0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          0.7     0.1        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          0.5     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          0.5     0.3        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          0.5     0.3   100450
```

**Screenshot: the refresh error of v99i-buffer-stg-sales on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99i-buffer-stg-sales-refresh-error.png**

## Log

```
2026-11-20T10:03:37Z run 20261120T100055Z-v99i-061e: variant=v99i-buffer-stg-sales data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T10:03:46Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T10:03:49Z F64: v99i-buffer-stg-sales is fe4b7ed4-bbdc-48ba-aa51-e9eae49eb056, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T10:04:09Z F64: model size in memory before the refresh: 0.4 MB
2026-11-20T10:04:10Z F64: refresh started, request ad124055-f199-488a-84d2-09abf6fcb1b0
2026-11-20T10:05:20Z F64: refresh failed (Failed) other
2026-11-20T10:05:20Z F64: monitoring database Monitoring KQL database
2026-11-20T10:06:56Z F64: ExecutionMetrics event found
```
