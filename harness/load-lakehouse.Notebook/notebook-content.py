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
load = "true"                     # "false": skip the load, only compare
compare_csv = "true"              # compare the CSV releases (data-1m-csv, data-10m-csv) with the loaded tables

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


def stage(tag, file_name):
    """Download one release file to Files/data/<tag>/ and return its OneLake path."""
    url = f"{base_url}/{tag}/{file_name}"
    local = os.path.join(tempfile.gettempdir(), f"{tag}-{file_name}")
    with requests.get(url, stream=True, timeout=600) as r:
        if r.status_code != 200:
            raise Exception(f"{url}: HTTP {r.status_code}. Is the repo public?")
        with open(local, "wb") as f:
            for chunk in r.iter_content(8 << 20):
                f.write(chunk)
    staged = f"{LAKE}/Files/data/{tag}/{file_name}"
    notebookutils.fs.cp(f"file://{local}", staged)
    os.remove(local)
    return staged

loaded = []
for tag in ([t.strip() for t in tags.split(",") if t.strip()] if load.lower() == "true" else []):
    for name in [f.strip() for f in files.split(",") if f.strip()]:
        staged = stage(tag, f"{name}.parquet")
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

# MARKDOWN ********************

# ## Compare the CSV releases with the Parquet data
# The CSV files are a separate export, not converted from the Parquet files. Two columns have other names
# (orders OrderDate is DT in Parquet, orderrows LineNumber is RowNumber). Read as text, renamed and cast to
# the Parquet types (the same step the models take), each file is compared with its table in lab_data:
# row count, and per column the nulls, the sum of numbers, the distinct count of text and the date range.

# CELL ********************

from pyspark.sql import functions as F

RENAME = {"orders": {"OrderDate": "DT"}, "orderrows": {"LineNumber": "RowNumber"}}
diffs = []
for tag in ([t.strip() for t in tags.split(",") if t.strip()] if compare_csv.lower() == "true" else []):
    csv_tag = tag.replace("-v1", "-csv")
    for name in [f.strip() for f in files.split(",") if f.strip()]:
        pq = spark.read.format("delta").load(f"{LAKE}/Tables/{SCHEMA[tag]}/{name}")
        raw = spark.read.option("header", True).option("inferSchema", False).csv(stage(csv_tag, f"{name}.csv"))
        for a, b in RENAME.get(name, {}).items():
            raw = raw.withColumnRenamed(a, b)
        types = dict(pq.dtypes)
        missing = [c for c in pq.columns if c not in raw.columns]
        if missing:
            diffs.append((csv_tag, name, "columns missing in CSV", str(missing), ""))
            continue
        cs = raw.select([(F.when(F.col(c) == "", None).otherwise(F.col(c)) if types[c] != "string" else F.col(c))
                         .cast(types[c]).alias(c) for c in pq.columns])
        def profile(df):
            aggs = [F.count(F.lit(1)).alias("rows")]
            for c, t in df.dtypes:
                aggs.append(F.sum(F.col(c).isNull().cast("int")).alias(f"{c}|nulls"))
                if t.startswith(("int", "bigint", "decimal", "double")):
                    aggs.append(F.sum(F.col(c).cast("decimal(38,6)")).alias(f"{c}|sum"))
                elif t == "string":
                    aggs.append(F.countDistinct(F.col(c)).alias(f"{c}|distinct"))
                    aggs.append(F.sum((F.col(c) == "").cast("int")).alias(f"{c}|empty"))
                else:
                    aggs.append(F.min(F.col(c)).alias(f"{c}|min"))
                    aggs.append(F.max(F.col(c)).alias(f"{c}|max"))
            return df.agg(*aggs).first().asDict()
        a, b = profile(pq), profile(cs)
        for k in a:
            if a[k] != b[k]:
                diffs.append((csv_tag, name, k, str(a[k]), str(b[k])))
        print(f"{csv_tag} {name}: {a['rows']:,} Parquet rows, {b['rows']:,} CSV rows, "
              f"{sum(1 for k in a if a[k] != b[k])} differences")

report = ["Loaded tables:"] + [f"{t:24} {n:>12,}  {ty}" for t, n, ty in loaded]
report += ["", "CSV against Parquet, measures that differ:",
           f"{'release':14} {'file':17} {'measure':28} {'Parquet':>24} {'CSV':>24}"]
report += [f"{d[0]:14} {d[1]:17} {d[2]:28} {d[3]:>24} {d[4]:>24}" for d in diffs]
# Spark reads an empty CSV field as null; Power Query's Csv.Document keeps it as an empty text.
text = "\n".join(report) + "\n"
notebookutils.fs.put(f"{LAKE}/Files/data/load-report.txt", text, True)
print(text)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
