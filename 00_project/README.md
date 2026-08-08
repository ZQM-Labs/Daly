# Daly Toolkit — Project

Global observability training and implementation scaffold.
Upstream: `EaglesNest`. Property arm: `Whitefeather`.

Core disciplines:
- 01_geoint
- 02_sigint
- 03_osint
- 04_humint
- 05_masint
- 06_cybint
- 07_finint
- 08_techint

Outputs folder:
- 09_outputs

Constraints:
- No active adversarial collection without explicit per-domain authorization.
- Local processing by default; external/cloud tooling opt-in only.
- Every dataset/output must carry observability chain metadata: source, collected, verified, hash, retention, site_id.
- Retain provenance/timestamp/consent metadata for all datasets.
- This toolkit mirrors EaglesNest capability surface; authoritative upstream remains `EaglesNest`.

Use:
- Read each README for discipline-specific workflow notes.
- Place new evidence/captures into corresponding numbered folder with timestamp prefixes.
- Mark final deliverables under `09_outputs/` with checksums/logs when appropriate.
- Weekly sync with `Whitefeather/00_eaglesnest_mirror/` for alignment.
