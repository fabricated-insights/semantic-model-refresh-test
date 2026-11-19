# Harness run 20261119T213746Z-v00-e02a

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: f20fbcf1c0f30239000712aeb1056d5b8bcf2fa1
- Notebook run: 1774a3a3-f449-4627-b6e6-0d9cd9d30be6
- Refresh parallelism requested: 6

## F2

- Result: **failed** (other)
- Peak n/a, Power Query n/a, duration 0 min, CPU n/a, rows n/a, model n/a (no size)
- Refresh request 8288b81d-53fc-418d-b106-1962cc4ae2c5, 2026-11-19T21:41:34.387 to 2026-11-19T21:41:38.76, workspace at f20fbcf, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v00-baseline on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T21:04:53Z).
  - **FLAG: result changed from refreshed to failed**
- Model size in memory when the full refresh started: 66 MB. The refresh may use the SKU maximum minus this: 3,000 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

Error text:

```
Retry attempts for failures while executing the refresh exceeded the retry limit set on the request.
{"error":{"code":"Premium_ASWL_Error","pbi.error":{"code":"Premium_ASWL_Error","parameters":{},"details":[{"code":"Premium_ASWL_Error_Details_Label","detail":{"type":1,"value":"We cannot refresh this semantic model because this semantic model uses a default data connection without explicit connection credentials. Please replace the default data connection in the semantic model settings with an explicit cloud or gateway data connection."}}],"exceptionCulprit":1}}}
{"error":{"code":"Premium_ASWL_Error","pbi.error":{"code":"Premium_ASWL_Error","parameters":{},"details":[{"code":"Premium_ASWL_Error_Details_Label","detail":{"type":1,"value":"We cannot refresh this semantic model because this semantic model uses a default data connection without explicit connection credentials. Please replace the default data connection in the semantic model settings with an explicit cloud or gateway data connection."}}],"exceptionCulprit":1}}}
The current operation was cancelled because another operation in the transaction failed.
{"error":{"code":"Premium_ASWL_Error","pbi.error":{"code":"Premium_ASWL_Error","parameters":{},"details":[{"code":"Premium_ASWL_Error_Details_Label","detail":{"type":1,"value":"We cannot refresh this semantic model because this semantic model uses a default data connection without explicit connection credentials. Please replace the default data connection in the semantic model settings with an explicit cloud or gateway data connection."}}],"exceptionCulprit":1}}}
{"error":{"code":"Premium_ASWL_Error","pbi.error":{"code":"Premium_ASWL_Error","parameters":{},"details":[{"code":"Premium_ASWL_Error_Details_Label","detail":{"type":1,"value":"We cannot refresh this semantic model because this semantic model uses a default data connection without explicit connection credentials. Please replace the default data connection in the semantic model settings with an explicit cloud or gateway data connection."}}],"exceptionCulprit":1}}}
```

**Screenshot: the refresh error of v00-baseline on F2 in the service (semantic model > Refresh history > error details), saved as docs/screenshots/f2-v00-baseline-refresh-error.png**

## Log

```
2026-11-19T21:40:24Z run 20261119T213746Z-v00-e02a: variant=v00-baseline data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=f20fbcf1c0f30239000712aeb1056d5b8bcf2fa1 pipeline_run=e02a8497-5741-4d45-9d57-4bb980f11988
2026-11-19T21:40:33Z F2: update from Git f223dfef873d39cf48b77eda7b75a0a8e5a91f74 -> f20fbcf1c0f30239000712aeb1056d5b8bcf2fa1
2026-11-19T21:41:13Z F2: v00-baseline is d5bd2831-6c52-4bdd-a667-69f292f70ca4, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T21:41:34Z F2: model size in memory before the refresh: 66.2 MB
2026-11-19T21:41:34Z F2: refresh started, request 8288b81d-53fc-418d-b106-1962cc4ae2c5
2026-11-19T21:41:44Z F2: refresh failed (Failed) other
```
