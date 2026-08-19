# pycddlib Method Test Gap Checklist (Archived Scope Violation)

Archived from active scope. Tracks pycddlib polyhedral methods documented in
`docs/archive/scope_violations/pycddlib/lattice/pycddlib_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Core Constructors and Representation Entry Points

- [ ] `Matrix(array, *, lin_set=(), rep_type=RepType.UNSPECIFIED, obj_type=LPObjType.NONE, obj_func=None)`
- [ ] `polyhedron_from_matrix(mat, row_order=None)`
- [ ] `Polyhedron(mat: Matrix, row_order: Optional[RowOrderType] = None)`

## 2. Matrix Canonicalization and Redundancy Surface

- [ ] `Matrix.canonicalize()`
- [ ] `Matrix.matrix_canonicalize()`
- [ ] `Matrix.matrix_redundancy_remove()`
- [ ] `redundancy_remove(mat)`
- [ ] `redundancy_remove_from_array(array, *, lin_set=(), rep_type=RepType.INEQUALITY)`
- [ ] `Matrix.matrix_rank()`

## 3. Adjacency and Incidence Surface

- [ ] `Matrix.matrix_adjacency()`
- [ ] `Matrix.matrix_weak_adjacency()`
- [ ] `Polyhedron.copy_adjacency()`
- [ ] `Polyhedron.copy_incidence()`
- [ ] `Polyhedron.copy_input_adjacency()`
- [ ] `Polyhedron.copy_input_incidence()`

## 4. H/V Conversion and Extraction Surface

- [ ] `Polyhedron.copy_generators()`
- [ ] `Polyhedron.copy_inequalities()`
- [ ] `Polyhedron.copy_input()`
- [ ] `Matrix.matrix_append_to(matrix, *, linear=False)`

## 5. Linear Programming Surface

- [ ] `linprog_from_matrix(mat)`
- [ ] `linprog_from_array(array, obj_type=LPObjType.MAX, obj_func=None, *, rep_type=RepType.INEQUALITY)`

---

## Domain Caveats

- pycddlib is an exact polyhedral H/V-representation and LP surface for rational cones/polyhedra.
- It is not an arithmetic indefinite-lattice genus/isometry classification API.

---

## References

- `docs/archive/scope_violations/pycddlib/lattice/pycddlib_lattice_reference.md`
- `docs/archive/scope_violations/pycddlib/upstream/pycddlib_online_provenance_2026-02-17.md`
- pycddlib docs home: `https://pycddlib.readthedocs.io/en/3.0.2/`
- pycddlib cdd module docs: `https://pycddlib.readthedocs.io/en/3.0.2/cdd.html`
- pycddlib repository: `https://github.com/mcmtroffaes/pycddlib`
