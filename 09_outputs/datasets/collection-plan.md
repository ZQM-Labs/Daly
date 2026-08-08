# Daily Dataset Collection Plan — IMINT / MASINT / TECHINT
Generated: 2026-08-07

Scope: global public observability corpus. Passive reference by default; active collection requires explicit user authorization with observability chain metadata.

Cross-links:
- Unified index: `C:\Users\zqmco\INT_TOOLKIT_INDEX.md`
- Upstream: `EaglesNest`
- Property arm: `Whitefeather`

## IMINT — imagery / geospatial
- Focus: satellite and aerial imagery datasets for computer vision / change detection baselines inside `11_imint`.
- Leads:
  - `chrieke/awesome-satellite-imagery-datasets` — curated dataset index
  - `satellite-image-deep-learning/datasets` — broad geospatial dataset list
  - `pubgeo/datasets` — public geospatial datasets
  - `openimages/dataset` — Open Images V4 for CV pretraining
  - `sfikas/medical-imaging-datasets` — medical imaging for BIOINT crossover
- Disposition: manifests in `11_imint/README.md additions table`; downloads gated by explicit user GO with observability chain.

## MASINT — acoustic / measurement signatures
- Focus: sound/audio event datasets for acoustic signature baselines inside `05_masint`.
- Leads:
  - `patchbanks/Lo-Fi-Drums-Dataset` — stamped audio loop dataset
  - `facebookresearch/real-acoustic-fields` — room impulse responses
  - `LCAV/audio-localization-dataset` — acoustic echolocation
- Disposition: manifests in `05_masint/README.md additions table`; gated by explicit GO.

## TECHINT — firmware / binary analysis
- Focus: firmware dataset construction and reverse-engineering workflows inside `08_techint`.
- Leads:
  - `VincentDary/open-firmware-dataset-builder` — reproducible firmware image dataset builder
  - `emproof-com/workshop_firmware_reverse_engineering` — firmware RE exercises
  - `gl0bal01/intel-codex` — SOPs for firmware RE and binary analysis
  - `extremecoders-re/re-list` — reverse engineering tool index
  - `hexsecs/awesome-embedded-security` — embedded security resource list
- Disposition: manifests in `08_techint/README.md additions table`; gated by explicit GO.

---
Policy reminder: passive reference only unless explicitly authorized. All artifacts must include observability chain metadata.
