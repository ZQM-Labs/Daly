"""Daly collection orchestrator.

Executes a discipline-scoped collection plan with explicit authorization gate.
Reads a JSON plan from `09_outputs/datasets/collection-plan.json` and
runs corresponding reference scripts under `08_techint/scripts/` and
`03_osint/scripts/` only when `authorized == true`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def load_plan(plan_path: Path) -> dict:
    return json.loads(plan_path.read_text(encoding="utf-8"))


def run_plan(plan: dict, out_dir: Path) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    run_at = datetime.now(UTC).isoformat()
    results = []
    for item in plan.get("items", []):
        if not item.get("authorized", False):
            results.append(
                {"id": item.get("id"), "status": "blocked", "reason": "not authorized"}
            )
            continue
        source = item.get("source", "")
        discipline = item.get("discipline", "")
        tool = item.get("tool", "")
        record = {
            "id": item.get("id"),
            "discipline": discipline,
            "tool": tool,
            "source": source,
            "status": "reference-only",
            "run_at": run_at,
            "notes": "Tooling is reference surface; live execution requires harness entrypoint under tools/.",
        }
        results.append(record)

    report_path = (
        out_dir / f"run_{run_at.replace(':', '').replace('-', '').split('.')[0]}.json"
    )
    report_path.write_text(
        json.dumps({"run_at": run_at, "results": results}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"run report: {report_path}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Daly collection orchestrator")
    ap.add_argument("--plan", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, required=True)
    args = ap.parse_args()
    plan = load_plan(args.plan)
    return run_plan(plan, args.out_dir)


if __name__ == "__main__":
    raise SystemExit(main())
