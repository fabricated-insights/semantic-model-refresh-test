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
from run_variant import (FABRIC, HARNESS_WS, LAKEHOUSE, ONELAKE, REMOTE, ROOT, check_pushed,  # noqa: E402
                         download, fabric, git, http, item_id, pull_results, sync_harness_workspace)

PIPELINE = "harness-queue"
QUEUES = ROOT / "results" / "queues"


# Targets whose workspace follows a branch other than main (source tests). Same map as in the notebook.
BRANCH_OF = {"F2-csv": "csv-switch", "F2-sql": "sql-switch", "F64-NE": "sql-switch"}


def committed_params(variant, ref):
    """DataTag and SourceType of a variant as committed at ref (HEAD for main, the pinned branch commit)."""
    text = git("show", f"{ref}:models/{variant}/{variant}.SemanticModel/definition/expressions.tmdl")
    tag = re.search(r'expression\s+DataTag\s*=\s*"([^"]+)"', text)
    src = re.search(r'expression\s+SourceType\s*=\s*"([^"]+)"', text)
    if not tag:
        sys.exit(f"No DataTag in {variant} at {ref}")
    return tag.group(1), (src.group(1) if src else "parquet")   # models from before the parameter load Parquet


def build_queue(variants, targets, repeats, cooldown, clear_first, once=(), ref="HEAD"):
    """Round robin: every variant once, then every variant again, so the repeats of one model are spread
    over the whole queue instead of running back to back. F2 is only in the first round: its result is
    pass or fail, and more F2 runs wait for a decision after the first. Variants in `once` (a failure
    that repeats the same way, such as v19 on Pro) are only in the first round too."""
    tags = {v: committed_params(v, ref) for v in variants}
    queue = []
    for rnd in range(1, repeats + 1):
        caps = [t for t in targets if rnd == 1 or not t.startswith("F2")]
        if not caps:
            break
        for v in (variants if rnd == 1 else [v for v in variants if v not in once]):
            queue.append({"variant": v, "targets": ",".join(caps), "data_tag": tags[v][0], "source_type": tags[v][1],
                          "clear_first": "true" if clear_first else "false",
                          "deploy_pro": "true" if "Pro" in caps else "false", "task": "refresh",
                          "cooldown_seconds": cooldown, "round": rnd})
    return queue


def running_queues():
    """Queues started from this repo that are still running: [(job id, record, targets)]."""
    out = []
    for f in sorted(QUEUES.glob("*.json")) if QUEUES.is_dir() else []:
        rec = json.loads(f.read_text(encoding="utf-8"))
        if rec.get("finished"):
            continue
        st = job(rec["job_id"]).get("status")
        if st in ("NotStarted", "InProgress"):
            caps = {t for q in rec["queue"] for t in q["targets"].split(",")}
            out.append((rec["job_id"], rec, caps))
        else:
            rec["finished"] = st
            f.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    return out


def start(variants, targets, clear_first, repeats=1, cooldown=0, once=(), branch_override=""):
    for v in list(variants) + list(once):
        if not (ROOT / "models" / v).is_dir():
            sys.exit(f"models/{v} does not exist")
    targets = [t.strip() for t in targets.split(",") if t.strip()]
    commit = check_pushed()
    # Queues may run side by side, one per capacity. Two on the same capacity would refresh the same model
    # twice at once, and a queue at another commit would have its workspaces moved under it.
    for jid, rec, caps in running_queues():
        if caps & set(targets):
            sys.exit(f"Queue {jid} is still running on {', '.join(sorted(caps & set(targets)))}. Wait for it.")
        if rec["commit"] != commit:
            sys.exit(f"Queue {jid} is running at {rec['commit'][:7]}, HEAD is {commit[:7]}. "
                     f"A queue at another commit would update the workspaces under it. Wait for it.")
    # One branch per queue: main, or the branch the source-test targets follow. Its commit is pinned.
    branches = {branch_override} if branch_override else {BRANCH_OF.get(t, "main") for t in targets}
    if len(branches) > 1:
        sys.exit(f"Targets {targets} follow different branches ({', '.join(sorted(branches))}); one queue per branch.")
    branch = branches.pop()
    pinned, ref = {"main": commit}, "HEAD"
    if branch != "main":
        git("fetch", REMOTE, branch)
        pinned[branch] = git("rev-parse", f"{REMOTE}/{branch}")
        ref = pinned[branch]
        print(f"  targets follow branch {branch}, pinned at {ref[:7]}")
    if branch_override:   # the workspace was switched to another branch than BRANCH_OF says
        pinned["branch_of"] = {t: branch_override for t in targets}
    queue = build_queue(variants, targets, repeats, cooldown, clear_first, set(once), ref)
    for v in variants:
        q = next(e for e in queue if e["variant"] == v)
        print(f"  {v}: DataTag {q['data_tag']}, SourceType {q['source_type']}")
    for rnd in sorted({q["round"] for q in queue}):
        print(f"  round {rnd}: {sum(1 for q in queue if q['round'] == rnd)} entries, targets "
              f"{next(q['targets'] for q in queue if q['round'] == rnd)}")
    print(f"  {len(queue)} entries in all, cooldown {cooldown} s after each")
    sync_harness_workspace(commit)
    pipe = item_id(HARNESS_WS, "DataPipeline", PIPELINE)
    body = {"executionData": {"parameters": {"queue": queue, "expected_commit": json.dumps(pinned)}}}
    _, headers, _ = fabric("POST", f"/workspaces/{HARNESS_WS}/items/{pipe}/jobs/instances?jobType=Pipeline", body)
    job_id = headers.get("location").rstrip("/").split("/")[-1]
    QUEUES.mkdir(parents=True, exist_ok=True)
    (QUEUES / f"{job_id}.json").write_text(json.dumps({
        "job_id": job_id, "commit": commit, "pinned": pinned, "started_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "queue": queue}, indent=2) + "\n", encoding="utf-8")
    print(f"Queue started at {commit[:7]}: pipeline job {job_id}, {len(queue)} run(s).")
    print(f"Check it with:   python harness/run_queue.py status {job_id}")
    print(f"Collect with:    python harness/run_queue.py collect {job_id}")


def job(job_id):
    # A queue started on another pipeline (the source-test copy) records where it runs.
    rec_file = QUEUES / f"{job_id}.json"
    rec = json.loads(rec_file.read_text(encoding="utf-8")) if rec_file.exists() else {}
    ws = rec.get("pipeline_workspace", HARNESS_WS)
    pipe = rec.get("pipeline_id") or item_id(HARNESS_WS, "DataPipeline", PIPELINE)
    s, _, out = http("GET", f"{FABRIC}/workspaces/{ws}/items/{pipe}/jobs/instances/{job_id}")
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
    s.add_argument("--once", default="", help="comma separated variants that run in the first round only")
    s.add_argument("--branch", default="", help="branch the target workspaces follow, if not the one in BRANCH_OF")
    for name in ("status", "collect"):
        sub.add_parser(name).add_argument("job_id")
    a = ap.parse_args()
    if a.cmd == "start":
        once = [v.strip() for v in a.once.split(",") if v.strip()]
        start(a.variants, a.targets, a.clear_first, a.repeats, a.cooldown, once, a.branch)
    elif a.cmd == "status":
        status(a.job_id)
    else:
        collect(a.job_id)


if __name__ == "__main__":
    main()
