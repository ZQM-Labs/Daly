"""Daly provenance attacher.

Attaches observability chain metadata to a dataset artifact manifest.
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


def attach(
    artifact: Path, source: str, site_id: str, retention: str, verified: str
) -> dict:
    return {
        "artifact": str(artifact),
        "source": source,
        "collected": datetime.now(UTC).isoformat(),
        "verified": verified,
        "hash": sha256_of(artifact),
        "retention": retention,
        "site_id": site_id,
        "policy": "passive-by-default; active-only when authorized",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Daly provenance attacher")
    ap.add_argument("--artifact", type=Path, required=True)
    ap.add_argument("--source", required=True)
    ap.add_argument("--site-id", required=True)
    ap.add_argument("--retention", required=True)
    ap.add_argument("--verified", required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    if not args.artifact.exists():
        raise SystemExit(f"artifact missing: {args.artifact}")
    record = attach(
        args.artifact, args.source, args.site_id, args.retention, args.verified
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"provenance record: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
