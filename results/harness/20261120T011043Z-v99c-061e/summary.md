# Harness run 20261120T011043Z-v99c-061e

- Task: refresh
- Variant: v99c-crossjoin-only
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 38ba70e3-625a-4cff-8aaa-bd8587b6a883
- Refresh parallelism requested: 6

## F64

- Result: **failed** (resource governance)
- Peak 25,555 MB, Power Query 25,510 MB, duration 3 min, CPU 528 s, rows 10,616,193, model 0 MB (Backup step in SemanticModelLogs)
- Refresh request f45f496d-6f74-4c8c-a6a8-67c13298d6f6, 2026-11-20T01:11:53.96 to 2026-11-20T01:14:44.163, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- Previous harness run of v99c-crossjoin-only on F64 data-1m-v1: failed, peak 25,592 MB (2026-11-18T14:23:59Z).
  - Peak change: -37 MB (-0.1%).
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 25,555 MB vs 615 MB (+24,940 MB), Power Query 25,510 MB vs 335 MB, model 0 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (834%); F16 5,120 MB: OVER (499%); F32 10,240 MB: OVER (250%); F64 25,600 MB: fits (100%); PPU 102,400 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25612 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25612 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25612 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

Steps running or failed when it stopped:

```
                                          Object      OperationDetailName                        Began Ended EndStatus
                           Sales Flat.Sales Flat           TabularRefresh 2026-11-20T01:11:57.6080237Z  None          
                   Customer Stats.Customer Stats           TabularRefresh 2026-11-20T01:11:57.6704084Z  None          
                           Sales Flat.Sales Flat               ExecuteSql 2026-11-20T01:11:57.7545798Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T01:11:58.7342464Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql  2026-11-20T01:11:58.766756Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T01:11:59.2461094Z  None          
                   Customer Stats.Customer Stats                  Process 2026-11-20T01:14:24.2225164Z  None          
                   Customer Stats.Customer Stats                 ReadData 2026-11-20T01:14:24.2230823Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec     Rows
                                           Customer Stats.Customer Stats          ExecuteSql        146.5     0.0        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          8.3     1.3        0
                                     Product Date Grid.Product Date Grid            VertiPaq          6.7     6.6        0
                                     Product Date Grid.Product Date Grid             Process          5.2     4.8        0
                                     Product Date Grid.Product Date Grid      TabularRefresh          5.2     4.8        0
                                     Product Date Grid.Product Date Grid            ReadData          4.8     4.8 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          4.6     1.2        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          4.5     1.2   104990
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          3.6     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.6     0.3        0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.3     0.0        0
                          Date.Date-44d762f0-a871-4687-b253-096276d9658b      TabularRefresh          1.2     0.1        0
```

**Screenshot: the refresh error of v99c-crossjoin-only on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99c-crossjoin-only-resource-governance.png**

## Log

```
2026-11-20T01:11:23Z run 20261120T011043Z-v99c-061e: variant=v99c-crossjoin-only data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T01:11:34Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T01:11:37Z F64: v99c-crossjoin-only is daa7e567-713a-45fb-9a38-cd372ab42dd8, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T01:11:53Z F64: model size in memory before the refresh: 0.1 MB
2026-11-20T01:11:54Z F64: refresh started, request f45f496d-6f74-4c8c-a6a8-67c13298d6f6
2026-11-20T01:15:04Z F64: refresh failed (Failed) resource governance
2026-11-20T01:15:05Z F64: monitoring database Monitoring KQL database
2026-11-20T01:16:40Z F64: ExecutionMetrics event found
```
