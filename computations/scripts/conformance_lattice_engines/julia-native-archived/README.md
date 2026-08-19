# Archived Julia-Native Doc Tests

This directory stores the former `tests/julia_doc/*.jl` TestItems-based suite.

Status:
- Archived and no longer used as active tests.
- Active coverage now lives under `tests/julia_pytest/migrated_julia_doc/*.py`.
- Python/pytest is the canonical test runner, and Julia code is exercised via `juliacall`.

Notes:
- `tests/julia_doc/Project.toml` and `tests/julia_doc/Manifest.toml` remain in place for Julia package activation from Python tests.
