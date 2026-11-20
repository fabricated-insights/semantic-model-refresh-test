# Harness run 20261120T032937Z-v99h-061e

- Task: refresh
- Variant: v99h-staging-buffers
- Data tag: data-1m-v1
- Targets: F64
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 06d5d077-97fc-4bf5-b508-8ec5be5b95f1
- Refresh parallelism requested: 6

## F64

- Result: **failed** (resource governance)
- Peak 25,589 MB, Power Query 25,520 MB, duration 3 min, CPU 522 s, rows 10,743,897, model 1 MB (Backup step in SemanticModelLogs)
- Refresh request 68c02d5f-b890-4728-87b8-4c7b8cd06393, 2026-11-20T03:32:47.857 to 2026-11-20T03:35:32.107, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: SemanticModelLogs ExecutionMetrics
- No earlier harness run of v99h-staging-buffers on F64 data-1m-v1.
- Against v00-baseline on F64 data-1m-v1 (2026-11-19T21:56:46Z): peak 25,589 MB vs 615 MB (+24,974 MB), Power Query 25,520 MB vs 335 MB, model 1 MB vs 73 MB.
- Model size in memory when the full refresh started: 0 MB. The refresh may use the SKU maximum minus this: 25,600 MB on F64.
- Measured peak against the command limit (SKU maximum minus the size before) of each SKU, if the model held the same data there: F2 3,066 MB: OVER (835%); F16 5,120 MB: OVER (500%); F32 10,240 MB: OVER (250%); F64 25,600 MB: fits (100%); PPU 102,400 MB: fits (25%). This assumes the peak, like 'consumed memory' in the errors, does not include the model already in memory; not verified.

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25594 MB, memory limit 25589 MB, database size before command execution 10 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The operation was canceled.. The exception was raised by the IDbCommand interface.
The operation was canceled.. The exception was raised by the IDbCommand interface.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25594 MB, memory limit 25589 MB, database size before command execution 10 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
The command has been canceled.. The exception was raised by the IDataReader interface. Please review the error message and provider documentation for further information and corrective action.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory 25594 MB, memory limit 25589 MB, database size before command execution 10 MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
Resource Governance: This operation was canceled because there wasn't enough memory to finish running it. Either reduce the memory footprint of your dataset by doing things such as limiting the amount of imported data, or if using Power BI Premium, increase the memory of the Premium capacity where this dataset is hosted. More details: consumed memory  MB, memory limit  MB, database size before command execution  MB. See https://go.microsoft.com/fwlink/?linkid=2159753 to learn more.
```

Steps running or failed when it stopped:

```
                                          Object      OperationDetailName                        Began Ended EndStatus
                           Sales Flat.Sales Flat           TabularRefresh 2026-11-20T03:32:50.4895394Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba           TabularRefresh 2026-11-20T03:32:50.5043914Z  None          
                   Customer Stats.Customer Stats           TabularRefresh  2026-11-20T03:32:50.505522Z  None          
Sales.Sales-4929449f-be0b-48cf-a44e-c644698415ba               ExecuteSql 2026-11-20T03:32:50.6893226Z  None          
                           Sales Flat.Sales Flat               ExecuteSql  2026-11-20T03:32:50.694836Z  None          
      Model.15d460ac-5121-4fa3-9240-b70400d77763 RelationshipBuildPrepare 2026-11-20T03:32:52.1568778Z  None          
      Model.55fa90e1-00c5-4666-8bc8-dde516c69228 RelationshipBuildPrepare 2026-11-20T03:32:52.1597608Z  None          
      Model.a7c057d3-ede2-4fdd-812a-d5be2dc1569f RelationshipBuildPrepare  2026-11-20T03:32:52.165358Z  None          
      Model.7a71d08b-0c26-46a2-b754-69b8e39a97f9 RelationshipBuildPrepare 2026-11-20T03:32:59.9494025Z  None          
                   Customer Stats.Customer Stats                  Process 2026-11-20T03:35:17.2357884Z  None          
                   Customer Stats.Customer Stats                 ReadData 2026-11-20T03:35:17.2362503Z  None          
```

Slowest steps:

```
                                                Object OperationDetailName  DurationSec  CpuSec     Rows
                         Customer Stats.Customer Stats          ExecuteSql        146.6     0.0        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59      TabularRefresh          9.1     0.8        0
                   Product Date Grid.Product Date Grid            VertiPaq          5.9     5.9        0
                   Product Date Grid.Product Date Grid             Process          4.6     4.3        0
                   Product Date Grid.Product Date Grid      TabularRefresh          4.6     4.3        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59             Process          4.6     0.8        0
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59            ReadData          4.5     0.8   104990
Customer.Customer-bee8b62a-fee2-49b8-a0b6-5518e67a2d59          ExecuteSql          4.3     0.0        0
                   Product Date Grid.Product Date Grid            ReadData          4.3     4.3 10113306
  Product.Product-9730db17-a88f-43ad-b6f2-50ae8a679b18      TabularRefresh          1.0     0.1        0
      Store.Store-4e2fa8b8-517f-4c17-ae5a-7d36051099bc      TabularRefresh          0.9     0.1        0
                                                                    Commit          0.9     0.0        0
```

**Screenshot: the refresh error of v99h-staging-buffers on F64 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f64-v99h-staging-buffers-resource-governance.png**

## Log

```
2026-11-20T03:32:06Z run 20261120T032937Z-v99h-061e: variant=v99h-staging-buffers data_tag=data-1m-v1 source_type=parquet targets=['F64'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=061e850d-f8a3-4ccb-b525-a7b05e8cd231
2026-11-20T03:32:21Z F64: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-20T03:32:24Z F64: v99h-staging-buffers is 6754d363-b82c-451a-a473-4f6d0b92e672, DataTag reads back data-1m-v1, SourceType parquet
2026-11-20T03:32:47Z F64: model size in memory before the refresh: 0.4 MB
2026-11-20T03:32:48Z F64: refresh started, request 68c02d5f-b890-4728-87b8-4c7b8cd06393
2026-11-20T03:35:58Z F64: refresh failed (Failed) resource governance
2026-11-20T03:35:58Z F64: monitoring database Monitoring KQL database
2026-11-20T03:36:49Z F64: ExecutionMetrics event found
```
