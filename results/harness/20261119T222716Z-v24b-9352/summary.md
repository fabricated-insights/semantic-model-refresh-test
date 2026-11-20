# Harness run 20261119T222716Z-v24b-9352

- Task: refresh
- Variant: v24b-second-fact-bidirectional
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: eb585e4bb20f00c4f5196dab488d2b31c10568a2
- Notebook run: 43be7594-ecdf-487d-8be8-e1a10e14cd07
- Refresh parallelism requested: 6

## F2

- Result: **refreshed** 
- Peak n/a, Power Query n/a, duration 7 min, CPU n/a, rows n/a, model 110 MB (INFO.STORAGETABLECOLUMNSEGMENTS + dictionaries (DAX))
- Refresh request c1cbc67d-0415-41fb-a59d-dea9ffe03d09, 2026-11-19T22:30:28.247 to 2026-11-19T22:37:16.297, workspace at eb585e4, DataTag read back data-1m-v1
- Numbers from: refresh API
- Previous harness run of v24b-second-fact-bidirectional on F2 data-1m-v1: refreshed, peak n/a (2026-11-18T12:58:28Z).
- No v00-baseline harness run with a measured peak on F2 data-1m-v1 to compare with.
- Model size in memory when the full refresh started: 82 MB. The refresh may use the SKU maximum minus this: 2,984 MB on F2.
- No peak measured (this capacity has no monitoring and the refresh gave no memory figure).

## Log

```
2026-11-19T22:29:49Z run 20261119T222716Z-v24b-9352: variant=v24b-second-fact-bidirectional data_tag=data-1m-v1 source_type=parquet targets=['F2'] expected_commit=eb585e4bb20f00c4f5196dab488d2b31c10568a2 pipeline_run=93523ee1-3673-4ebc-892f-7f87f528e0de
2026-11-19T22:29:59Z F2: workspace already at eb585e4bb20f00c4f5196dab488d2b31c10568a2
2026-11-19T22:30:02Z F2: v24b-second-fact-bidirectional is 256381b6-5aae-4faa-bb41-efc1cb01273a, DataTag reads back data-1m-v1, SourceType parquet
2026-11-19T22:30:28Z F2: model size in memory before the refresh: 82.4 MB
2026-11-19T22:30:30Z F2: refresh started, request c1cbc67d-0415-41fb-a59d-dea9ffe03d09
2026-11-19T22:37:41Z F2: refresh refreshed (Completed) 
2026-11-19T22:37:43Z F2: model size in memory right after the refresh: 110.0 MB
```
