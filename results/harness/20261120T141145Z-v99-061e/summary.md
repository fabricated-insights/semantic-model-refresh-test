# Harness run 20261120T141145Z-v99-061e

- Task: refresh
- Variant: v99-kitchen-sink
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 3a15bc3b-8fc3-4386-9bda-172dc8e6dae0
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 14,826 MB, Power Query 14,747 MB, duration 1 min, CPU 329 s, rows 10,329,373, model n/a (no size)
- Refresh request 4a444e76-9bc4-42e2-a27a-faa1cea6dca6, 2026-11-20T14:14:39.05 to 2026-11-20T14:16:07.01, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99-kitchen-sink on F64 data-1m-v1: failed, peak 14,702 MB (2026-11-20T08:42:58Z).
  - Peak change: +124 MB (+0.8%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 14,826 MB vs 667 MB (+14,159 MB), Power Query 14,747 MB vs 592 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (484%); F16 5,120 MB: OVER (290%); F32 10,240 MB: OVER (145%); F64 25,600 MB: fits (58%); PPU 102,400 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
            768aac35-6135-47bf-bbb0-c54b0aa43296     TabularSequencePoint 2026-11-20T14:14:40.7163803Z  None          
                           Sales Flat.Sales Flat           TabularRefresh 2026-11-20T14:14:40.8695113Z  None          
                   Customer Stats.Customer Stats           TabularRefresh  2026-11-20T14:14:40.890775Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T14:14:40.9059468Z  None          
                   Customer Stats.Customer Stats               ExecuteSql 2026-11-20T14:14:41.0325274Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T14:14:41.0499011Z  None          
                           Sales Flat.Sales Flat               ExecuteSql  2026-11-20T14:14:41.050177Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T14:14:43.3353342Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec     Rows
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         15.3     1.9        0
                                     Product Date Grid.Product Date Grid            VertiPaq         12.5    12.5        0
                                     Product Date Grid.Product Date Grid             Process          9.1     8.4        0
                                     Product Date Grid.Product Date Grid      TabularRefresh          9.1     8.4        0
                                     Product Date Grid.Product Date Grid            ReadData          8.3     8.3 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          8.2     1.8        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          8.1     1.8   104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          7.0     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.3     0.6        0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.0     0.1        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          1.0     0.6        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          0.9     0.6   100450
```

**Screenshot: the refresh error of v99-kitchen-sink on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99-kitchen-sink-refresh-error.png**

## Log

```
2026-11-20T14:14:00Z run 20261120T141145Z-v99-061e: variant=v99-kitchen-sink data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T14:14:13Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T14:14:15Z F64: v99-kitchen-sink is 768aac35-6135-47bf-bbb0-c54b0aa43296, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T14:14:38Z F64: model size in memory before the refresh: 0.1 MB
2026-11-20T14:14:39Z F64: refresh started, request 4a444e76-9bc4-42e2-a27a-faa1cea6dca6
2026-11-20T14:16:19Z F64: refresh failed (Failed) other
2026-11-20T14:16:19Z F64: monitoring database Monitoring KQL database
2026-11-20T14:17:55Z F64: ExecutionMetrics event found
```
