from pathlib import Path

from dy_index_update import render, scan
from dy_orchestrator import load_plan, run_plan
from dy_provenance import attach, sha256_of


def test_sha256_of(tmp_path: Path) -> None:
    p = tmp_path / "x.txt"
    p.write_text("x", encoding="utf-8")
    assert len(sha256_of(p)) == 64


def test_attach(tmp_path: Path) -> None:
    artifact = tmp_path / "a.txt"
    artifact.write_text("sample", encoding="utf-8")
    record = attach(artifact, "src", "site", "ret", "verified")
    assert record["site_id"] == "site"
    assert len(record["hash"]) == 64
    assert "passive-by-default" in record["policy"]


def test_run_plan_blocks_unauthorized(tmp_path: Path) -> None:
    plan_path = tmp_path / "plan.json"
    plan_path.write_text(
        '{"items":[{"id":"d1","discipline":"01_geoint","tool":"eo-browser","source":"copernicus","authorized":false}]}\n',
        encoding="utf-8",
    )
    run_dir = tmp_path / "out"
    assert run_plan(load_plan(plan_path), run_dir) == 0
    run_file = next(run_dir.iterdir())
    report = __import__("json").loads(run_file.read_text(encoding="utf-8"))
    assert report["results"][0]["status"] == "blocked"


def test_scan_base(tmp_path: Path) -> None:
    base = tmp_path
    (base / "01_geoint").mkdir()
    (base / "01_geoint" / "README.md").write_text("", encoding="utf-8")
    (base / "01_geoint" / "tools").mkdir()
    (base / "01_geoint" / "tools" / "t.py").write_text("", encoding="utf-8")
    entries = scan(base)
    assert entries[0]["tools"] == ["t.py"]


def test_render_index() -> None:
    entries = [{"discipline": "01_geoint", "readme": True, "tools": ["t.py"]}]
    rendered = render(entries)
    assert "# Daly Toolkit — skill index" in rendered
    assert "01_geoint" in rendered
