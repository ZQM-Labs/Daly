# Daly

Skill index builder + collection orchestrator + provenance attacher.

## CLI tools

`tools/dy_index_update.py`
- Scan discipline folders for `README.md` and tools under `<discipline>/tools/`.
- Write `skills-index.md` table: discipline, README status, tool list.

`tools/dy_orchestrator.py`
- Read a JSON collection plan and execute only authorized items.
- Blocked items are recorded as `"blocked"` with reason `"not authorized"`.
- Writes timestamped JSON run report to output directory.

`tools/dy_provenance.py`
- Attach observability chain metadata to an artifact.
- Emits JSON with source, collected timestamp, SHA-256 hash, retention, policy.

## Usage

```bash
python tools/dy_index_update.py --base 00_project --out skills-index.md
python tools/dy_orchestrator.py --plan collection-plan.json --out-dir 09_outputs/runs
python tools/dy_provenance.py --artifact dataset.zip --source copernicus --site-id site-001 --retention 90d --verified today --out provenance.json
```

## Verify

```bash
make ci
```

## Integration: zqm-intel-platforms
This repo vendors `zqm-intel-platforms>=0.1.0` as a dependency. Use the shared SIEM/OSINT/CTI wrappers for Splunk HEC, Loki, and Windows-telemetry export defined in that package.
