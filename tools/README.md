# Daly Tools

Location: `tools/`

dy_orchestrator.py
  Execute a discipline-scoped collection plan with explicit authorization gating.
  Passive-by-default; active collection requires user authorization.

dy_provenance.py
  Attach observability chain metadata (hash, source, site_id, retention, policy)
  to a dataset artifact.

dy_index_update.py
  Rebuild `00_project/skills-index.md` by scanning discipline READMEs and
  `<discipline>/tools/` folders.

Verified: 2026-08-07 — 5/5 tests passing.
