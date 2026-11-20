# Harness run 20261120T033721Z-v99i-061e

- Task: refresh
- Variant: v99i-buffer-stg-sales
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 4caaeba5-2972-4889-8be0-0449c36d073d
- Refresh parallelism requested: 6

## F64

- Result: **failed** (resource governance)
- Peak 25,521 MB, Power Query 25,482 MB, duration 3 min, CPU 687 s, rows 10,948,697, model 1 MB (Backup step in SemanticModelLogs)
- Refresh request e2d3f38c-9e50-4a9f-bc3f-1e5e5831c45a, 2026-11-20T03:40:43.707 to 2026-11-20T03:44:07.917, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99i-buffer-stg-sales on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 25,521 MB vs 615 MB (+24,906 MB), Power Query 25,482 MB vs 335 MB, model 1 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (832%); F16 5,120 MB: OVER (498%); F32 10,240 MB: OVER (249%); F64 25,600 MB: fits (100%); PPU 102,400 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25595 MB, memory limit 25589 MB, database size before command execution 10 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25595 MB, memory limit 25589 MB, database size before command execution 10 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25595 MB, memory limit 25589 MB, database size before command execution 10 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

Steps running or failed when it stopped:

```
                                          Object      OperationDetailName                        Began Ended EndStatus
                   Customer Stats.Customer Stats           TabularRefresh 2026-11-20T03:40:46.2471043Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T03:40:46.3100845Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T03:40:46.4555588Z  None          
                           Sales Flat.Sales Flat           TabularRefresh 2026-11-20T03:40:47.8899301Z  None          
                           Sales Flat.Sales Flat               ExecuteSql 2026-11-20T03:40:47.9421603Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare 2026-11-20T03:40:48.0873514Z  None          
      Model.15d460ac-5121-4fa3-9240-b70400d77763 RelationshipBuildPrepare 2026-11-20T03:40:49.0079963Z  None          
      Model.55fa90e1-00c5-4666-8bc8-dde516c69228 RelationshipBuildPrepare 2026-11-20T03:40:49.0108937Z  None          
      Model.7a71d08b-0c26-46a2-b754-69b8e39a97f9 RelationshipBuildPrepare 2026-11-20T03:40:50.9683229Z  None          
                   Customer Stats.Customer Stats                  Process 2026-11-20T03:43:10.3321205Z  None          
                   Customer Stats.Customer Stats                 ReadData 2026-11-20T03:43:10.3325218Z  None          
```

Slowest steps:

```
                                                                  Object OperationDetailName  DurationSec  CpuSec     Rows
                                           Customer Stats.Customer Stats          ExecuteSql        143.9     0.0        0
                                     Product Date Grid.Product Date Grid            VertiPaq          5.8     5.8        0
                                     Product Date Grid.Product Date Grid             Process          4.7     4.4        0
                                     Product Date Grid.Product Date Grid      TabularRefresh          4.7     4.4        0
                                     Product Date Grid.Product Date Grid            ReadData          4.3     4.3 10113306
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          4.2     0.9        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          2.9     0.8        0
                  Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          2.8     0.8   104990
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          2.7     0.0        0
                        Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc          ExecuteSql          2.5     0.0        0
Currency Exchange.Currency Exchange-84d00514-3ac1-4a6c-a61b-f2bed7b860be      TabularRefresh          1.6     0.3        0
                    Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.3     0.1        0
```

**Screenshot: the refresh error of v99i-buffer-stg-sales on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99i-buffer-stg-sales-resource-governance.png**

## Log

```
2026-11-20T03:40:06Z run 20261120T033721Z-v99i-061e: variant=v99i-buffer-stg-sales data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T03:40:18Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T03:40:21Z F64: v99i-buffer-stg-sales is fe4b7ed4-bbdc-48ba-aa51-e9eae49eb056, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T03:40:43Z F64: model size in memory before the refresh: 0.4 MB
2026-11-20T03:40:43Z F64: refresh started, request e2d3f38c-9e50-4a9f-bc3f-1e5e5831c45a
2026-11-20T03:44:24Z F64: refresh failed (Failed) resource governance
2026-11-20T03:44:24Z F64: monitoring database Monitoring KQL database
2026-11-20T03:46:00Z F64: ExecutionMetrics event found
```
