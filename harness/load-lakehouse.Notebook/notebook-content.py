# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# # Load the lab data into lab_data
# Downloads the Parquet files of the data releases and writes one Delta table per file to the
# schema-enabled lakehouse `lab_data`: schema `data_1m` for data-1m-v1 and `data_10m` for data-10m-v1
# (`data_1m.sales`, `data_10m.sales`, ...). Models with `SourceType = "sql"` read these tables
# through the lakehouse SQL endpoint. Column types stay as in the Parquet files (int32, int64,
# decimal(20,5), string); timestamps are UTC instants and arrive in SQL as datetime2 in UTC, the same
# values the Parquet models get after dropping the zone.
# Run once by hand, or again after a data release changes. Overwrites the tables it writes, nothing else.

# PARAMETERS CELL ********************

tags = "data-1m-v1,data-10m-v1"   # releases to load
files = "currencyexchange,customer,date,orderrows,orders,product,sales,store"
base_url = "https://github.com/fabricated-insights/semantic-model-refresh-test/releases/download"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import os
import tempfile

import requests
import sempy.fabric as fabric
import notebookutils

SCHEMA = {"data-1m-v1": "data_1m", "data-10m-v1": "data_10m"}
ws = notebookutils.runtime.context["currentWorkspaceId"]
lakes = fabric.FabricRestClient().get(f"v1/workspaces/{ws}/lakehouses").json()["value"]
lake_id = [l["id"] for l in lakes if l["displayName"] == "lab_data"][0]
LAKE = f"abfss://{ws}@onelake.dfs.fabric.microsoft.com/{lake_id}"
spark.conf.set("spark.sql.session.timeZone", "UTC")   # timestamps stay UTC end to end

loaded = []
for tag in [t.strip() for t in tags.split(",") if t.strip()]:
    for name in [f.strip() for f in files.split(",") if f.strip()]:
        url = f"{base_url}/{tag}/{name}.parquet"
        local = os.path.join(tempfile.gettempdir(), f"{tag}-{name}.parquet")
        with requests.get(url, stream=True, timeout=600) as r:
            if r.status_code != 200:
                raise Exception(f"{url}: HTTP {r.status_code}. Is the repo public?")
            with open(local, "wb") as f:
                for chunk in r.iter_content(8 << 20):
                    f.write(chunk)
        staged = f"{LAKE}/Files/data/{tag}/{name}.parquet"
        notebookutils.fs.cp(f"file://{local}", staged)
        os.remove(local)
        df = spark.read.parquet(staged)
        table = f"{SCHEMA[tag]}/{name}"   # a folder under Tables is a schema in a schema-enabled lakehouse
        df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(f"{LAKE}/Tables/{table}")
        n = spark.read.format("delta").load(f"{LAKE}/Tables/{table}").count()
        loaded.append((table, n, ", ".join(f"{c}:{t}" for c, t in df.dtypes)))
        print(f"{table}: {n:,} rows")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

for table, n, types in loaded:
    print(f"{table:24} {n:>12,}  {types}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
