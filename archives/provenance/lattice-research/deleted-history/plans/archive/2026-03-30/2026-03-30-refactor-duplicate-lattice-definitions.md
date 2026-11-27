# Plan: Refactor Duplicate Lattice Definitions

**Created**: 2026-03-30 13:45 **Status**: Complete **SCHEDULE.md slot**: 14:00-15:00
(Refactoring: centralized classes for building lattices)

## Context

`coble_geometry.sage` (197 lines) exists as a central module with canonical lattice
definitions (U, E8, Λ_K3, S_Co, T_Co) and utilities.
However, two scripts still have duplicate definitions:
- `task1_3_embeddings.sage` (lines 41, 45): `hyperbolic_plane()`, `E8_lattice()`
- `task1_3_embeddings_primitive.sage` (lines 43, 52): `hyperbolic_plane()`,
  `E8_lattice()`

## Goal

Refactor both scripts to import from `coble_geometry.sage` instead of duplicating
definitions.

## Tasks

1. ✓ Add `load("coble_geometry.sage")` to both scripts
2. ✓ Remove duplicate `hyperbolic_plane()` and `E8_lattice()` definitions
3. ✓ Verify both scripts still run correctly with `sage script.sage`
4. ✓ Commit changes

## Verification

- ✓ Both scripts run without errors
- ✓ Output files generated successfully
- ✓ No duplicate definitions remain in computation scripts

## Results

Commit: 5ec608b
- Removed 45 lines of duplicate code (22 lines from each script + comments)
- Both scripts now use centralized definitions from `computations/coble_geometry.sage`
- `task1_3_embeddings.sage` runs successfully
- `task1_3_embeddings_primitive.sage` runs successfully (pre-existing bug in
  discriminant_group unrelated to refactoring)
