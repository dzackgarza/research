# HyperCells Online Provenance Snapshot (2026-02-17)

## Purpose

Records the exact upstream HyperCells sources used to build the first-class checklist/reference surfaces in this repository.

## Survey Date

- 2026-02-17 (UTC)

## Canonical Sources

- Package landing page (version, scope, package dependencies, known limitations):
  - `https://gap-packages.github.io/HyperCells/`
- Manual contents/index:
  - `https://www.hypercells.net/chap0_mj.html`
- Manual chapter 2 (core types/attributes/interfaces):
  - `https://www.hypercells.net/chap2_mj.html`
- Manual chapter 3 (triangle-group cells and supercells):
  - `https://www.hypercells.net/chap3_mj.html`
- Manual chapter 4 (cell-graph model methods):
  - `https://www.hypercells.net/chap4_mj.html`
- Manual chapter 5 (supercell enumeration):
  - `https://www.hypercells.net/chap5_mj.html`
- Manual chapter 6 (HyperCell database methods):
  - `https://www.hypercells.net/chap6_mj.html`
- Manual chapter 7 (point-group representation workflows):
  - `https://www.hypercells.net/chap7_mj.html`
- Manual chapter 8 (display/export APIs):
  - `https://www.hypercells.net/chap8_mj.html`

## Key Upstream Statements Localized

- Constructors and workflows exposing `simplifyMethod` document:
  - `MaximalTree` default,
  - optional `KnuthBendix` mode requiring package `kbmag`.
- Package page limitation notes include:
  - incomplete full support for compact hyperbolic 3D orbifolds,
  - incomplete support for chiral/non-orientable orbifolds in dimensions greater than 3 for `TGCellGraph`,
  - `boundByGenus` support currently restricted to type values below 102 for selected type/species database methods.

## Repository Surfaces Fed By This Snapshot

- `docs/hypercells_methods_checklist.md`
- `docs/hypercells/lattice/hypercells_lattice_reference.md`
