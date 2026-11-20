# Harness run 20261120T010123Z-v99b-061e

- Task: refresh
- Variant: v99b-one-sales-copy
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: a4800bf9-4d40-471f-aceb-a725100d108b
- Refresh parallelism requested: 6

## F64

- Result: **failed** (resource governance)
- Peak 25,582 MB, Power Query 25,530 MB, duration 4 min, CPU 727 s, rows 597,095, model 0 MB (Backup step in SemanticModelLogs)
- Refresh request 89720265-1cee-4867-b3b1-458d433f0f24, 2026-11-20T01:04:12.87 to 2026-11-20T01:07:53.227, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99b-one-sales-copy on F64 data-1m-v1: failed, peak 25,592 MB (2026-11-18T14:00:59Z).
  - Peak change: -10 MB (-0.0%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 25,582 MB vs 615 MB (+24,967 MB), Power Query 25,530 MB vs 335 MB, model 0 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (834%); F16 5,120 MB: OVER (500%); F32 10,240 MB: OVER (250%); F64 25,600 MB: fits (100%); PPU 102,400 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25609 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25609 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25609 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

Steps running or failed when it stopped:

```
                                          Object      OperationDetailName                        Began Ended EndStatus
                   Customer Stats.Customer Stats           TabularRefresh  2026-11-20T01:04:15.286083Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T01:04:16.5731193Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T01:04:16.6008028Z  None          
                           Sales Flat.Sales Flat           TabularRefresh 2026-11-20T01:04:16.6818009Z  None          
                           Sales Flat.Sales Flat               ExecuteSql 2026-11-20T01:04:16.7143341Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T01:04:17.2955081Z  None          
                   Customer Stats.Customer Stats                  Process 2026-11-20T01:07:01.3727748Z  None          
                   Customer Stats.Customer Stats                 ReadData 2026-11-20T01:07:01.3731794Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec   Rows
                                           Customer Stats.Customer Stats          ExecuteSql        165.9     0.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          8.3     1.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          4.2     0.0      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          4.0     0.9      0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          3.9     0.9 104990
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          2.0     0.1      0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b          ExecuteSql          1.7     0.0      0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.7     0.3      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.4     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          1.3     0.0      0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          1.2     0.0      0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          1.1     0.0      0
```

**Screenshot: the refresh error of v99b-one-sales-copy on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99b-one-sales-copy-resource-governance.png**

## Log

```
2026-11-20T01:03:36Z run 20261120T010123Z-v99b-061e: variant=v99b-one-sales-copy data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T01:03:49Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T01:03:53Z F64: v99b-one-sales-copy is 1fe6d06d-415b-469f-9bfa-d9105a1aa0a2, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T01:04:12Z F64: model size in memory before the refresh: 0.1 MB
2026-11-20T01:04:13Z F64: refresh started, request 89720265-1cee-4867-b3b1-458d433f0f24
2026-11-20T01:08:23Z F64: refresh failed (Failed) resource governance
2026-11-20T01:08:23Z F64: monitoring database Monitoring KQL database
2026-11-20T01:09:59Z F64: ExecutionMetrics event found
```
