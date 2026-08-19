# pycddlib Online Provenance Snapshot (2026-02-17 UTC)

Scope: first-class checklist/reference creation for the missing `pycddlib` package surface.

---

## 1. Sources surveyed

Canonical upstream docs and repository:

- `https://pycddlib.readthedocs.io/en/3.0.2/`
- `https://pycddlib.readthedocs.io/en/3.0.2/cdd.html`
- `https://pycddlib.readthedocs.io/en/3.0.2/examples.html`
- `https://pycddlib.readthedocs.io/en/3.0.2/lp.html`
- `https://github.com/mcmtroffaes/pycddlib`

---

## 2. Extracted method surface

From the cdd module and API docs:

- Core constructors and entry points:
  - `Matrix(...)`
  - `polyhedron_from_matrix(...)`
  - `Polyhedron(...)`
- Canonicalization/redundancy:
  - `Matrix.canonicalize`
  - `Matrix.matrix_canonicalize`
  - `Matrix.matrix_redundancy_remove`
  - `redundancy_remove`
  - `redundancy_remove_from_array`
  - `Matrix.matrix_rank`
- Adjacency/incidence and extraction:
  - `Matrix.matrix_adjacency`
  - `Matrix.matrix_weak_adjacency`
  - `Matrix.matrix_append_to`
  - `Polyhedron.copy_generators`
  - `Polyhedron.copy_inequalities`
  - `Polyhedron.copy_adjacency`
  - `Polyhedron.copy_incidence`
  - `Polyhedron.copy_input`
  - `Polyhedron.copy_input_adjacency`
  - `Polyhedron.copy_input_incidence`
- LP surface:
  - `linprog_from_array`
  - `linprog_from_matrix`

---

## 3. Representation and constraint notes captured

- H-representation rows follow documented `[b A]` form with inequalities `0 <= b + A x`.
- V-representation rows follow documented `[t V]` form (examples use `t=0` rays, `t=1` vertices).
- `rep_type` and `lin_set` metadata are part of the API contract and must align with the intended representation semantics.
- The package surface is exact polyhedral/LP tooling, not a quadratic-form indefinite genus/isometry stack.
