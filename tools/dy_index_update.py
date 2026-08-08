"""Daly skill index updater.

Rebuilds `00_project/skills-index.md` by scanning each discipline folder
for `README.md` and listing executable tools under `<discipline>/tools/`.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def scan(base: Path) -> list[dict]:
    entries = []
    for discipline in sorted(
        p for p in base.iterdir() if p.is_dir() and not p.name.startswith(".")
    ):
        readme = discipline / "README.md"
        tools_dir = discipline / "tools"
        entry = {
            "discipline": discipline.name,
            "readme": readme.exists(),
            "tools": [p.name for p in tools_dir.glob("*.py")]
            if tools_dir.exists()
            else [],
        }
        entries.append(entry)
    return entries


def render(entries: list[dict]) -> str:
    lines = [
        "# Daly Toolkit — skill index",
        "",
        "| Discipline | README | Tools |",
        "|------------|--------|-------|",
    ]
    for e in entries:
        tools = ", ".join(f"`{t}`" for t in e["tools"]) or "—"
        readme = "✓" if e["readme"] else "✗"
        lines.append(f"| {e['discipline']} | {readme} | {tools} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Daly skill index updater")
    ap.add_argument("--base", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    entries = scan(args.base)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render(entries), encoding="utf-8")
    print(f"index written: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
