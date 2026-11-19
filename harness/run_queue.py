"""Start a queue of harness runs in Fabric, check on it, and collect its results.

The queue runs in the F64 workspace as the harness-queue pipeline: one refresh-harness notebook run per
entry, one after the other. Once started it needs nothing from this machine: a sleeping laptop or a lost
connection does not stop it. Pro runs deploy the model from the F64 workspace inside the notebook.

Usage (from the repo root, after the models are committed and pushed):

    python harness/run_queue.py start v00-baseline v20-pq-sort --targets F2,F64,PPU,Pro
    python harness/run_queue.py status JOB_ID
    python harness/run_queue.py collect JOB_ID

start    Reads DataTag and SourceType of each variant from HEAD, checks that HEAD is pushed, brings the
         F64 workspace up to it (so the notebook and pipeline that run are the committed ones), and starts
         the pipeline. Saves the queue to results/queues/<job id>.json.
collect  Downloads the run folders of that queue from harness_lake that are not in the repo yet and
         appends their rows to results/harness-runs.csv, as run_variant.py does for a single run.
         Safe to run again while the queue is still running: it only adds what is new.

Auth: the signed-in az CLI user. Python standard library only.
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_variant import (FABRIC, HARNESS_WS, LAKEHOUSE, ONELAKE, ROOT, check_pushed, committed_data_tag,  # noqa: E402
                         download, fabric, git, http, item_id, pull_results, sync_harness_workspace)

PIPELINE = "harness-queue"
QUEUES = ROOT / "results" / "queues"


def committed_source_type(variant):
    text = git("show", f"HEAD:models/{variant}/{variant}.SemanticModel/definition/expressions.tmdl")
    m = re.search(r'expression\s+SourceType\s*=\s*"([^"]+)"', text)
    return m.group(1) if m else "parquet"   # models from before the parameter load Parquet


def build_queue(variants, targets, repeats, cooldown, clear_first):
    """Round robin: every variant once, then every variant again, so the repeats of one model are spread
    over the whole queue instead of running back to back. F2 is only in the first round: its result is
    pass or fail, and more F2 runs wait for a decision after the first."""
    tags = {v: (committed_data_tag(v), committed_source_type(v)) for v in variants}
    queue = []
    for rnd in range(1, repeats + 1):
        caps = [t for t in targets if rnd == 1 or t != "F2"]
        if not caps:
            break
        for v in variants:
            queue.append({"variant": v, "targets": ",".join(caps), "data_tag": tags[v][0], "source_type": tags[v][1],
                          "clear_first": "true" if clear_first else "false",
                          "deploy_pro": "true" if "Pro" in caps else "false", "task": "refresh",
                          "cooldown_seconds": cooldown, "round": rnd})
    return queue


def start(variants, targets, clear_first, repeats=1, cooldown=0):
    for v in variants:
        if not (ROOT / "models" / v).is_dir():
            sys.exit(f"models/{v} does not exist")
    targets = [t.strip() for t in targets.split(",") if t.strip()]
    commit = check_pushed()
    queue = build_queue(variants, targets, repeats, cooldown, clear_first)
    for v in variants:
        q = next(e for e in queue if e["variant"] == v)
        print(f"  {v}: DataTag {q['data_tag']}, SourceType {q['source_type']}")
    for rnd in sorted({q["round"] for q in queue}):
        print(f"  round {rnd}: {sum(1 for q in queue if q['round'] == rnd)} entries, targets "
              f"{next(q['targets'] for q in queue if q['round'] == rnd)}")
    print(f"  {len(queue)} entries in all, cooldown {cooldown} s after each")
    sync_harness_workspace(commit)
    pipe = item_id(HARNESS_WS, "DataPipeline", PIPELINE)
    body = {"executionData": {"parameters": {"queue": queue, "expected_commit": commit}}}
    _, headers, _ = fabric("POST", f"/workspaces/{HARNESS_WS}/items/{pipe}/jobs/instances?jobType=Pipeline", body)
    job_id = headers.get("location").rstrip("/").split("/")[-1]
    QUEUES.mkdir(parents=True, exist_ok=True)
    (QUEUES / f"{job_id}.json").write_text(json.dumps({
        "job_id": job_id, "commit": commit, "started_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "queue": queue}, indent=2) + "\n", encoding="utf-8")
    print(f"Queue started at {commit[:7]}: pipeline job {job_id}, {len(queue)} run(s).")
    print(f"Check it with:   python harness/run_queue.py status {job_id}")
    print(f"Collect with:    python harness/run_queue.py collect {job_id}")


def job(job_id):
    pipe = item_id(HARNESS_WS, "DataPipeline", PIPELINE)
    s, _, out = http("GET", f"{FABRIC}/workspaces/{HARNESS_WS}/items/{pipe}/jobs/instances/{job_id}")
    if s >= 300:
        sys.exit(f"job {job_id}: HTTP {s} {str(out)[:500]}")
    return out


def run_folders(lake_id):
    url = (f"{ONELAKE}/{HARNESS_WS}?resource=filesystem&recursive=false&directory="
           + urllib.parse.quote(f"{lake_id}/Files/harness/runs"))
    _, _, out = http("GET", url, resource="https://storage.azure.com", headers={"x-ms-version": "2023-11-03"})
    return sorted(p["name"].rsplit("/", 1)[-1] for p in out.get("paths", []) if p.get("isDirectory") == "true")


def queue_runs(job_id):
    """Run folders of this queue: status.json carries the pipeline run id."""
    lake_id = item_id(HARNESS_WS, "Lakehouse", LAKEHOUSE)
    started = json.loads((QUEUES / f"{job_id}.json").read_text(encoding="utf-8"))["started_utc"] \
        if (QUEUES / f"{job_id}.json").exists() else ""
    stamp = re.sub(r"[-:]", "", started[:19]) + "Z" if started else ""
    found = []
    for run_id in run_folders(lake_id):
        if stamp and run_id < stamp[:13]:   # run ids start with their UTC start time; skip older folders fast
            continue
        try:
            st = json.loads(download(f"{lake_id}/Files/harness/runs/{run_id}/status.json"))
        except SystemExit:
            continue   # no status.json yet: the run is still going
        if st.get("pipeline_run_id") == job_id:
            found.append((run_id, st))
    return found


def status(job_id):
    j = job(job_id)
    print(f"Pipeline job {job_id}: {j.get('status')}, started {j.get('startTimeUtc')}, ended {j.get('endTimeUtc') or '-'}")
    if j.get("failureReason"):
        print(f"  failure: {json.dumps(j['failureReason'])[:1500]}")
    for run_id, st in queue_runs(job_id):
        local = (ROOT / "results" / "harness" / run_id).is_dir()
        print(f"  {run_id}  {st.get('variant')}  rows {st.get('rows')}"
              f"{'  STOPPED: ' + st['stopped'][:200] if st.get('stopped') else ''}{'  (collected)' if local else ''}")


def collect(job_id):
    runs = queue_runs(job_id)
    new = [(r, st) for r, st in runs if not (ROOT / "results" / "harness" / r).is_dir()]
    print(f"{len(runs)} finished run(s) in this queue, {len(new)} not collected yet")
    for run_id, st in new:
        print(f"== {run_id} {st.get('variant')}")
        pull_results(run_id, st.get("notebook_run_id") or job_id)
    print(f"Pipeline job is {job(job_id).get('status')}.")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("start")
    s.add_argument("variants", nargs="+")
    s.add_argument("--targets", default="F64", help="comma separated: F2,F64,PPU,Pro")
    s.add_argument("--clear-first", action="store_true")
    s.add_argument("--repeats", type=int, default=1,
                   help="rounds over the whole list (round robin); F2 is only in the first round")
    s.add_argument("--cooldown", type=int, default=0, help="seconds to wait after each entry")
    for name in ("status", "collect"):
        sub.add_parser(name).add_argument("job_id")
    a = ap.parse_args()
    if a.cmd == "start":
        start(a.variants, a.targets, a.clear_first, a.repeats, a.cooldown)
    elif a.cmd == "status":
        status(a.job_id)
    else:
        collect(a.job_id)


if __name__ == "__main__":
    main()
