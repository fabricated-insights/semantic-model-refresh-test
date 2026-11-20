# Harness run 20261120T002621Z-v99-061e

- Task: refresh
- Variant: v99-kitchen-sink
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: f91437a9-286e-45b5-9045-5b8edbf77e3e
- Refresh parallelism requested: 6

## F64

- Result: **failed** (resource governance)
- Peak 25,589 MB, Power Query 25,503 MB, duration 7 min, CPU 1,565 s, rows 10,698,113, model 0 MB (Backup step in SemanticModelLogs)
- Refresh request fd5f75d1-4218-41f6-91f4-f822cbae722a, 2026-11-20T00:29:38.107 to 2026-11-20T00:36:37.907, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99-kitchen-sink on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 25,589 MB vs 615 MB (+24,974 MB), Power Query 25,503 MB vs 335 MB, model 0 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (835%); F16 5,120 MB: OVER (500%); F32 10,240 MB: OVER (250%); F64 25,600 MB: fits (100%); PPU 102,400 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25604 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25604 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25604 MB, memory limit 25592 MB, database size before command execution 7 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

Steps running or failed when it stopped:

```
                                          Object      OperationDetailName                        Began Ended EndStatus
                           Sales Flat.Sales Flat           TabularRefresh 2026-11-20T00:29:39.4039534Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T00:29:39.4197882Z  None          
                           Sales Flat.Sales Flat               ExecuteSql 2026-11-20T00:29:39.5483297Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T00:29:39.5503211Z  None          
                   Customer Stats.Customer Stats           TabularRefresh 2026-11-20T00:29:41.8836722Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T00:29:43.0271618Z  None          
                   Customer Stats.Customer Stats                  Process 2026-11-20T00:34:39.8197635Z  None          
                   Customer Stats.Customer Stats                 ReadData 2026-11-20T00:34:39.8205119Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec     Rows
                                           Customer Stats.Customer Stats          ExecuteSql        297.9     0.0        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh         14.9     1.6        0
                                     Product Date Grid.Product Date Grid            VertiPaq          9.9     9.9        0
                                     Product Date Grid.Product Date Grid      TabularRefresh          8.5     8.0        0
                                     Product Date Grid.Product Date Grid             Process          8.5     8.0        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          8.0     0.0        0
                                     Product Date Grid.Product Date Grid            ReadData          7.9     8.0 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          6.9     1.5        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          6.8     1.5   104990
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          3.3     0.5        0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          3.0     0.1        0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18          ExecuteSql          2.7     0.0        0
```

**Screenshot: the refresh error of v99-kitchen-sink on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99-kitchen-sink-resource-governance.png**

## Log

```
2026-11-20T00:28:57Z run 20261120T002621Z-v99-061e: variant=v99-kitchen-sink data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T00:29:10Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T00:29:13Z F64: v99-kitchen-sink is 768aac35-6135-47bf-bbb0-c54b0aa43296, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T00:29:38Z F64: model size in memory before the refresh: 0.1 MB
2026-11-20T00:29:38Z F64: refresh started, request fd5f75d1-4218-41f6-91f4-f822cbae722a
2026-11-20T00:36:50Z F64: refresh failed (Failed) resource governance
2026-11-20T00:36:50Z F64: monitoring database Monitoring KQL database
2026-11-20T00:38:26Z F64: ExecutionMetrics event found
```
