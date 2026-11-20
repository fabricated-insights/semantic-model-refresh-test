# Harness run 20261120T150125Z-v99f-061e

- Task: refresh
- Variant: v99f-calc-tables
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: e7a64db0-751a-453c-a4d9-7e87731e9875
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 385 MB, Power Query 364 MB, duration 0 min, CPU 7 s, rows 38,519, model n/a (no size)
- Refresh request 0c49d40b-b153-4ff7-86df-1fe02fe2a1ff, 2026-11-20T15:04:45.583 to 2026-11-20T15:04:50.13, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99f-calc-tables on F64 data-1m-v1: failed, peak 1,052 MB (2026-11-20T09:50:44Z).
  - Peak change: -667 MB (-63.4%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T11:27:17Z): peak 385 MB vs 667 MB (-282 MB), Power Query 364 MB vs 592 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 386 MB. The refresh may use the SKU maximum minus this: 25,214 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 2,680 MB: fits (14%); F16 4,734 MB: fits (8%); F32 9,854 MB: fits (4%); F64 25,214 MB: fits (2%); PPU 102,014 MB: fits (0%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Information is needed in order to combine data. Please specify a privacy level for each data source.;Information about a data source is required.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The current operation was cancelled because another operation in the transaction failed.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
```

Steps running or failed when it stopped:

```
                                                                  Object  OperationDetailName                        Began Ended EndStatus
                                    841b2a42-15a1-46af-911e-9d8fc71b8909 TabularSequencePoint 2026-11-20T15:04:47.8793544Z  None          
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b       TabularRefresh  2026-11-20T15:04:48.062132Z  None          
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba       TabularRefresh 2026-11-20T15:04:48.0627396Z  None          
                                                   Sales Flat.Sales Flat       TabularRefresh 2026-11-20T15:04:48.0656058Z  None          
                                           Customer Stats.Customer Stats       TabularRefresh 2026-11-20T15:04:48.0775423Z  None          
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59       TabularRefresh 2026-11-20T15:04:48.0780719Z  None          
                                           Customer Stats.Customer Stats           ExecuteSql 2026-11-20T15:04:48.2303182Z  None          
                        Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           ExecuteSql 2026-11-20T15:04:48.2306155Z  None          
                                                   Sales Flat.Sales Flat           ExecuteSql 2026-11-20T15:04:48.2419747Z  None          
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59              Process 2026-11-20T15:04:49.2725728Z  None          
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             ReadData 2026-11-20T15:04:49.2745424Z  None          
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be       TabularRefresh 2026-11-20T15:04:49.3809936Z  None          
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be              Process 2026-11-20T15:04:49.6856782Z  None          
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             ReadData 2026-11-20T15:04:49.6865274Z  None          
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b              Process 2026-11-20T15:04:49.7203185Z  None          
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b             ReadData 2026-11-20T15:04:49.7225845Z  None          
```

Slowest steps:

```
                                                                                                       Object OperationDetailName  DurationSec  CpuSec  Rows
                                                               Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          1.5     0.0     0
                                                             Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          1.3     0.1     0
                                                             Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          1.1     0.0     0
                                                       Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          1.0     0.0     0
                                     Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be          ExecuteSql          0.3     0.0     0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f            ReadData          0.0     0.0     1
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f            VertiPaq          0.0     0.0     0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f     CompressSegment          0.0     0.0     0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f   AnalyzeEncodeData          0.0     0.0     0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f             Process          0.0     0.0     0
DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f.DateTableTemplate_bda775d5-d7fb-4133-ac68-c3454dbd392f      TabularRefresh          0.0     0.0     0
                                                             Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc            ReadData          0.0     0.0    74
```

**Screenshot: the refresh error of v99f-calc-tables on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99f-calc-tables-refresh-error.png**

## Log

```
2026-11-20T15:04:01Z run 20261120T150125Z-v99f-061e: variant=v99f-calc-tables data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T15:04:10Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T15:04:17Z F64: v99f-calc-tables is 841b2a42-15a1-46af-911e-9d8fc71b8909, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T15:04:45Z F64: model size in memory before the refresh: 385.7 MB
2026-11-20T15:04:45Z F64: refresh started, request 0c49d40b-b153-4ff7-86df-1fe02fe2a1ff
2026-11-20T15:04:56Z F64: refresh failed (Failed) other
2026-11-20T15:04:56Z F64: monitoring database Monitoring KQL database
2026-11-20T15:07:33Z F64: ExecutionMetrics event found
```
