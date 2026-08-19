# Documentation Gaps - Bilinear-Form Lattice Methods

Reference docs (`docs/*/lattice/*.md`) track method surfaces with source-backed signatures.
Checklist files (`docs/*_methods_checklist.md`) track TEST COVERAGE - separate task.

## Goal 1: Local Doc Integration

Local upstream docs under `docs/**/upstream/` are required before contract-fidelity work can proceed.

Known gaps: check each package directory under `docs/` for an `upstream/` subdirectory. Create missing ones.

## Goal 2: Contract-Fidelity Work

Completeness and provable correctness of all documented methods across all reference docs under `docs/`.

For each reference doc: verify typed signatures, argument constraints, source citations, and domain assumptions (definiteness, ring, etc.) are explicit.

This goal has no terminal state. Find a gap and fix it.
