# Harness run 20261120T095609Z-v99h-061e

- Task: refresh
- Variant: v99h-staging-buffers
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 594cd7bf-99a9-4827-934f-c4e39b448759
- Refresh parallelism requested: 6

## F64

- Result: **failed** (other)
- Peak 14,286 MB, Power Query 14,202 MB, duration 1 min, CPU 269 s, rows 10,559,477, model n/a (no size)
- Refresh request a1ec4a89-76b3-4a36-bebb-83b3123f1861, 2026-11-20T09:57:26.39 to 2026-11-20T09:58:38.55, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99h-staging-buffers on F64 data-1m-v1: failed, peak 25,589 MB (2026-11-20T03:36:51Z).
  - Peak change: -11,303 MB (-44.2%). **FLAG: peak changed by more than 1%**
- Against v00-baseline on F64 data-1m-v1 (2026-11-20T05:49:55Z): peak 14,286 MB vs 716 MB (+13,570 MB), Power Query 14,202 MB vs 527 MB, model n/a vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (466%); F16 5,120 MB: OVER (279%); F32 10,240 MB: OVER (140%); F64 25,600 MB: fits (56%); PPU 102,400 MB: fits (14%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

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
                  6754d363-b82c-451a-a473-4f6d0b92e672     TabularSequencePoint  2026-11-20T09:57:28.706119Z  None          
                                 Sales Flat.Sales Flat           TabularRefresh 2026-11-20T09:57:29.0762775Z  None          
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59           TabularRefresh 2026-11-20T09:57:29.0947342Z  None          
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T09:57:29.1348194Z  None          
      Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T09:57:29.2771411Z  None          
                                 Sales Flat.Sales Flat               ExecuteSql 2026-11-20T09:57:29.3087713Z  None          
                         Customer Stats.Customer Stats           TabularRefresh 2026-11-20T09:57:30.8374737Z  None          
                         Customer Stats.Customer Stats               ExecuteSql 2026-11-20T09:57:30.9198066Z  None          
            Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T09:57:31.9627857Z  None          
            Model.15d460ac-5121-4fa3-9240-b70400d77763 RelationshipBuildPrepare   2026-11-20T09:57:32.14599Z  None          
            Model.55fa90e1-00c5-4666-8bc8-dde516c69228 RelationshipBuildPrepare   2026-11-20T09:57:32.15608Z  None          
                   Product Date Grid.Product Date Grid           TabularRefresh  2026-11-20T09:57:32.241301Z  None          
                   Product Date Grid.Product Date Grid                  Process 2026-11-20T09:57:32.2648396Z  None          
                   Product Date Grid.Product Date Grid                 ReadData 2026-11-20T09:57:32.2720101Z  None          
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59                  Process 2026-11-20T09:57:39.9434419Z  None          
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59                 ReadData 2026-11-20T09:57:39.9530508Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql         10.7     0.0      0
                                     Product Date Grid.Product Date Grid            VertiPaq          8.8     8.8      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          3.0     0.2      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          2.5     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.7     0.3      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.6     1.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be            ReadData          1.2     0.9 100450
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be             Process          1.2     0.9      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          1.1     0.1      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          0.9     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          0.9     0.0      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b            ReadData          0.5     0.2   4018
```

**Screenshot: the refresh error of v99h-staging-buffers on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99h-staging-buffers-refresh-error.png**

## Log

```
2026-11-20T09:56:54Z run 20261120T095609Z-v99h-061e: variant=v99h-staging-buffers data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T09:57:04Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T09:57:08Z F64: v99h-staging-buffers is 6754d363-b82c-451a-a473-4f6d0b92e672, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T09:57:26Z F64: model size in memory before the refresh: 0.4 MB
2026-11-20T09:57:26Z F64: refresh started, request a1ec4a89-76b3-4a36-bebb-83b3123f1861
2026-11-20T09:59:07Z F64: refresh failed (Failed) other
2026-11-20T09:59:07Z F64: monitoring database Monitoring KQL database
2026-11-20T09:59:56Z F64: ExecutionMetrics event found
```
