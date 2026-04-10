#!/usr/bin/env python3
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "cron" / "jobs.json"
OPENCLAW_BIN = os.environ.get("OPENCLAW_BIN", "openclaw")


def run(cmd, capture_output=True):
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        capture_output=capture_output,
        check=True,
    )
    return result.stdout if capture_output else ""


def flatten_jobs(node):
    jobs = []
    if isinstance(node, dict):
        name = node.get("name")
        job_id = node.get("jobId") or node.get("id")
        if name and job_id:
            jobs.append({"name": name, "id": job_id})
        for value in node.values():
            jobs.extend(flatten_jobs(value))
    elif isinstance(node, list):
        for item in node:
            jobs.extend(flatten_jobs(item))
    return jobs


def load_existing_jobs():
    raw = run([OPENCLAW_BIN, "cron", "list", "--all", "--json"])
    data = json.loads(raw)
    found = flatten_jobs(data)
    dedup = {}
    for job in found:
        dedup[job["id"]] = job
    return list(dedup.values())


def message_from_file(path_str):
    path = ROOT / path_str
    text = path.read_text(encoding="utf-8").strip()
    return " ".join(line.strip() for line in text.splitlines() if line.strip())


def remove_jobs_by_name(name, existing_jobs):
    matches = [job for job in existing_jobs if job["name"] == name]
    for job in matches:
        subprocess.run(
            [OPENCLAW_BIN, "cron", "rm", job["id"]],
            cwd=ROOT,
            text=True,
            check=True,
        )


def add_job(job, timezone):
    message = message_from_file(job["messageFile"])
    cmd = [
        OPENCLAW_BIN,
        "cron",
        "add",
        "--name",
        job["name"],
        "--cron",
        job["cron"],
        "--tz",
        timezone,
        "--session",
        job.get("session", "isolated"),
        "--message",
        message,
        "--exact",
    ]

    delivery = job.get("delivery", "none")

    if isinstance(delivery, str):
        if delivery == "none":
            cmd.append("--no-deliver")
        elif delivery in ("announce", "deliver"):
            cmd.append("--announce")
        else:
            raise ValueError(f"Unknown delivery mode string: {delivery}")
    elif isinstance(delivery, dict):
        mode = delivery.get("mode", "none")
        if mode == "none":
            cmd.append("--no-deliver")
        elif mode == "announce":
            cmd.append("--announce")
            channel = delivery.get("channel")
            to = delivery.get("to")
            if channel:
                cmd.extend(["--channel", channel])
            if to:
                cmd.extend(["--to", to])
            if delivery.get("bestEffort") is True:
                cmd.append("--best-effort-deliver")
        else:
            raise ValueError(f"Unknown delivery mode: {mode}")
    else:
        raise ValueError("delivery must be a string or object")

    subprocess.run(cmd, cwd=ROOT, text=True, check=True)


def main():
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    timezone = config["timezone"]
    desired_jobs = config["jobs"]
    existing_jobs = load_existing_jobs()

    for job in desired_jobs:
        remove_jobs_by_name(job["name"], existing_jobs)
        add_job(job, timezone)

    print("Cron jobs installed or refreshed from cron/jobs.json")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(exc.stdout or "", end="")
        print(exc.stderr or "", end="", file=sys.stderr)
        raise
