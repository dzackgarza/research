# pycddlib Lattice Method Reference (Archived Scope Violation)
## Python cddlib wrapper for exact H/V polyhedral workflows

Archived under `docs/archive/scope_violations/` because this surface is polyhedral/LP-focused and outside this project's bilinear-form lattice-theory scope.

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PY]` | Python package surface |
| `[POLY]` | Polyhedral/cone workflow |
| `[HREP]` | Halfspace (inequality) representation surface |
| `[VREP]` | Generator representation surface |
| `[LP]` | Linear-programming surface |
| `[EXACT]` | Exact rational arithmetic pathway |

---

## 1. Scope

`pycddlib` exposes Python bindings for cddlib. The package surface here is focused on:

- exact H-representation and V-representation transformations,
- canonicalization and redundancy removal,
- adjacency/incidence extraction,
- LP solves through cddlib-backed routines.

Not in scope:

- indefinite arithmetic quadratic-form genus/isometry classification.

---

## 2. Representation Contracts

### 2.1 Matrix row conventions

| Surface | Contract | Tags |
|---|---|---|
| H-representation rows `[b A]` | Each row represents `0 <= b + A x`; `lin_set` marks rows treated as equalities. | `[PY, POLY, HREP]` |
| V-representation rows `[t V]` | Rows encode generators with a leading type flag (`0` for rays, `1` for vertices in documented examples). | `[PY, POLY, VREP]` |
| `rep_type` on `Matrix` | Must be set to `RepType.INEQUALITY` or `RepType.GENERATOR` before running representation-dependent routines. | `[PY, POLY]` |

### 2.2 Core constructors

| API | Signature | Description | Tags |
|---|---|---|---|
| `Matrix` | `Matrix(array, *, lin_set=(), rep_type=RepType.UNSPECIFIED, obj_type=LPObjType.NONE, obj_func=None)` | Input matrix container with representation metadata and optional LP objective metadata. | `[PY, POLY, EXACT]` |
| `polyhedron_from_matrix` | `polyhedron_from_matrix(mat, row_order=None)` | Build a `Polyhedron` from matrix input with optional row-order strategy. | `[PY, POLY, HREP, VREP]` |
| `Polyhedron` | `Polyhedron(mat: Matrix, row_order: Optional[RowOrderType] = None)` | Polyhedron/cone object created from H-rep or V-rep matrix data. | `[PY, POLY, HREP, VREP]` |

---

## 3. Canonicalization and Redundancy Surface

| API | Signature | Description | Tags |
|---|---|---|---|
| `Matrix.canonicalize` | `canonicalize(self) -> tuple[Set[int], Set[int], Sequence[NumberType]]` | Canonicalizes matrix rows and returns metadata including linear/redundant sets. | `[PY, POLY, HREP, VREP, EXACT]` |
| `Matrix.matrix_canonicalize` | `matrix_canonicalize(self) -> tuple[Set[int], Set[int], Sequence[NumberType]]` | Alternative canonicalization entry point with the same contract family as `canonicalize`. | `[PY, POLY, HREP, VREP, EXACT]` |
| `Matrix.matrix_redundancy_remove` | `matrix_redundancy_remove(self) -> tuple[Set[int], Sequence[NumberType]]` | Removes redundant rows from matrix representation data. | `[PY, POLY, HREP, EXACT]` |
| `redundancy_remove` | `redundancy_remove(mat) -> tuple[Set[int], Sequence[NumberType]]` | Module-level redundancy removal for matrix objects. | `[PY, POLY, HREP, EXACT]` |
| `redundancy_remove_from_array` | `redundancy_remove_from_array(array, *, lin_set=(), rep_type=RepType.INEQUALITY) -> tuple[Set[int], Sequence[NumberType]]` | Convenience redundancy-removal wrapper from raw arrays. | `[PY, POLY, HREP, EXACT]` |
| `Matrix.matrix_rank` | `matrix_rank(self) -> int` | Rank of the matrix in cddlib-backed exact arithmetic context. | `[PY, POLY, EXACT]` |

---

## 4. Adjacency, Incidence, and Conversion Surface

### 4.1 Matrix-level adjacency tests

| API | Signature | Description | Tags |
|---|---|---|---|
| `Matrix.matrix_adjacency` | `matrix_adjacency(self) -> AdjacencyTestType` | Adjacency extraction on matrix representation data. | `[PY, POLY, HREP, VREP]` |
| `Matrix.matrix_weak_adjacency` | `matrix_weak_adjacency(self) -> AdjacencyTestType` | Weak-adjacency variant for representation matrix analysis. | `[PY, POLY, HREP, VREP]` |
| `Matrix.matrix_append_to` | `matrix_append_to(self, matrix, *, linear=False) -> None` | Appends rows to a target matrix, with optional linearity flag. | `[PY, POLY, HREP, VREP]` |

### 4.2 Polyhedron-level extractors

| API | Signature | Description | Tags |
|---|---|---|---|
| `Polyhedron.copy_generators` | `copy_generators(self) -> Matrix` | Return V-representation (generators/rays) for the polyhedron. | `[PY, POLY, VREP]` |
| `Polyhedron.copy_inequalities` | `copy_inequalities(self) -> Matrix` | Return H-representation (inequalities/equalities) for the polyhedron. | `[PY, POLY, HREP]` |
| `Polyhedron.copy_adjacency` | `copy_adjacency(self) -> Set[Tuple[int, int]]` | Adjacency relation on output representation rows. | `[PY, POLY]` |
| `Polyhedron.copy_incidence` | `copy_incidence(self) -> Tuple[Set[int], ...]` | Incidence relation on output representation rows. | `[PY, POLY]` |
| `Polyhedron.copy_input` | `copy_input(self) -> Matrix` | Copy of the original input matrix. | `[PY, POLY]` |
| `Polyhedron.copy_input_adjacency` | `copy_input_adjacency(self) -> Set[Tuple[int, int]]` | Adjacency relation on input representation rows. | `[PY, POLY]` |
| `Polyhedron.copy_input_incidence` | `copy_input_incidence(self) -> Tuple[Set[int], ...]` | Incidence relation on input representation rows. | `[PY, POLY]` |

---

## 5. Linear Programming Surface

| API | Signature | Description | Tags |
|---|---|---|---|
| `linprog_from_array` | `linprog_from_array(array, obj_type=LPObjType.MAX, obj_func=None, *, rep_type=RepType.INEQUALITY)` | LP solve from array input with explicit objective type and objective vector support. | `[PY, POLY, LP, EXACT]` |
| `linprog_from_matrix` | `linprog_from_matrix(mat)` | LP solve from `Matrix` input carrying representation/objective metadata. | `[PY, POLY, LP, EXACT]` |

---

## 6. Assumptions and Constraints

- The documented APIs operate on cddlib representation data and require correct representation metadata (`rep_type`, and `lin_set` when equalities are intended).
- `row_order` controls are documented for nondegenerate workflows.
- The package surface is polyhedral/rational; no documented contract provides indefinite-form genus/isometry classification semantics.

---

## 7. Sources

- pycddlib docs home: `https://pycddlib.readthedocs.io/en/3.0.2/`
- pycddlib cdd module reference: `https://pycddlib.readthedocs.io/en/3.0.2/cdd.html`
- pycddlib examples page: `https://pycddlib.readthedocs.io/en/3.0.2/examples.html`
- pycddlib LP docs: `https://pycddlib.readthedocs.io/en/3.0.2/lp.html`
- pycddlib repository: `https://github.com/mcmtroffaes/pycddlib`
